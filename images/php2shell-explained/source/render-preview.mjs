import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const source = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(source, '../../..');
const review = path.join(root, 'docs/php2shell-figures-review');
const { default: markdownToHtml } = await import(pathToFileURL(path.join(review, 'node_modules/zenn-markdown-html/dist/index.js')));
const markdown = (await fs.readFile(path.join(root, 'articles/php2shell-explained.md'), 'utf8')).replace(/^---[\s\S]*?---\s*/, '');
const escapeHtml = text => text.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;');
const rendered = (await markdownToHtml(markdown, {
  customEmbed: { mermaid: code => `<pre class="mermaid">${escapeHtml(code)}</pre>` },
})).replaceAll('https://raw.githubusercontent.com/Inosuke0718/Zenn/main/images/', '/images/');
const html = `<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>PHP2Shell 図版確認</title>
<link rel="stylesheet" href="/docs/php2shell-figures-review/node_modules/zenn-content-css/lib/index.css">
<style>body{margin:0;color:#253447;background:#fff;font-family:"Yu Gothic",Meiryo,sans-serif}main{max-width:760px;margin:40px auto;padding:0 20px}.mermaid{text-align:center;background:#fafafa!important;border:1px solid #e4e7eb}.mermaid svg{height:auto}h1{font-size:26px}figure{margin:0}img{height:auto}*{box-sizing:border-box}@media(max-width:600px){main{margin:20px auto}}</style>
</head><body><main class="znc"><h1>PHP2Shell 図版確認</h1>${rendered}</main></body></html>`;
await fs.writeFile(path.join(review, 'article.html'), html);
console.log('Built docs/php2shell-figures-review/article.html');
