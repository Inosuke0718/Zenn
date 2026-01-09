---
title: "Antigravityで迷う「Skills？Rules？Workflow？GEMINI.md？」使い分けガイド（初学者向け）"
emoji: "🗺️"
type: "tech"
topics: ["antigravity", "gemini", "ai", "workflow", "guide"]
published: true
---

# Antigravity で迷う「Skills？Rules？Workflow？GEMINI.md？」使い分けガイド

AI エディタの Antigravity を触り始めると、**Rules** や **Skills**、さらに **Workflow** や `GEMINI.md` といった“AI に指示する仕組み”がいくつも出てきて、「結局どこに何を書けばいいの？」と迷う瞬間、ありませんか？ 🤔

結論から言うと、これらは役割が明確に違います。（似て見えても、AI への「効かせ方」が違うのです）

この記事では、Java（JSP/Servlet）や Python を学ぶ皆さんが直面するリアルな開発シーンを例に、**初学者が迷わない使い分け**を表と具体例でまとめます。

---

## 🏁 まず結論：一言でいうと何？

- `GEMINI.md`：プロジェクトの「憲法」（絶対守る基本方針）
- Rules：日常運用の「ガードレール」（常時、または条件付きで適用されるルール）
- Skills：タスク別の「専門家マニュアル」（必要なときにだけ読む“手順書”）
- Workflow：作業の「進行表」（人間やエージェントが順序通りに進めるためのフロー）

ポイントは、**Rules/GEMINI.md は“どう振る舞うべきか（お作法）”**、**Skills/Workflow は“どうやって達成するか（手順）”** の比重が高いことです。

---

## 📊 使い分け早見表（これだけ見れば OK）

Java や Python の開発現場に置き換えると、以下のようなイメージです。

| 名前        | 役割（何を書く？）            | いつ効く？                               | 保存場所（ここが正解！）                                                                  | 向いてる例（Java/Python）                                              |
| --------- | -------------------- | ----------------------------------- | ----------------------------------------------------------------------------- | --------------------------------------------------------------- |
| GEMINI.md | 最上位方針（憲法：言語ver・禁止事項） | チャット開始時にまず読まれる                      | ルート直下./GEMINI.md<small>※人間も AI も一番最初に見る場所</small>                             | 「Java 17 / Python 3.11 を使用」「日本語で回答」「初学者向けに優しく解説」                |
| Rules     | 開発ルール（命名規則、MVC、型定義）  | Always On / Model Decision（常時〜条件付き） | .agent フォルダ.agent/rules/*.md<small>※Antigravity が自動で読み込む標準の場所</small>       | 「クラス名は PascalCase」「JSP に Java ロジックを書かない」「Python は Type Hint 必須」 |
| Skills    | タスク別の専門手順（役割・テンプレート） | 依頼内容に応じて自動ピックされる想定                  | .skills フォルダ.skills/*.md<small>※隠しフォルダにしてルートを汚さないのが通例</small>               | 「Servlet クラス作成手順」「DAO パターン実装手順」「スクレイピングコード生成手順」                 |
| Workflow  | 手順の流れ（手順 1→2→3、入出力）  | 実行するときだけ参照（都度）                      | .agent フォルダ.agent/workflows/*.md<small>※ここに入れないと「ワークフロー機能」として認識されない</small> | 「Tomcat デプロイ手順」「requirements.txt 更新フロー」「DB 接続テスト手順」             |

> Gemini はまず`GEMINI.md`（憲法）を読み、依頼に応じて`skills/`から「今回は Servlet 作成スキルを使おう」と道具を選ぶ、というイメージです 🛠️

---

## 🚦 Rules の「Model Decision」って何？ Skills と同じ？

ここが一番の悩みどころです。「モデルが必要だと思ったら適用する」という点で似ているからです。
ですが、**目的**で分けると運用が楽になります。

- **Model Decision な Rules**：
  「うっかり破るとバグや減点対象になるルール」を、AI が空気を読んで守ってくれる機能。
- **Skills**：
  「特定の機能を作るときのレシピ」を、必要なときだけ呼び出して再現性を高める機能。

### 迷ったときの判断基準

- **「クラス名の付け方」や「インデント」など、全体で守るべき規約**
  👉 **Rules**（または`GEMINI.md`）へ
- **「ログイン画面を作る」「CSV を読み込む」など、特定の作業手順**
  👉 **Skills**（＋ Workflow）へ

---

## 🐍 具体例：MVC モデルやインデント規約はどこ？

たとえば、JSP/Servlet や Python 開発でよくある以下のルールは、プロジェクト全体に関わるので **Rules** が向いています。

### Rules に書くべきこと（常時守ってほしい）
- **Java/JSP**:
  - JSP ファイルには `<% Javaコード %>` を書かず、EL 式と JSTL を使う（MVC の分離）。
  - クラス名は必ずアッパーキャメルケース（`StudentData`）、変数名はローワーキャメルケース（`studentName`）。
  - `System.out.println` は使わず、ロガーを使用する。
- **Python**:
  - インデントはスペース 4 つ。
  - 関数には必ず型ヒント（Type Hinting）をつける（例: `def add(a: int, b: int) -> int:`）。

### Skills/Workflow に書くべきこと（作業フロー化）
一方で、「新しい機能を実装する」ような一連の流れは Skills に寄せるとメリットが出ます。

- **Skills 側（例：新規 Servlet 追加スキル）**:
  1. `HttpServlet` を継承したクラスを作成する。
  2. `@WebServlet` アノテーションで URL パターンを指定する。
  3. `doGet` / `doPost` メソッドをオーバーライドする。
  4. 転送先の JSP ファイルが存在するかチェックする。

---

## 🔰 初学者向け：おすすめの最小構成

最初から全部使いこなそうとするとパンクします。まずは次の 2 つだけで十分です！

1. **`GEMINI.md`**：プロジェクトの大前提（5〜10 行くらい）
2. **Rules**：「これだけは守れ」と言われる鉄の掟

慣れてきて、「毎回同じようなコード修正をお願いしてるな…」と感じたら、その作業を Skills へ移しましょう。

---

## 📝 そのまま使えるテンプレ

### GEMINI.md（最小構成）

```md
# Project Constitution (GEMINI.md)

- Language: Japanese (出力は日本語で行うこと)
- Tech Stack: Java 17, Servlet 6.0, JSP, Python 3.11
- Tone: Helpful and educational for beginners.
- Priority: Code readability and best practices (PEP8 / Java Naming Conventions).
```

### Skills ファイル（例：Java の DAO 作成）

```md
# create-dao-skill

## When to use

- When the user asks to create a Data Access Object (DAO) for database operations.

## Checklist

- Use `try-with-resources` to ensure `Connection`, `PreparedStatement`, and `ResultSet` are closed.
- Do not hardcode SQL values; use `?` placeholder.
- Throw distinct exceptions or handle them gracefully; don't just print stack trace.
- Follow the Singleton pattern or Dependency Injection if applicable.
```

このように「**気をつけるポイント（チェックリスト）**」を書いておくだけで、AI が生成するコードの品質（特に DB 周りの安全性）がグッと上がります ✨

---

## まとめ

- **`GEMINI.md`** は「プロジェクトの前提（言語バージョンなど）」。
- **Rules** は「常に守るべきコーディング規約（命名規則・MVC など）」。
- **Skills** は「特定のタスクを行うための手順書（DAO 作成など）」。
- 迷ったら、まずは `GEMINI.md` と `Rules` に「よく注意されること」を書いてみましょう！

AI に正しく指示を出せれば、プログラミング学習の効率は何倍にもなります。ぜひ試してみてくださいね！🚀