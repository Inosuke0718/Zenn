"""Render the editable SVG and inspect article layout with real Zenn Markdown/CSS.

One-time dependencies:
  npm install --prefix docs/php2shell-figures-review zenn-markdown-html@0.5.2 zenn-content-css@0.5.8 mermaid@11.17.2
  pip install playwright
  playwright install chromium
Run from any directory: python images/php2shell-explained/source/render-review.py
"""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import json
import os
import re
import subprocess
from threading import Thread
from urllib.parse import unquote, urlsplit

from playwright.sync_api import sync_playwright

SOURCE = Path(__file__).resolve().parent
ROOT = SOURCE.parents[2]
REVIEW = ROOT / 'docs/php2shell-figures-review'
REVIEW.mkdir(parents=True, exist_ok=True)


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def available_chromium(playwright):
    expected = Path(playwright.chromium.executable_path)
    if expected.is_file():
        return expected
    # An existing local Playwright browser is sufficient for static figure QA.
    cache = Path(os.environ['LOCALAPPDATA']) / 'ms-playwright'
    candidates = sorted(cache.glob('chromium_headless_shell-*/chrome-headless-shell-win64/chrome-headless-shell.exe'))
    if not candidates:
        raise RuntimeError('Install Chromium with: playwright install chromium')
    return candidates[-1]


def check_sources():
    article = (ROOT / 'articles/php2shell-explained.md').read_text(encoding='utf-8')
    blocks = re.findall(r'```mermaid\n(.*?)```', article, flags=re.S)
    assert len(blocks) == 2
    for code, name in zip(blocks, ['01_公開までの段取り', '07_きっかけと乗っ取りの違い']):
        assert code.strip() == (SOURCE / f'{name}.mmd').read_text(encoding='utf-8').strip()
    for url in re.findall(r'!\[[^\]]*\]\((https://raw\.githubusercontent\.com/[^\s)]+)', article):
        relative = unquote(urlsplit(url).path.split('/main/', 1)[1])
        assert (ROOT / relative).is_file(), relative


check_sources()
subprocess.run(['node', str(SOURCE / 'render-preview.mjs')], cwd=ROOT, check=True)
server = ThreadingHTTPServer(('127.0.0.1', 0), partial(QuietHandler, directory=str(ROOT)))
Thread(target=server.serve_forever, daemon=True).start()
origin = f'http://127.0.0.1:{server.server_port}'
report = {}
try:
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=str(available_chromium(p)))
        page = browser.new_page(viewport={'width': 800, 'height': 900}, device_scale_factor=1)
        page.goto(origin + '/images/php2shell-explained/source/02_PHPの層とブラウザー.svg')
        page.evaluate('document.fonts.ready')
        page.screenshot(path=str(SOURCE.parent / '02_PHPのどの層か.png'))
        for width in [1080, 375]:
            page.set_viewport_size({'width': width, 'height': 1000})
            errors = []
            page.on('pageerror', lambda error: errors.append(str(error)))
            page.goto(origin + '/docs/php2shell-figures-review/article.html')
            page.add_script_tag(path=str(REVIEW / 'node_modules/mermaid/dist/mermaid.min.js'))
            page.evaluate('''async () => {
              mermaid.initialize({startOnLoad:false, securityLevel:'strict',theme:'neutral',fontFamily:'"Yu Gothic",Meiryo,sans-serif',flowchart:{htmlLabels:true}});
              await mermaid.run({querySelector:'.mermaid'});
              await document.fonts.ready;
              for (const img of document.images) img.loading = 'eager';
              await Promise.all([...document.images].map(img => img.decode()));
            }''')
            layout = page.evaluate('''() => ({
              documentWidth:document.documentElement.scrollWidth,
              viewport:innerWidth,
              images:[...document.images].map(i=>({src:i.getAttribute('src'),width:i.clientWidth,naturalWidth:i.naturalWidth})),
              diagrams:document.querySelectorAll('.mermaid svg').length
            })''')
            assert not errors, errors
            assert layout['documentWidth'] == width, layout
            assert layout['diagrams'] == 2, layout
            assert len(layout['images']) == 4, layout
            assert all(image['naturalWidth'] > 0 for image in layout['images']), layout
            page.screenshot(path=str(REVIEW / f'article-{width}.png'), full_page=True)
            for index, figure in enumerate(page.locator('.znc img, .mermaid').all()):
                figure.screenshot(path=str(REVIEW / f'figure-{width}-{index}.png'))
            page.locator('table').nth(3).screenshot(path=str(REVIEW / f'roles-{width}.png'))
            report[str(width)] = layout
        browser.close()
finally:
    server.shutdown()
(REVIEW / 'verification.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(report, ensure_ascii=False, indent=2))
