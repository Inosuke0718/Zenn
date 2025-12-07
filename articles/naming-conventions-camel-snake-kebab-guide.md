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

## 3大ケースの基本をおさらい

まずは基本の「形」と「主な生息地」を整理します。

### 🐪 キャメルケース (Camel Case)

単語の先頭を大文字にして繋げる記法です。ラクダのコブのように見えることからこう呼ばれます。

実は2種類あります。

**ローワーキャメル (Lower Camel Case)**

先頭は小文字、続く単語の先頭は大文字。

- 例: `userProfile`, `createdAt`, `getElementById`
- 主な用途: JavaScript, Java, Goなどの変数名・関数名。

**アッパーキャメル (Upper Camel Case) / パスカルケース (Pascal Case)**

先頭も大文字。

- 例: `UserProfile`, `ReactComponent`, `CustomerService`
- 主な用途: クラス名、型定義、Reactコンポーネント名。

### 🐍 スネークケース (Snake Case)

単語をアンダースコア（`_`）で繋ぐ記法です。地面を這うヘビに見えるためです。

**基本のスネーク**: すべて小文字。

- 例: `user_profile`, `created_at`, `get_element`
- 主な用途: Python全般、SQLの列名、Rustの変数名。

**スクリーミングスネーク (Screaming Snake)**: すべて大文字。

- 例: `MAX_COUNT`, `API_KEY`
- 主な用途: 多くの言語での「定数（Constant）」や環境変数。

### 🍢 ケバブケース (Kebab Case)

単語をハイフン（`-`）で繋ぐ記法です。串刺しのケバブに見えるためです。一部ではチェインケースとも呼ばれます。

- 例: `user-profile`, `font-size`, `main-content`
- 主な用途: URL、HTMLのクラス名・ID、CSSプロパティ、npmパッケージ名。

**注意**: 多くのプログラミング言語ではハイフンが「マイナス（引き算）」と解釈されるため、変数名には使えません。

## 言語・用途別 採用マトリックス

「どの言語で、どのケースを使うべきか」を一目でわかる表にしました。

これさえ覚えておけば、大抵の現場で通用します。

| 言語 / 技術 | 変数・関数 | クラス・型 | 定数 | ファイル名 |
|------------|-----------|-----------|------|-----------|
| JavaScript / TypeScript | 🐪 lowerCamel | 🐫 Pascal | 🗣 SCREAMING | 🍢 kebab (推奨)<br>🐫 Pascal (React) |
| Python | 🐍 snake | 🐫 Pascal | 🗣 SCREAMING | 🐍 snake |
| Java / C# | 🐪 lowerCamel | 🐫 Pascal | 🗣 SCREAMING | 🐫 Pascal |
| Go | 🐪 lowerCamel | 🐫 Pascal | 🐫 Pascal (※1) | 🐍 snake |
| Ruby | 🐍 snake | 🐫 Pascal | 🗣 SCREAMING | 🐍 snake |
| Rust | 🐍 snake | 🐫 Pascal | 🗣 SCREAMING | 🐍 snake |
| PHP | 🐪 lowerCamel<br>🐍 snake (※2) | 🐫 Pascal | 🗣 SCREAMING | 🐫 Pascal (PSR-4) |
| SQL (DBカラム) | 🐍 snake | - | - | - |
| HTML / CSS | 🍢 kebab (class/id) | - | - | 🍢 kebab |
| URL / APIパス | 🍢 kebab | - | - | 🍢 kebab |

**(※1)** Go言語では、先頭が大文字ならPublic（外部公開）、小文字ならPrivateという厳格なルールがあるため、定数でもキャメル/パスカルを使います。

**(※2)** PHPはフレームワーク（Laravel等）やWordPressなどの文化圏によって流儀が分かれますが、最近はPSR準拠でキャメルが優勢です。

## なぜ使い分ける必要があるのか？

### 1. 「Webの標準」と「プログラムの都合」の衝突

Web（HTML/CSS/URL）は、大文字小文字を区別しない（Case Insensitive）歴史が長いため、可読性のために区切り文字が必要でした。そこで選ばれたのがハイフン（`-`）です。

一方でプログラミング言語（JS, Python等）では、ハイフンは演算子の「マイナス」です。

`user-id` と書くと、「user 引く id」という計算式になってしまいます。

だからプログラムの中ではキャメルやスネークが使われるのです。

### 2. Next.js (React) ユーザーへの特記事項

JavaScriptの世界では、ファイル名とコード内で規則が混在しがちです。

特にNext.jsでは以下の使い分けがベストプラクティスです。

- **コンポーネント (コード内)**: `UserProfile.tsx` (パスカルケース)
- **関数・変数 (コード内)**: `getUserProfile()` (ローワーキャメル)
- **画像・アセット (publicフォルダ)**: `user-profile.png` (ケバブケース)
- **URLになるルーティング**: `app/user-profile/page.tsx` (ケバブケース)

「URLやファイルシステムに関わる部分はケバブ、JavaScriptとして動く部分はキャメル/パスカル」と覚えておくとスッキリします。

## まとめ

- **JS/TS/Java/Go** を書くなら基本は **キャメルケース** 🐪
- **Python/Ruby/SQL/Rust** を書くなら基本は **スネークケース** 🐍
- **HTML/CSS/URL/画像ファイル** は **ケバブケース** 🍢
- **クラス名・Reactコンポーネント** は偉そうに **パスカルケース** 🐫

「郷に入っては郷に従え」で、言語やフレームワーク推奨のスタイルに合わせることが、可読性の高いコードへの第一歩です。

迷ったら公式ドキュメントや有名なOSSのコードを覗いてみましょう！
