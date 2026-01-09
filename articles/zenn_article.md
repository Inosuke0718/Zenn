---
title: "【個人開発】Gemini 2.5 FlashでPDFを「聴ける」ようにするデスクトップアプリを作ってみた"
emoji: "🔊"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ["python", "gemini", "gui", "個人開発", "初心者向け"]
published: false
---

# はじめに

技術書や論文、英語のドキュメントを読むとき、「**これ、音声で聴き流せたら便利なのになぁ**」と思ったことはありませんか？
特に英語の PDF は、読んで理解するのにエネルギーを使うため、通勤中や作業中に「ながら聴き」できれば最高です。

そこで今回は、Google の最新 AI モデル **Gemini 2.5 Flash** を使って、**PDF を読み込み、章ごとに翻訳して、自然な英語音声に変換するデスクトップアプリ「DocuVoice AI」** を作ってみました。

この記事では、初学者の方向けに、このアプリがどのような仕組みで動いているのか、Python でどうやって実装したのかを分かりやすく解説します。

# 作ったもの

**DocuVoice AI (Desktop Edition)** という Windows アプリです。

## 主な機能

1. **PDF ドラッグ＆ドロップ**: 読みたい PDF ファイルを GUI にポイっと入れるだけ。
2. **AI による構造解析**: Gemini Vision API を使って、複雑なレイアウトの PDF でも正しくテキストを抽出し、自動で「章 (Chapter)」ごとに分割します。
3. **翻訳 & 音声合成**: 抽出したテキストを必要に応じて翻訳し、Gemini の TTS モデルで高品質な音声に変換します。
4. **マージ**: 章ごとの音声ファイルを 1 つの MP3 ファイルに結合して出力します。

UI はこんな感じで、シンプルに作りました。
![DocuVoice](images/DocuVoice.png)

# 技術スタック

「なるべくシンプルに、かつ最新の技術を使う」をテーマに選定しました。

- **言語**: Python 3.12
- **GUI フレームワーク**: [FreeSimpleGUI](https://github.com/spyoungtech/FreeSimpleGUI)
  - 以前は PySimpleGUI として知られていたライブラリの派生版です。直感的に GUI が組めるので初心者におすすめです。
- **AI モデル**: **Google Gemini 2.5 Flash**
  - 高速かつ安価で、マルチモーダル（画像もテキストも音声も扱える）なのが特徴です。
  - SDK: `google-genai`
- **PDF 処理**: PyMuPDF (`fitz`)
  - PDF のページ数カウントやバリデーションに使用。
- **音声処理**: FFmpeg
  - 生成された音声ファイルの結合に使用。
- **配布**: PyInstaller
  - Python が入っていない PC でも動くように `.exe` 化します。

# 特徴的な実装ポイント

このアプリの「賢い」部分（Brain）の実装について解説します。

## 1. 従来の OCR ではなく「Vision API」で読む

PDF からテキストを抽出するとき、`PyPDF2`などの従来のライブラリを使うと、段組（2 カラムレイアウト）や図表のキャプションが混ざってしまい、読む順序がおかしくなることがよくあります。

そこで、今回は **Gemini Vision API** に「**PDF のページ画像をそのまま見せる**」という豪快なアプローチを取りました。
人間が目で見て読むのと同じように、AI に画像として認識させることで、レイアウトを正しく解釈させることができます。

### 特製のプロンプト (Prompt Engineering)

さらに工夫したのが「章ごとの分割」です。
テキストをただ抽出するのではなく、プロンプトで「章の区切りに特定のマーカーを入れて！」と指示を出しています。

実際のコード (`src/core/pdf_processor.py`) の一部です：

```python
prompt = """You are a document analysis expert. Extract ALL text content from this PDF document.

Instructions:
1. Read the document as a human would, following the natural reading order
2. Preserve the document structure (chapters, sections, paragraphs)
...
Output the extracted text in a clean, readable format.
Mark chapter/section boundaries with "===CHAPTER===" followed by the chapter title.
"""
```

こうすることで、AI が出力してきたテキストには `===CHAPTER=== Introduction` のような区切りが入るので、あとはプログラムで `msg.split("===CHAPTER===")` するだけで綺麗に章分けができます。
正規表現や複雑なロジックを書く必要がなく、AI の力を最大限に活用した部分です。

## 2. Gemini で音声合成 (TTS)

Gemini はテキスト生成だけでなく、音声生成も可能です。
`gemini-2.5-flash-preview-tts` というモデルを使用しています。

```python
# src/core/gemini_client.py より抜粋

response = self.client.models.generate_content(
    model="gemini-2.5-flash-preview-tts",
    contents=prompt,
    config=types.GenerateContentConfig(
        response_modalities=["AUDIO"],
        speech_config=types.SpeechConfig(
            voice_config=types.VoiceConfig(
                prebuilt_voice_config=types.PrebuiltVoiceConfig(
                    voice_name="Iapetus", # 落ち着いた男性の声
                )
            )
        ),
    ),
)
```

非常に自然な発音で、長文の読み上げにも対応してくれます。

## 3. UI は「FreeSimpleGUI」でサクッと

GUI 開発というと難しそうですが、Python には `FreeSimpleGUI` という「リストの中に部品を並べるだけ」で作れるライブラリがあります。

メイン画面のレイアウト定義はこれだけです：

```python
layout = [
    [sg.Text("DocuVoice AI", font=("Meiryo UI", 16))],
    [sg.Input(key="-PDF-PATH-"), sg.FileBrowse("選択")],
    [sg.Button("変換開始", key="-START-")],
    [sg.ProgressBar(100, key="-PROGRESS-BAR-")],
]
```

これだけでウィンドウが作れるので、ロジックの実装に集中できました。
実際のアプリでは、処理中に画面がフリーズしないように `threading` モジュールを使って、重い AI 処理を別スレッドで動かす工夫をしています。

# 配布に向けた工夫 (PyInstaller)

自分だけで使うなら Python スクリプトのままでいいのですが、友人に使ってもらうために `.exe` 化にも挑戦しました。

`PyInstaller` を使いましたが、いくつかハマりポイントがありました。
特に、外部ファイル（アイコン画像など）を含める場合、パスの指定に注意が必要です。

```python
# 実行ファイル化されたときは sys._MEIPASS という一時フォルダが使われる
if hasattr(sys, '_MEIPASS'):
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")
```

このようなコードを入れて、開発環境でも実行ファイル形式でも正しくリソースを読み込めるようにしました。

# Gemini API 取得方法

TBD

# まとめ

今回は、Gemini のマルチモーダル能力（視覚・音声）をフル活用して、実用的なデスクトップアプリを作成しました。

- **Vision API** でレイアウト崩れを防ぐ
- **LLM** で章分割を自動化する
- **SimpleGUI** で手軽に UI を作る

この 3 点を組み合わせることで、個人開発でもかなり高機能なツールが短期間で作れることがわかりました。
皆さんもぜひ、身の回りの「ちょっと不便」を AI と Python で解決してみてください！

---
