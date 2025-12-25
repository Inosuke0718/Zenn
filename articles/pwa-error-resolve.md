---
title: "【Next.js】本番だけPWAが動かない！？国際化(i18n)でmanifestが検出されない時の解決策"
emoji: "📱"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ["nextjs", "pwa", "manifest", "国際化", "i18n"]
published: true
---

## 【Next.js】本番だけPWAが動かない！？国際化(i18n)でmanifestが検出されない時の解決策

ローカル開発環境では完璧に動作していた PWA（Progressive Web App）。
「よし、これでリリースだ！」と Vercel や Cloudflare にデプロイした瞬間、スマホで確認しても**「ホーム画面に追加」が出ない...**。

そんな冷や汗をかく瞬間、ありませんか？

特に Next.js の App Router で `next-intl` などの国際化対応をしていると、この**「本番環境でのみ manifest が検出されない」**という厄介な問題に遭遇することがあります。

今回は、私が実際に遭遇したこの現象の原因と、確実に PWA を動作させるための解決策（ベストプラクティス）を共有します。

### 😱 なぜか本番環境だけ PWA にならない...

開発中のローカル環境（localhost）では、Chrome の DevTools で「Installability」がクリアされ、スマホでもインストールボタンが表示されていました。

しかし、本番環境にデプロイすると、Chrome DevTools の Application タブで以下のエラーが表示されてしまったのです。

```text
No manifest detected
```

#### 調査でわかった奇妙な挙動

原因を探るためにいくつか検証を行ったところ、不可解な挙動が見えてきました。

1.  **ファイル自体は存在する**:
    ブラウザで直接 `https://example.com/manifest.webmanifest` にアクセスすると、JSON データは正しく表示されます。
2.  **HTML にタグがない**:
    ページのソースコードを確認すると、本来あるはずの以下のタグが出力されていませんでした。
    ```html
    <!-- これが消えている... -->
    <link rel="manifest" href="/manifest.webmanifest" />
    ```

どうやら、Next.js の **Metadata API** と **国際化（i18n）の動的ルート** の組み合わせが悪さをしているようです。

### 🕵️ 原因：Metadata API と動的ルートの相性

通常、Next.js（App Router）では `app/manifest.ts` を配置することで動的にマニフェストを生成するのが一般的です 。また、`layout.tsx` の `metadata` オブジェクトで `manifest` プロパティを指定することもできます。[1]

しかし、以下のようなディレクトリ構成の場合、この仕組みが正常に動作しないケースがあります。

```text
src/
 └ app/
    └ [locale]/        # 👈 国際化ルート
       ├ layout.tsx    # ここでmetadataを設定しても...
       └ manifest.ts   # 動的生成がうまく紐付かない
```

`[locale]` という動的ルートの下では、Next.js がビルド時にマニフェストへのリンクタグを正しく HTML に注入できない場合があるようです。これは Vercel や Cloudflare OpenNext など、デプロイ環境に関わらず発生します。

### 🛠️ 解決策：原点回帰の「静的ファイル」作戦

結論から言うと、Next.js の「動的生成機能」に頼らず、**「静的ファイルを配置して、明示的に読み込む」**というクラシックな手法に切り替えることで解決します。

手順は以下の 3 ステップです。

#### 📄 1. 静的 manifest ファイルの作成

まず、動的な `src/app/manifest.ts` を削除し、代わりに `public` フォルダ直下に静的な JSON ファイルを作成します。拡張子は `.webmanifest` 推奨です。

```json:public/manifest.webmanifest
{
  "name": "NextWho - ツギダレ",
  "short_name": "NextWho",
  "description": "バドミントン、卓球、テニスなどのスポーツイベントでプレイヤーをコートに効率的に配置する無料ツール",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#ffffff",
  "theme_color": "#FFE566",
  "orientation": "portrait-primary",
  "icons": [
    {
      "src": "/icon-192.png",
      "sizes": "192x192",
      "type": "image/png",
      "purpose": "maskable"
    },
    {
      "src": "/icon-512.png",
      "sizes": "512x512",
      "type": "image/png",
      "purpose": "maskable"
    }
  ]
}
```

※ アイコン画像（`icon-192.png` 等）も忘れずに `public` フォルダに配置してください 。[2]

#### 🔗 2. layout.tsx に直書きする

次に、`src/app/[locale]/layout.tsx` の `<head>` タグ内に、マニフェストへのリンクを直接記述します。Next.js の `<Head>` コンポーネントではなく、HTML の `<head>` 内、または `metadata` 以外の場所で読み込ませるのがポイントです。

```tsx:src/app/[locale]/layout.tsx
export default async function LocaleLayout({
  children,
  params,
}: {
  children: React.ReactNode;
  params: Promise<{ locale: string }>;
}) {
  const { locale } = await params;

  return (
    <html lang={locale}>
      <head>
        {/* 👇 ここで明示的に読み込む！ */}
        <link rel="manifest" href="/manifest.webmanifest" />
      </head>
      <body>
        {/* 省略 */}
        {children}
      </body>
    </html>
  );
}
```

#### 🗑️ 3. metadata 設定のお掃除

最後に、`generateMetadata` や `metadata` オブジェクトに残っている `manifest` プロパティを削除します。これが残っていると競合する可能性があります。

```typescript:src/lib/metadata.ts
export function generateSiteMetadata({ locale }: { locale: string }): Metadata {
  return {
    title: 'NextWho',
    // manifest: '/manifest.webmanifest', // 👈 この行は削除する！
    category: 'sports',
  };
}
```

### ⚖️ なぜこの方法が良いのか？

Next.js の機能を使う場合と、今回の解決策を比較してみましょう。

| 特徴 | Next.js 標準 (manifest.ts) | 今回の解決策 (静的配置) |
| :--- | :--- | :--- |
| **実装の手軽さ** | TypeScript で書ける | JSON を手書き |
| **i18n 対応** | `[locale]` 下で不安定 | **どの構成でも確実** |
| **HTML 出力** | Next.js 任せ (失敗リスクあり) | **開発者が保証 (確実)** |
| **デプロイ環境** | 環境依存の可能性あり | どこでも動作する |

国際化ルーティングを行っている場合、**確実性**において静的ファイル配置に軍配が上がります。

### ✅ 動作確認をしよう

デプロイが完了したら、必ず本番環境で検証を行いましょう。

1.  **Chrome DevTools**:
    F12 キーを押し、「Application」タブ → 「Manifest」を選択します。エラーがなく、設定内容が表示されていれば成功です。
2.  **HTML ソース**:
    `view-source:https://your-domain.com/` を開き、`<link rel="manifest" ...>` が存在するか確認します。
3.  **実機確認**:
    スマホでアクセスし、「ホーム画面に追加」ができるか試してみましょう。

### まとめ

Next.js と国際化ライブラリの組み合わせは非常に強力ですが、PWA 周りで少しハマりポイントがあります。

- **`manifest.ts` がうまく動かない時は、静的ファイルに切り替える。**
- **`layout.tsx` に `<link rel="manifest">` を直書きする。**
- **Metadata API の `manifest` 設定は削除する。**

「本番で動かない！」と焦ったときは、Next.js の魔法（自動生成）を一度手放して、Web 標準のシンプルな記述に戻ってみてください。案外すんなりと解決することが多いですよ。

それでは、快適な PWA 開発ライフを！

[1](https://nextjsjp.org/docs/app/guides/progressive-web-apps)
[2](https://qiita.com/sh10n/items/678074d325f8a95a952e)