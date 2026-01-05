---
title: "Antigravityで迷う「Skills？Rules？Workflow？GEMINI.md？」使い分けガイド（初学者向け）"
emoji: "🗺️"
type: "tech"
topics: ["antigravity", "gemini", "ai", "workflow", "guide"]
published: true
---

# Antigravity で迷う「Skills？Rules？Workflow？GEMINI.md？」使い分けガイド（初学者向け）

Antigravity を触り始めると、**Rules**や**Skills**、さらに**Workflow**や`GEMINI.md`といった“AI に指示する仕組み”がいくつも出てきて混乱しがちです 。  
結論から言うと、これは役割が違います（似て見えても、置き場所と効かせ方が違う）。

この記事では、Antigravity（Gemini 系環境）でよくある構成「`GEMINI.md` + skills/」を前提に、**初学者が迷わない使い分け**を表と具体例でまとめます 。

---

## まず結論：一言でいうと何？

- `GEMINI.md`：プロジェクトの「憲法」（絶対守る基本方針）
- Rules：日常運用の「ガードレール」（常時/条件付きで適用されるルール）
- Skills：タスク別の「専門家マニュアル」（必要なときにだけ読む“役割・手順”）
- Workflow：作業の「手順書」（人間 or エージェントが手順通りに進めるための流れ）

ポイントは、**Rules/GEMINI.md は“どう振る舞うべきか”**、**Skills/Workflow は“どうやって達成するか”**の比重が高いことです 。

---

## 使い分け早見表（これだけ見れば OK）

| 名前              | 役割（何を書く？）                                                  | いつ効く？                                              | 置きどころのイメージ                                 | 向いてる例                                                                              |
| ----------------- | ------------------------------------------------------------------- | ------------------------------------------------------- | ---------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `GEMINI.md`       | 最上位方針（口調・品質基準・禁止事項・プロジェクトの前提）          | チャット開始時にまず読まれる前提                        | リポジトリルート直下                                 | 「この PJ は Next.js(App Router)、TypeScript 必須」「出力は日本語」「セキュリティ優先」 |
| Rules             | 開発ルール（命名規則、i18n 運用、コミット規約、例外処理の統一など） | Always On / Model Decision など設定により常時〜条件付き | `agent/rules/` など（UI から管理）                   | 「翻訳キーは ja/en 両方に必ず追加」「API は必ず Zod でバリデーション」                  |
| Skills（skills/） | タスク別の専門手順（役割・判断基準・チェックリスト・必要ファイル）  | 依頼内容に応じて自動ピックされる想定                    | `skills/` フォルダに用途別ファイル                   | 「ブログ記事作成スキル」「リファクタ手順スキル」「Shopify 商品登録スキル」              |
| Workflow          | 手順の流れ（手順 1→2→3、入力/出力、完了条件）                       | 実行するときだけ参照（都度）                            | docs/ や skills 内、またはプロジェクト運用に合わせる | 「リリース手順」「新規ページ追加」「障害対応フロー」                                    |

> 記事の運用例では、Gemini はまず`GEMINI.md`を読み、依頼に応じて`skills/`から最適なスキルを選ぶ、という整理でした 。

---

## Rules の「Model Decision」って何？ Skills と同じ？

同じに見えやすい理由は、どちらも「モデルが必要だと思ったら適用する」動きになり得るからです 。  
ただし、**目的が違う**ので分けると運用が楽になります 。

- Model Decision な Rules：  
  “破ると事故るルール”を、状況に応じて賢く効かせたい（ただし基本は守ってほしい）
  ![Model Decision](https://github.com/Inosuke0718/Zenn/blob/main/images/antigravity-guide-skills-rules/image-5.png?raw=true)
- Skills：  
  “この作業をやるときの詳細手順・役割”を、必要なときだけロードしてトークン節約＆再現性 UP

迷ったらこの基準が簡単です：

- **横断的・常設の規約** → Rules（または`GEMINI.md`）
- **特定タスクのレシピ** → Skills（＋ Workflow）

---

## 具体例：i18n ルールはどこに置く？

たとえば画像のような「翻訳キー運用（ja/en 両方更新、重複回避、命名規則…）」は、プロジェクト全体に関わるので Rules が向いています（常に守ってほしい）。

一方で、もし「翻訳キー追加を自動化して、差分作成までやる」みたいに**作業フロー化**するなら、Skills/Workflow 側に寄せるとメリットが出ます 。

- Rules 側（例）：
  - `useTranslations`を使うなら ja/en 両方にキーを追加する
  - 追加前に既存キーを検索して重複を避ける
  - 命名規則（例：`page.section.item`）を守る
- Skills 側（例）：
  - “翻訳キー追加スキル”として、具体的な手順（検索 → 追加 → 整形 → チェック → テスト）を提供する
  - 可能ならスクリプト/コマンドも同梱して半自動化する

---

## 初学者向け：おすすめの最小構成

最初は次の 2 つだけでも十分です 。

1. `GEMINI.md`：プロジェクトの大前提（5〜15 行くらい）
2. Rules：日常で破りがちなルール（i18n、命名、例外処理など）

慣れてきたら、頻繁に繰り返す作業を Skills/Workflow へ移します 。

- 繰り返す作業が増える
- 生成品質にムラがある
- 依頼するたびに同じ説明をしている  
  → このどれかが出たら Skills 化のタイミングです 。

---

## そのまま使えるテンプレ

### GEMINI.md（最小）

```md
# Project Constitution (GEMINI.md)

- Output language: Japanese
- Stack: Next.js(App Router) + TypeScript
- Prefer small, safe diffs.
- Never invent API responses; ask when unsure.
- Follow project Rules and existing patterns.
```

（上は例です。あなたの PJ に合わせて短く保つのがコツです）

### Skills ファイル（最小の考え方）

```md
# i18n-key-add Skill

## When to use

- When adding new UI text that requires translations.

## Checklist

- Search existing keys to avoid duplicates.
- Add keys to both ja and en JSON.
- Keep the same nested structure.
- Verify the component uses the correct key.
```

“作業の型”だけ書いておけば、毎回の説明コストが下がります 。

---

![](/images/antigravity-guide-skills-rules.jpg)

i18n（internationalization / 国際化）とは、アプリや Web サイトを多言語・多地域に対応できるように、最初から設計・実装しておくことです 。たとえば「画面の文言をコードに直書きせず、翻訳用の JSON（リソースファイル）からキーで取り出す」「言語によって日付/通貨/表記が変わっても破綻しない」ようにしておくのが典型です 。なお、特定の言語向けに翻訳・調整する作業は l10n（localization / ローカライズ）と呼ばれ、i18n の次の工程として説明されます 。
