---
title: "next.js学習"
emoji: "😘" # アイキャッチとして使われる絵文字（1文字だけ）
type: "tech" # tech: 技術記事 / idea: アイデア記事
topics: ["NextAuth.js", "Next.js"] # タグ。["markdown", "rust", "aws"]のように指定する
published: false # 公開設定（falseにすると下書き）
---

## passwordのハッシュ化
```
function hashPassword(password: string) {
    const saltRounds = 10; // ソルトの長さ
    return bcrypt.hash(password, 10);
}
```

## Expressパッケージ
サーバーフレームワークの一つでにカスタムサーバーを構築できる
サーバーサイドレンダリング（SSR）、静的サイト生成（SSG）、APIルートなどを提供する

## Payloadとは
サーバーサイドでのデータ処理やAPIエンドポイント、クライアントサイドでのデータフェッチ時に送受信されるデータのこと
つまるところPayload とは受け渡しをするデータのこと

## Payload CMS
コンテンツ管理システム

## Next.jsのハンドラ
Next.jsでHTTPリクエストを処理する為のメソッドをさす

## cross-env
cross-env は、Node.js のプロジェクトで環境変数を設定するためのツールです。特に、異なるオペレーティングシステム間で環境変数を一貫して設定する際に有用です。

## Nodemon
Node.jsの開発を支援するツールです。Node.jsで書かれたアプリケーションを監視し、ファイルが変更されると自動的にアプリケーションを再起動
### $ npm add -D nodemon
Nodemonを現在のNode.jsプロジェクトの開発依存関係として追加する

## tRCP
TypeScriptとReactを使用したフルスタックの開発を簡素化するためのツール
直接サーバサイドの関数をフロントエンドから呼び出すことができます
強力なバックエンド統合: tRPCは、Node.jsベースのサーバーや、さまざまなデータベースとの連携が容易です
### install command
```
npm add @trpc/client @trpc/next @trpc/react-query @trpc/server @tanstack/react-query
```