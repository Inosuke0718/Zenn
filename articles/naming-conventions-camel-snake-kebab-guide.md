---
title: "【命名規則】キャメル・スネーク・ケバブ... 結局どれをいつ使う？言語別ベストプラクティスまとめ"
emoji: "🐪"
type: "tech"
topics: ["プログラミング", "命名規則", "初心者", "ベストプラクティス"]
published: true
---

プログラミングをしていると、「ここって `userId` ？ `user_id` ？ それとも `user-id` ？」と迷う瞬間、ありませんか？

プロジェクトや言語によって「正解」が変わるのが命名規則の厄介なところです。

今回は、主要な命名規則（キャメル、スネーク、ケバブ）の特徴と、どの言語で何が採用されているかの決定版まとめを作成しました。

## 3 大ケースの基本をおさらい

まずは基本の「形」と「主な生息地」を整理します。

### 🐪 キャメルケース (Camel Case)

単語の先頭を大文字にして繋げる記法です。ラクダのコブのように見えることからこう呼ばれます。

実は 2 種類あります。

**ローワーキャメル (Lower Camel Case)**

先頭は小文字、続く単語の先頭は大文字。

- 例: `userProfile`, `createdAt`, `getElementById`
- 主な用途: JavaScript, Java, Go などの変数名・関数名。

**アッパーキャメル (Upper Camel Case) / パスカルケース (Pascal Case)**

先頭も大文字。

- 例: `UserProfile`, `ReactComponent`, `CustomerService`
- 主な用途: クラス名、型定義、React コンポーネント名。

### 🐍 スネークケース (Snake Case)

単語をアンダースコア（`_`）で繋ぐ記法です。地面を這うヘビに見えるためです。

**基本のスネーク**: すべて小文字。

- 例: `user_profile`, `created_at`, `get_element`
- 主な用途: Python 全般、SQL の列名、Rust の変数名。

**スクリーミングスネーク (Screaming Snake)**: すべて大文字。

- 例: `MAX_COUNT`, `API_KEY`
- 主な用途: 多くの言語での「定数（Constant）」や環境変数。

### 🍢 ケバブケース (Kebab Case)

単語をハイフン（`-`）で繋ぐ記法です。串刺しのケバブに見えるためです。一部ではチェインケースとも呼ばれます。

- 例: `user-profile`, `font-size`, `main-content`
- 主な用途: URL、HTML のクラス名・ID、CSS プロパティ、npm パッケージ名。

**注意**: 多くのプログラミング言語ではハイフンが「マイナス（引き算）」と解釈されるため、変数名には使えません。

## 言語・用途別 採用マトリックス

「どの言語で、どのケースを使うべきか」を一目でわかる表にしました。

これさえ覚えておけば、大抵の現場で通用します。

| 言語 / 技術             | 変数・関数                     | クラス・型 | 定数           | ファイル名                           |
| ----------------------- | ------------------------------ | ---------- | -------------- | ------------------------------------ |
| JavaScript / TypeScript | 🐪 lowerCamel                  | 🐫 Pascal  | 🗣 SCREAMING    | 🍢 kebab (推奨)<br>🐫 Pascal (React) |
| Python                  | 🐍 snake                       | 🐫 Pascal  | 🗣 SCREAMING    | 🐍 snake                             |
| Java                    | 🐪 lowerCamel                  | 🐫 Pascal  | 🗣 SCREAMING    | 🐫 Pascal                            |
| C#                      | � Pascal (※3)                  | 🐫 Pascal  | 🗣 SCREAMING    | 🐫 Pascal                            |
| Go                      | 🐪 lowerCamel                  | 🐫 Pascal  | 🐫 Pascal (※1) | 🐍 snake                             |
| Ruby                    | 🐍 snake                       | 🐫 Pascal  | 🗣 SCREAMING    | 🐍 snake                             |
| Rust                    | 🐍 snake                       | 🐫 Pascal  | 🗣 SCREAMING    | 🐍 snake                             |
| PHP                     | 🐪 lowerCamel<br>🐍 snake (※2) | 🐫 Pascal  | 🗣 SCREAMING    | 🐫 Pascal (PSR-4)                    |
| SQL (DB カラム)         | 🐍 snake                       | -          | -              | -                                    |
| HTML / CSS              | 🍢 kebab (class/id)            | -          | -              | 🍢 kebab                             |
| URL / API パス          | 🍢 kebab                       | -          | -              | 🍢 kebab                             |

**(※1)** Go 言語では、先頭が大文字なら Public（外部公開）、小文字なら Private という厳格なルールがあるため、定数でもキャメル/パスカルを使います。

**(※2)** PHP はフレームワーク（Laravel 等）や WordPress などの文化圏によって流儀が分かれますが、最近は PSR 準拠でキャメルが優勢です。

**(※3)** Java と異なり、C#は関数と public な変数は PascalCase です。lowerCamel はローカル変数、private フィールドなどに使われます。

## なぜ使い分ける必要があるのか？

### 1. 「Web の標準」と「プログラムの都合」の衝突

Web（HTML/CSS/URL）は、大文字小文字を区別しない（Case Insensitive）歴史が長いため、可読性のために区切り文字が必要でした。そこで選ばれたのがハイフン（`-`）です。

一方でプログラミング言語（JS, Python 等）では、ハイフンは演算子の「マイナス」です。

`user-id` と書くと、「user 引く id」という計算式になってしまいます。

だからプログラムの中ではキャメルやスネークが使われるのです。

### 2. Next.js (React) ユーザーへの特記事項

JavaScript の世界では、ファイル名とコード内で規則が混在しがちです。

特に Next.js では以下の使い分けがベストプラクティスです。

- **コンポーネント (コード内)**: `UserProfile.tsx` (パスカルケース)
- **関数・変数 (コード内)**: `getUserProfile()` (ローワーキャメル)
- **画像・アセット (public フォルダ)**: `user-profile.png` (ケバブケース)
- **URL になるルーティング**: `app/user-profile/page.tsx` (ケバブケース)

「URL やファイルシステムに関わる部分はケバブ、JavaScript として動く部分はキャメル/パスカル」と覚えておくとスッキリします。

## まとめ

- **JS/TS/Java/Go** を書くなら基本は **キャメルケース** 🐪
- **Python/Ruby/SQL/Rust** を書くなら基本は **スネークケース** 🐍
- **HTML/CSS/URL/画像ファイル** は **ケバブケース** 🍢
- **クラス名・React コンポーネント** は偉そうに **パスカルケース** 🐫

「郷に入っては郷に従え」で、言語やフレームワーク推奨のスタイルに合わせることが、可読性の高いコードへの第一歩です。

迷ったら公式ドキュメントや有名な OSS のコードを覗いてみましょう！
