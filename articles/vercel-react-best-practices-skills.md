---
title: "Vercel公式「React Best Practices」をAIにインストールして、最強のコードレビュー環境を作る"
emoji: "🤖"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ["react", "vercel", "ai", "cursor", "claude"]
published: true
---

# はじめに

先日、Vercelが **「React Best Practices」** というリポジトリを公開しました。

これは単なる読み物ではなく、**AIエージェント（Claude CodeやCursorなど）にインストールして、自動コードレビューの基準として使える** という画期的な仕組み「Skills」の一部として提供されています。

この記事では、この「Skills」の概要と、実際にVercelが提唱する「Reactのベストプラクティス」を使って、自分のコードをAIにレビューしてもらう方法を解説します。

# 1. Skills（Agent Skills）とは？

**Skills** は、Vercelが提供する「AIエージェント向けの拡張機能パッケージ」です。

これまでAIに指示を出すときは、「あなたはシニアエンジニアです。パフォーマンスを考慮して…」といったプロンプトを毎回書く必要がありました。しかし、Skillsを使うと、特定の専門知識や振る舞い（ペルソナ）をコマンド一つでAIにインストールできます。

- **公式リポジトリ**: [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills)
- **何ができるか**: チームやコミュニティで培われた「暗黙の知見」を、AIが参照可能なルールセットとして固定できます。

# 2. Vercel公式「React Best Practices」の中身

今回注目する **React Best Practices** は、Vercelが10年以上にわたるReact/Next.jsの運用で培った最適化のノウハウをまとめたものです。

- **公式ドキュメント**: [React Best Practices (GitHub)](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices)
- **ブログ解説**: [Introducing: React Best Practices](https://vercel.com/blog/introducing-react-best-practices)

この中には40以上のルールが含まれていますが、特に「修正した時のインパクトが大きい順（CRITICAL 〜 LOW）」に優先順位が付けられています。これにより、AIは些末な指摘よりも、**パフォーマンスに直結する重要な修正** を優先して提案できるようになっています。

# 3. インストールと使い方

使い方は非常にシンプルです。npxコマンドで導入できるため、コマンド一つで導入できます。

## インストール方法

ターミナルで以下のコマンドを実行します（※ `add-skill` コマンドは `skills` に移行中のため、最新の推奨コマンドを使用します）。

```bash
npx add-skill vercel-labs/agent-skills
```

## AIへの頼み方（プロンプト例）

インストール後、AIエージェント（Claude CodeやCursorのComposer機能など）に対して以下のように指示します。

> 「このコンポーネントを react-best-practices の基準でレビューしてください。特にパフォーマンスに悪影響がある箇所を指摘し、修正案を出してください。」

# 4. 初学者がまずチェックすべき2つの重要ルール

Vercelのベストプラクティスの中でも、特に初心者がやりがちで、かつ修正効果が高い2つのポイントを紹介します。AIにレビューを頼む際は、まずここを重点的に見てもらいましょう。

## ① awaitの直列化（Async Waterfall）を潰す

非同期処理を無意識に `await` で連鎖させてしまうと、待ち時間が積み重なって表示が遅くなります。

**悪い例（直列処理）:**

```javascript
// Aが終わるまでBが始まらない
const user = await fetchUser();
const posts = await fetchPosts();
```

**良い例（並列処理）:**

```javascript
// 依存関係がないなら同時に投げる（Promise.all）
const [user, posts] = await Promise.all([fetchUser(), fetchPosts()]);
```

この「依存関係がないなら並列化する」という判断は、AIが得意とするレビュー領域です。

## ② Barrel File（バレルファイル）を避ける

`index.ts` などで複数のモジュールをまとめて export する「Barrel File」は便利ですが、バンドルサイズが肥大化し、ビルドやロードが遅くなる原因になります。

**悪い例:**

```javascript
// @/components/index.ts からすべて読み込むと、使わないコンポーネントも巻き込まれる可能性がある
import { Button } from "@/components";
```

**良い例:**

```javascript
// 直接ファイルを指定して読み込む
import { Button } from "@/components/Button";
```

Vercelはこのルールを **「CRITICAL（最重要）」** レベルに設定しています。AIに「バレルファイル経由のimportがないかチェックして」と頼むだけで、アプリの軽量化につながります。

# まとめ：AIを「専属レビュアー」にしよう

これまで、こうしたパフォーマンスの指摘は経験豊富なシニアエンジニアが行うものでした。しかし、Vercelの **React Best Practices** を導入することで、AIがその役割の一部を自動で担ってくれるようになります。

まずは自分の書いたコードを、AIに「Vercel流」でレビューさせてみてください。きっと、昨日の自分よりも少しだけ速くて強いコードが書けるようになるはずです。

## 参考リンク

- [vercel-labs/agent-skills (GitHub)](https://github.com/vercel-labs/agent-skills)
- [Introducing: React Best Practices (Vercel Blog)](https://vercel.com/blog/introducing-react-best-practices)
