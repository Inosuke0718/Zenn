---
title: "【デスクトップアプリ入門】Electron + React + Viteで爆速デスクトップアプリ開発（安全＆確実に起動）"
emoji: "⚡"
type: "tech"
topics: ["electron", "react", "vite", "typescript", "desktop-app"]
published: false
---

「デスクトップアプリを作りたいけど、Electronって環境構築が面倒くさそう…」
「Webpackの設定で挫折した…」

そんなあなたに朗報です。**Vite** を使えば、Electronの開発環境はかなりスムーズに整います。

この記事では、初学者向けに **Electron + React + Vite + TypeScript** の構成で、

1. ちゃんと `npm run dev` でElectronが起動する
2. 最低限のセキュリティ（`contextIsolation` など）を押さえる  
   ところまでを丁寧に解説します。

## なぜこの構成なのか？

- Electron: Web技術（HTML/CSS/JS）でWindows/Mac/Linuxアプリが作れるフレームワーク
- React: 宣言的UIで管理しやすい
- Vite: 開発サーバーとHMRが高速で体験が良い
- TypeScript: 型安全で事故を減らせる

これらを組み合わせると「Web開発のノウハウそのままで」デスクトップアプリを作れます。

## 1. プロジェクト作成（React + TS）

```bash
npm create vite@latest my-electron-app -- --template react-ts
cd my-electron-app
npm install
```

ここまででReactが動く状態です。

## 2. Electron周りを導入

今回は「Viteの開発サーバー起動と一緒に、Electronも自動で立ち上げる」ために `vite-plugin-electron` を使います。  
このプラグインは、Viteのビルド完了フックで `electron .` を実行して起動（または再起動）する仕組みになっています。

```bash
# Electron本体
npm install -D electron

# Vite と Electron を繋ぐプラグイン
npm install -D vite-plugin-electron

# 配布（パッケージング）用（任意：配布までやるなら入れておく）
npm install -D electron-builder
```

## 3. ディレクトリ構成

Electronは「メインプロセス（OS側）」と「レンダラープロセス（画面側）」の2つで動きます。

```text
my-electron-app/
├── electron/             <-- 新規作成（メインプロセス系）
│   ├── main.ts           <-- アプリの本体
│   └── preload.ts        <-- 安全な通信の橋渡し
├── src/                  <-- React（レンダラープロセス）
├── dist/                 <-- Vite build成果物（自動生成）
├── dist-electron/        <-- Electron側のビルド成果物（自動生成）
├── vite.config.ts
└── package.json
```

※ `vite-plugin-electron` はデフォルトで `electron/` 配下を `dist-electron/` にビルドします。

## 4. 実装（main / preload / vite.config）

### electron/main.ts（アプリ本体）

ポイントは「開発モードの切り分け」と「セキュリティの確保」です。

#### 1. 仕組み：なぜ `loadURL` するのか？

```ts
if (process.env.VITE_DEV_SERVER_URL) {
  // 開発中: サーバーのURL（http://localhost:5173）を開く
  mainWindow.loadURL(process.env.VITE_DEV_SERVER_URL);
} else {
  // 本番時: パッケージ内のHTMLファイルを直接読む
  mainWindow.loadFile(path.join(__dirname, "../dist/index.html"));
}
```

Electronは「Webサイトを表示できる専用ブラウザ」のようなものです。

- **開発時**：Reactの変更を即座に反映（HMR）させたいので、Viteが立てたローカルサーバー（`http://localhost:...`）を見に行きます。Chromeで開発中の画面を開くのと全く同じ状態です。
- **本番時**：サーバーは立っていないので、アプリ内に同梱された `html` ファイルを直接読み込みます。

#### 2. セキュリティ：なぜ隔離するのか？

```ts
    webPreferences: {
      nodeIntegration: false, // Node.jsの機能（fsなど）を無効化
      contextIsolation: true, // レンダラーとメインの世界を隔離
    },
```

初期のElectronは、画面上のJavaScriptから `require('fs').unlink(...)` のようにPC内のファイルを直接消すことが可能でした。これは便利ですが、もし外部サイトを表示したりXSS（クロスサイトスクリプティング）脆弱性があると、**PCが乗っ取られる**危険性があります。

