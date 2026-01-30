---
title: "Antigravityで迷う「Rules？Workflow？Skills？GEMINI.md？」使い分けガイド（初学者向け）"
emoji: "🗺️"
type: "tech"
topics: ["antigravity", "gemini", "ai", "workflow", "guide"]
published: true
---

# Antigravity で迷う「Rules？Workflow？Skills？GEMINI.md？」使い分けガイド

AI エディタの Antigravity を触り始めると、**Rules** や **Workflow**、さらに `GEMINI.md` といった「AI に指示する仕組み」がいくつも出てきて、「結局どこに何を書けばいいの？」と迷う瞬間、ありませんか？

結論から言うと、これらは役割が明確に違います。
さらに最近は **Skills** という仕組みもあり、ここを押さえると運用が一気に楽になります。

この記事では、Java（JSP/Servlet）や Python を学ぶ皆さんが直面するリアルな開発シーンを例に、**初学者が迷わない使い分け**を表と具体例でまとめます。

---

## 🏁 まず結論：一言でいうと何？

- **`GEMINI.md`（グローバルRules）**：
  全プロジェクト共通の「基本方針（常設ルール）」を書いておく場所で、`~/.gemini/GEMINI.md` に置きます。

- **Rules（ワークスペースRules）**：
  プロジェクトごとの「校則（制約・規約）」を、`.agent/rules/` にMarkdownとして置きます。

- **Workflow**：
  反復タスクの「手順書（オンデマンド実行）」を、`.agent/workflows/` にMarkdownとして置き、チャットで `/workflow-name` のようにスラッシュコマンドで呼び出します。

- **Skills**：
  “必要なときだけ読み込まれる”専門手順パッケージで、`SKILL.md` を含むフォルダとして定義され、`.agent/skills/`（プロジェクト）または `~/.gemini/antigravity/global_skills/`（全体）に置きます。

ポイントは、**Rules は常設の制約**、**Workflow は手動で起動する手順**、**Skills は意図に応じて自動適用される手順パッケージ**、という棲み分けです。

---

## 📊 使い分け早見表（これだけ見れば OK）

Java や Python の開発現場に置き換えると、以下のようなイメージです。

| 名前 | 役割（何を書く？） | いつ効く？  | 保存場所（ここが正解）　| 向いてる例（Java/Python）　|
| ------------- | ------------- | ------------- | ------------- | ------------- |
| **GEMINI.md** | 全体の常設ルール（出力言語、説明の粒度、全体方針など）                                        | すべてのワークスペースに適用                                                     | `~/.gemini/GEMINI.md`                                                                       | 「日本語で回答」「初学者向けに専門用語は説明」「まず結論→理由→手順で書く」      |
| **Rules**     | プロジェクト規約（命名、MVC方針、テスト方針、禁止事項）                                       | Always On / Model Decision / Manual など設定に応じて適用                         | `./.agent/rules/`                                                                           | 「JSPにJavaロジックを書かない」「Pythonは型ヒント必須」「ログはlogger使用」     |
| **Workflow**  | 反復タスクの手順（デプロイ、PR対応、テスト生成など）                                          | 必要なときに `/workflow-name` で実行                                             | `./.agent/workflows/`                                                                       | 「Tomcatデプロイ手順」「requirements更新」「DB接続テスト」                      |
| **Skills**    | 専門手順のパッケージ（必要時にだけ読み込む“手順＋ベストプラクティス＋任意の資材/スクリプト”） | 会話開始時に一覧が見え、関連しそうなら `SKILL.md` を読み込まれて実行（自動適用） | `./.agent/skills/<skill>/SKILL.md` / `~/.gemini/antigravity/global_skills/<skill>/SKILL.md` | 「コードレビュー観点固定」「脆弱性チェック手順」「社内テンプレに沿うIssue作成」 |

---

## ⚠️ 「Skills」というボタンはありません（でも公式機能です）

Antigravity のUIに「Skills」という専用の設定画面やボタンが無いことがあります。
ただし **Skills 自体は公式機能**で、UI登録ではなく「所定のフォルダに `SKILL.md` を置く」方式で動きます。

Skills は「`SKILL.md` を含むフォルダ」として定義され、会話開始時にエージェントは利用可能なSkillsの「name/description」を見て、関連があれば `SKILL.md` を読み込み、その指示に従って作業します。
また、明示的に使わせたい場合は、Skill名に言及することで“使うことを保証しやすい”と説明されています。

---

## 🚦 Rules と Workflow の違いは？

「Rules」と「Workflow」、どこが違うの？という疑問がよくあります。
**目的**で分けると運用が楽になります。

