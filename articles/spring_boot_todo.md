---
title: "Spring Boot + LocalStorage で作る TODO アプリ完全ガイド"
emoji: "📝"
type: "tech"
topics: ["springboot", "javascript", "bootstrap", "localstorage", "java"]
published: true
---

# Spring Boot + LocalStorage で作る TODO アプリ完全ガイド

## 概要

この記事では、Spring Boot、Bootstrap、JavaScript を使用して、LocalStorage にデータを保存する TODO アプリケーションを作成する方法を詳しく解説します。

完成したコードは以下のリポジトリで確認できます：
https://github.com/Inosuke0718/todo_demo

初心者の方でも理解しやすいよう、実装手順を丁寧に説明していきます。

## 完成イメージ

以下が今回作成する TODO アプリの動作デモです：

![TODO アプリのデモ](https://storage.googleapis.com/zenn-user-upload/db7915ef309c-20250729.gif)

## 技術スタック

- **バックエンド**: Spring Boot 3.5.4
- **フロントエンド**: Bootstrap 5、JavaScript (Vanilla)
- **データ保存**: LocalStorage （一番手っ取り早く作成できる LocalStorage を採用）
- **ビルドツール**: Maven
- **Java バージョン**: 17

## 事前準備

まだ Spring Boot の環境構築ができていない方は、こちらの記事を参考に簡単に構築できます！

**📚 環境構築ガイド**: [VSCode で SpringBoot 使う環境構築](https://qiita.com/inokazum/items/0031523bb817a885d7d5)

上記の記事では、VSCode を使用した Spring Boot 開発環境の構築方法を詳しく解説しています。

## ディレクトリ構造と作成するファイル

### 1. バックエンド構造

```
src/main/java/todo_demo/example/todo_demo/
├── TodoDemoApplication.java (既存)
├── controller/
│   └── TodoController.java (新規作成)
├── model/
│   └── Todo.java (新規作成)
└── dto/
    └── TodoDto.java (新規作成)
```

### 2. フロントエンド構造

```
src/main/resources/
├── static/
│   ├── css/
│   │   └── style.css (新規作成)
│   └── js/
│       └── todo.js (新規作成)
└── templates/
    └── index.html (新規作成)
```

## 実装詳細

### 1. pom.xml の更新

追加する依存関係：

```xml
<\!-- Thymeleaf テンプレートエンジン -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-thymeleaf</artifactId>
</dependency>
```

### 2. バックエンドコンポーネント

#### a) TodoController.java

- **パス**: `src/main/java/todo_demo/example/todo_demo/controller/TodoController.java`
- **役割**: HTTP リクエストを処理し、HTML ページを返す
- **エンドポイント**:
  - `GET /` - TODO アプリのメインページを表示
  - `GET /api/todos` - すべての TODO を JSON 形式で返す（オプション）

#### b) Todo.java

- **パス**: `src/main/java/todo_demo/example/todo_demo/model/Todo.java`
- **役割**: TODO アイテムのデータモデル
- **フィールド**:
  - `id` (Long): 一意の識別子
  - `title` (String): TODO のタイトル
  - `completed` (boolean): 完了状態
  - `createdDate` (LocalDateTime): 作成日時

#### c) TodoDto.java

- **パス**: `src/main/java/todo_demo/example/todo_demo/dto/TodoDto.java`
- **役割**: データ転送オブジェクト（フロントエンドとの通信用）

### 3. フロントエンドコンポーネント

#### a) index.html

- **パス**: `src/main/resources/templates/index.html`
- **内容**:
  - Bootstrap 5 を使用したレスポンシブデザイン
  - TODO リスト表示エリア
  - 新規 TODO 追加フォーム
  - 各 TODO アイテムに編集・削除・完了チェックボタン

#### b) todo.js

- **パス**: `src/main/resources/static/js/todo.js`
- **機能**:
  - LocalStorage から TODO データの読み込み・保存
  - TODO 追加機能
  - TODO 編集機能
  - TODO 削除機能
  - TODO 完了状態の切り替え
  - リストの動的な更新

#### c) style.css

- **パス**: `src/main/resources/static/css/style.css`
- **内容**:
  - カスタムスタイル
  - モバイルファーストのレスポンシブデザイン
  - 完了した TODO のスタイリング

### 4. LocalStorage データ構造

```javascript
{
  "todos": [
    {
      "id": "1234567890",
      "title": "買い物に行く",
      "completed": false,
      "createdDate": "2024-01-20T10:00:00"
    }
  ]
}
```

## 実装手順

実際のコード実装については、[GitHub リポジトリ](https://github.com/Inosuke0718/todo_demo)で詳細なコードを確認できます。

1. **pom.xml を更新** - Thymeleaf 依存関係を追加
2. **モデルクラスを作成** - Todo.java、TodoDto.java
3. **コントローラーを作成** - TodoController.java
4. **HTML テンプレートを作成** - index.html (Bootstrap 使用)
5. **JavaScript ファイルを作成** - todo.js (LocalStorage 処理)
6. **CSS ファイルを作成** - style.css (レスポンシブデザイン)
7. **アプリケーションをテスト** - mvn spring-boot:run で実行

## 初心者向け説明

### Spring Boot の基本構造

- **Controller**: Web ブラウザからのリクエストを受け取る窓口
- **Model**: データの構造を定義
- **Templates**: HTML ページのテンプレート
- **Static**: CSS、JavaScript、画像などの静的ファイル

### そもそもSpring Bootとは？

このYoutube解説が分かりやすいかと思います。こちらをご覧ください。
https://www.youtube.com/watch?v=8UERVg5c_HM

### 実行方法

1. リポジトリをクローン：

```bash
git clone https://github.com/Inosuke0718/todo_demo.git
cd todo_demo
```

2. アプリケーションを実行：

```bash
./mvnw spring-boot:run
```

3. ブラウザで `http://localhost:8080` にアクセス

## 次のステップ

### 🚀 アプリをインターネットに公開しよう！

作成した TODO アプリをインターネット上に公開して、どこからでもアクセスできるようにしませんか？

次の記事では、この TODO アプリを **Render.com** を使って **完全無料** でデプロイする方法を詳しく解説しています：

:::message
**🚀 続編記事**: [【無料】Spring Boot TODO アプリを Render.com にデプロイする完全ガイド](https://zenn.dev/your-username/articles/spring-boot-render-deploy)

- Docker を使ったコンテナ化
- 無料でのクラウドデプロイ
- 本番環境用の設定
- ヘルスチェック機能の実装

すべて無料で、5-10 分程度でデプロイ完了します！
:::

### その他の拡張アイデア

- データベース（H2、MySQL など）を使用したバージョンへの拡張
- REST API の実装
- ユーザー認証機能の追加

## 関連記事

https://zenn.dev/your-username/articles/spring-boot-render-deploy
