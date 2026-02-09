---
title: "Tailwind CSSがなぜ人気なのか＆Node.jsなしで今すぐ始める方法"
emoji: "🌊"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ["tailwindcss", "css", "frontend", "beginner"]
published: true
---

# はじめに

近年、フロントエンド開発のデファクトスタンダードになりつつある **Tailwind CSS** 。
「クラス名が長くなるだけでしょ？」「Bootstrapでよくない？」と思っている方に向けて、なぜこれほど人気なのか、その理由と具体的な使い方をサクッと解説します。

## 1. Tailwind CSSってなんで人気なの？

結論から言うと、 **「CSS設計の悩みから解放されるから」** です。
主な人気の理由は以下の3点です。

- **クラス名を考えなくていい（命名不要）**
  従来のCSSでは `.card-wrapper-inner` のようなクラス名をひねり出す必要がありましたが、Tailwindでは `flex p-4 bg-white` と書くだけ。命名のストレスがゼロになります。
- **デザインの微調整が爆速（ユーティリティファースト）**
  HTMLとCSSを行き来せず、HTMLファイルだけでスタイリングが完結します。修正もその場で行えるため、開発スピードが格段に上がります。
- **安全なファイルサイズ（PurgeCSS）**
  ビルド時に「使っていないクラス」を自動で削除してくれるため、最終的なCSSファイルサイズが非常に小さく、パフォーマンスに優れています（CDN版を除く）。

## 2. Bootstrapとの違いは？

よく比較されるBootstrapとの最大の違いは、 **「完成品」か「部品」か** です。

| 特徴             | Bootstrap                                              | Tailwind CSS                                                       |
| :--------------- | :----------------------------------------------------- | :----------------------------------------------------------------- |
| **アプローチ**   | **コンポーネント指向**<br>（完成されたUIパーツを使う） | **ユーティリティ指向**<br>（小さな機能単位のクラスを組み合わせる） |
| **イメージ**     | 「レトルトカレー」<br>誰が作っても同じ味で美味しい。   | 「スパイスセット」<br>配合次第で自分好みの味を自由に作れる。       |
| **デザイン**     | 「Bootstrapっぽい」見た目になりがち。                  | 完全にオリジナルのデザインが作れる。                               |
| **カスタマイズ** | 既存のスタイルを打ち消すのが大変。                     | 最初から白紙なので上書きの苦労がない。                             |

**Bootstrap** は、`btn-primary` と書けば綺麗な青いボタンがすぐ出ます。管理画面やプロトタイプなど、デザインにこだわらない場合は最強です。
**Tailwind CSS** は、`bg-blue-500 text-white rounded px-4 py-2` と書いてボタンを作ります。手間は少し増えますが、自由度は無限大です。

## 3. わかりやすい例：p-1 と p-10 の違い

Tailwindの数値は、基本的に **「1単位 = 0.25rem (4px)」** のルールで統一されています（デフォルト設定の場合）。

この「4の倍数」のリズム（4px, 8px, 12px...）で作ると、デザイン全体に統一感が生まれるように設計されています。

- **`p-1`**
  - 計算：`1 × 4px = 4px`
  - 意味：`padding: 0.25rem;`
  - 用途：ほんの少し隙間を開けたいとき。

- **`p-10`**
  - 計算：`10 × 4px = 40px`
  - 意味：`padding: 2.5rem;`
  - 用途：セクションの区切りなど、ガッツリ余白を取りたいとき。

**直感的な比較:**

```html
<!-- p-1 (4px): 文字と枠がキツキツ -->
<div class="p-1 border bg-gray-100">狭い余白</div>

<!-- p-10 (40px): ゆったりとしたスペース -->
<div class="p-10 border bg-gray-100">広い余白</div>
```

![Tailwind CSS の余白比較（p-1 vs p-10）](https://github.com/Inosuke0718/Zenn/blob/main/images/tailwind-padding.png?raw=true)


## 4. Node.jsなくても使えるよ（Play CDN）

「npm install とか設定ファイルとか面倒くさい！」という方へ。
実はHTMLファイルに `<script>` タグを1行足すだけで、今すぐブラウザ上でTailwindを使えます。これを **Play CDN** と呼びます。

### 使い方

以下のコードをHTMLファイルとして保存し、ブラウザで開くだけです。

```html
<!doctype html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <!-- これを入れるだけでOK -->
    <script src="https://cdn.tailwindcss.com"></script>
  </head>
  <body>
    <div class="h-screen flex items-center justify-center bg-gray-100">
      <h1 class="text-3xl font-bold text-blue-600 underline">Hello world!</h1>
    </div>
  </body>
</html>
```

**注意点:**
このCDN版はブラウザで毎回CSSを計算するため、動作が少し重くなります。本番公開用（プロダクション）には非推奨ですが、学習やちょっとしたプロトタイプ作成には最適です。

まずはこのPlay CDNを使って、`p-1` と `p-10` を書き換えて変化を楽しんでみてください！

### 参考

- [Play CDN 公式ドキュメント](https://tailwindcss.com/docs/installation/play-cdn)