- **Rules**：
  エージェントに守らせたい「制約・規約」を、Markdownで常設する仕組みです。
- **Workflow**：
  反復タスクを“手順として保存”し、`/workflow-name` のスラッシュコマンドでオンデマンド実行する仕組みです。

### 迷ったときの判断基準

- 「命名規則」「インデント」「MVC」「必須テスト」など、常に守るべき規約
  👉 **Rules**（全体なら `GEMINI.md`、プロジェクトなら `.agent/rules/`）
- 「デプロイ」「PRコメント対応」「単体テスト生成」など、やる時だけ走らせたい手順
  👉 **Workflow**（`.agent/workflows/` に置いて `/...` で呼ぶ）
- 「状況に応じて自動適用してほしい専門手順（レビュー観点、社内手順、チェックリスト）」
  👉 **Skills**（`.agent/skills/` または `~/.gemini/antigravity/global_skills/`）

---

## 🐍 具体例：MVC モデルやインデント規約はどこ？

たとえば、JSP/Servlet や Python 開発でよくある以下のルールは、プロジェクト全体に関わるので **Rules** が向いています。

### Rules に書くべきこと（校則：常時守ってほしい）

- **Java/JSP**:
  - JSP ファイルには `<% Javaコード %>` を書かず、EL 式と JSTL を使う（MVC の分離）。
  - クラス名は PascalCase（`StudentData`）、変数名は camelCase（`studentName`）。
  - `System.out.println` は使わず、ロガーを使用する。
- **Python**:
  - インデントはスペース 4 つ。
  - 関数には必ず型ヒントをつける（例: `def add(a: int, b: int) -> int:`）。

---

## 🔰 初学者向け：おすすめの最小構成

最初から全部使いこなそうとするとパンクします。まずは次の 2 つだけで十分です！

1. **`GEMINI.md`（グローバルRules）**：全体の方針（5〜10 行くらい）
2. **Rules（ワークスペースRules）**：そのプロジェクトの鉄の掟（命名、MVC、テスト方針など）

慣れてきて、「毎回同じ手順をお願いしてるな…」と感じたら、その作業を **Workflow** にして `/...` で呼び出すのがおすすめです。
さらに「似た依頼のたびに、AIが毎回やり方をブレさせる」なら、**Skills** にして“自動適用される専門手順”として固定化すると安定します。

---

## 📝 そのまま使えるテンプレ

### GEMINI.md（グローバルRules）

- **保存場所**：`~/.gemini/GEMINI.md`（全ワークスペースに適用）

```md
# Global Rules (~/.gemini/GEMINI.md)

- Output language: Japanese
- Audience: Beginner
- Explain jargon briefly
- Format: conclusion -> reason -> steps
```

### ワークスペース固有の Rules

- **保存場所**：`./.agent/rules/`

```md
# Project Rules (.agent/rules/project-profile.md)

## 命名規則

- クラス名は PascalCase
- 変数名は camelCase

## MVC 分離

- JSP に Java ロジックを書かない
- Controller は薄く保つ
```

### Workflow ファイル（例：Java の DAO 作成）

- **保存場所**：`./.agent/workflows/`、呼び出しは `/workflow-name`

```md
# create-dao (.agent/workflows/create-dao.md)

## 概要

データベース操作用の DAO を作成する手順

## 手順

1. `dao/` に新しいクラスを作成
2. `try-with-resources` で `Connection`, `PreparedStatement`, `ResultSet` を管理
3. SQL 値はハードコードせず `?` プレースホルダを使用
4. 例外処理とログを実装
5. 必要に応じて DI を適用
```

### Skill ファイル（例：コードレビュー観点を固定）

- **保存場所**：`./.agent/skills/<skill>/SKILL.md` または `~/.gemini/antigravity/global_skills/<skill>/SKILL.md`

```md
---
name: code-review
description: Reviews code changes focusing on critical correctness, security, and reliability issues.
---

# Code Review Skill

## Principles

- Prefer critical issues over style nitpicks.
- Always cite exact files/lines when pointing issues.

## Checklist

1. Correctness and crashes
2. Security (auth, secrets, injection)
3. Data integrity (DB writes, concurrency)
4. Observability (logging, error handling)
```

---

## まとめ

- **GEMINI.md**（`~/.gemini/GEMINI.md`）は全体に効く **Global Rules**。
- **Rules**（`.agent/rules/`）はプロジェクトごとの常設ルール。
- **Workflows**（`.agent/workflows/`）は `/workflow-name` で呼ぶ反復手順。
- **Skills**（`.agent/skills/` / `~/.gemini/antigravity/global_skills/`）は `SKILL.md` を置いて“意図に応じて自動適用される”専門手順パッケージ。