そのため現在は、**「画面側（レンダラー）」と「OS側（メイン）」の間にガラスの壁（Context Isolation）を作る**のが鉄則です。
壁の向こう側（OS機能）へアクセスしたい時だけ、安全な「受付窓口（preload.ts）」を通して依頼するイメージです。

---

実際のコード全文は以下のようになります。

````ts:electron/main.ts


```ts:electron/main.ts
import { app, BrowserWindow } from 'electron'
import path from 'node:path'

let mainWindow: BrowserWindow | null = null

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 900,
    height: 700,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      nodeIntegration: false,
      contextIsolation: true,
    },
  })

  // vite-plugin-electron の推奨パターン：
  // vite serve の時は VITE_DEV_SERVER_URL が入るのでそれを読む
  if (process.env.VITE_DEV_SERVER_URL) {
    mainWindow.loadURL(process.env.VITE_DEV_SERVER_URL)
    mainWindow.webContents.openDevTools()
  } else {
    // 本番/ビルド時は dist/index.html を読む
    mainWindow.loadFile(path.join(__dirname, '../dist/index.html'))
  }
}

app.whenReady().then(createWindow)

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit()
})

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) createWindow()
})
````

補足：[Electron公式](https://electronjs.org/docs/latest/tutorial/context-isolation)も、リモートコンテンツを扱う場合は `nodeIntegration` を無効化し、`contextIsolation` を有効化することを推奨しています。

### electron/preload.ts（橋渡し役）

「とりあえず空でもOK」より、**最小の安全な公開例**を置いた方が次へ進みやすいです。  
Electronの `contextBridge` を使い、レンダラーに必要最小限のAPIだけ公開します。

```ts:electron/preload.ts
import { contextBridge } from 'electron'

contextBridge.exposeInMainWorld('myAPI', {
  ping: () => 'pong',
})
```

※ ここで公開した `myAPI` はレンダラー側（React）で `window.myAPI.ping()` のように呼べます。

### vite.config.ts（ViteにElectronを統合）

`vite-plugin-electron/simple` を使うと設定がかなりシンプルになります。

```ts:vite.config.ts
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import electron from 'vite-plugin-electron/simple'

export default defineConfig({
  plugins: [
    react(),
    electron({
      main: {
        entry: 'electron/main.ts',
      },
      preload: {
        input: 'electron/preload.ts',
      },
      // Optional: Renderer側でNode APIが欲しいときの入口（基本は空でOK）
      renderer: {},
    }),
  ],
})
```

## 5. package.json（ここがハマりどころ）

### 絶対に直すポイント：`type: "module"` は一旦やめる

`vite-plugin-electron` 側でも「現状 `type: "module"` はサポートされない」という注意があるため、初学者は一旦やめるのが安全です。

### mainエントリとscripts

`main` はビルド後のElectronメインを指す必要があります（デフォルトはCommonJSで `.js` が出ます）。

```json:package.json
{
  "name": "my-electron-app",
  "version": "0.0.0",
  "main": "dist-electron/main.js",
  "scripts": {
    "dev": "vite",
    "build": "vite build && electron-builder",
    "preview": "vite preview"
  }
}
```

これで `npm run dev` は Vite を起動し、プラグイン経由でElectronも起動します。

## 6. いざ起動！

```bash
npm run dev
```

Reactの画面が表示されたElectronウィンドウが立ち上がれば成功です。

## 技術の仕組み：なぜサーバー？

- Web開発（通常）: ブラウザが dev server（例: `localhost:5173`）にアクセスして表示
- Electron開発: Electronウィンドウ（Chromium内蔵）が dev server にアクセスして表示

つまり開発中は「Electronが内蔵ブラウザとしてViteサーバーを見に行ってる」だけです。

## 配布するなら（electron-builder）

electron-builder は `package.json` のトップレベル `build` キーで設定でき、そこに `appId` などを書けます。

例：

```json
{
  "build": {
    "appId": "com.example.myElectronApp"
  }
}
```

## さいごに

これで「Electron + React + Vite」の最強開発環境が、ちゃんと起動できる形で整いました。  
次は IPC（Renderer→Main）を増やしたり、ファイル操作・通知・トレイ常駐などElectronらしい機能に進むのがおすすめです。
