---
title: "【2026年版】モダンなアイコンライブラリ9選＋α ＆ 失敗しない使い分け完全ガイド"
emoji: "🎨"
type: "tech"
topics: ["react", "nextjs", "tailwindcss", "frontend", "design"]
published: true
---

Webフロントエンド開発において、「アイコンをどこから持ってくるか」は地味に毎回悩むテーマです。

かつては「とりあえず Font Awesome を CDN で読み込む」が定番でしたが、ここ数年で状況は大きく変わりました。

1. **コンポーネント指向の普及**：アイコンをフォントではなく SVG コンポーネントとして import し、props で色・サイズ・太さを制御するのが標準になった
2. **デザイントレンドの変化**：Tailwind CSS や shadcn/ui の普及で、細いストローク＋角丸のミニマルな線画が主流に
3. **バンドルサイズへの意識**：「使うアイコンだけをビルドに含める」ことが当たり前になり、全部入りフォントを読み込む手法が敬遠されるように

この記事では、2026年時点で押さえておきたい主要アイコンライブラリ9つ＋補完的に知っておくと便利な2つを、**アイコン数・ライセンス・グリッド設計といった実データ付き**で整理します。

:::message
本文中の数値・ライセンスは 2026年8月時点で公式リポジトリ・公式ドキュメントを確認したものです。特にアイコン数は頻繁に増減するため、採用前に必ず公式サイトで最新の情報をご確認ください。
:::

---

## 1. 選定前に押さえる5つの評価軸

| 評価軸 | チェックすること |
| :--- | :--- |
| **デザインの一貫性** | グリッドサイズ・ストローク幅・角丸の値が全アイコンで統一されているか |
| **スタイルの幅** | Outline / Solid / Duotone など、1アイコンに複数バリエーションがあるか |
| **カバー率** | 必要なアイコン（特にニッチな概念やロゴ）が実際に存在するか |
| **DX・パフォーマンス** | npm パッケージの品質、フレームワーク対応、Tree-shaking の効き方 |
| **ライセンスとコスト** | 商用利用の可否、**帰属表示（attribution）の要否**、無料版の制限 |

特に見落としがちなのが最後の「帰属表示の要否」です。MIT / ISC / Apache 2.0 なら UI 上の表記は不要ですが、CC BY 系はコード内へのライセンス表記が必要になります。

---

## 2. スペック早見表

| ライブラリ | アイコン数 | スタイル | ライセンス | グリッド |
| :--- | :--- | :--- | :--- | :--- |
| **Font Awesome** | Free 約2,000 / Pro 63,000+ | Free は Solid・Regular・Brands のみ | Free: CC BY 4.0＋SIL OFL＋MIT / Pro: 有料 | 16px ベース |
| **Lucide** | 1,600+ | Outline中心 | ISC | 24×24 / stroke 2px |
| **Phosphor Icons** | 1,500+ | 6ウェイト | MIT | viewBox 256×256 |
| **Hugeicons** | Free 5,400+ / Pro 59,000+ | Free は Stroke Rounded のみ | Free: MIT / Pro: 有料 | 24×24 |
| **Heroicons** | 292 | 4サイズ・スタイル | MIT | 24 / 20 / 16 |
| **Iconoir** | 1,600+ | Outline中心 | MIT | 24×24 / stroke 1.5px |
| **Material Symbols** | 3,800+ | 3スタイル × 4可変軸 | Apache 2.0 | opsz 20〜48 |
| **Tabler Icons** | 6,000+ | Outline + Filled | MIT | 24×24 / stroke 2px |
| **React Icons** | 40,000+（20以上のセット） | 各セット準拠 | MIT（各セットのライセンスに従う） | 各セット準拠 |

---

## 3. モダンアイコンライブラリ9選

### ① Font Awesome — 網羅性の絶対王者、ただし無料版の範囲に注意

![Font Awesome](https://raw.githubusercontent.com/Inosuke0718/Zenn/main/images/zenn-icon-libraries/font-awesome.png)

🔗 https://fontawesome.com/

2012年から続く最古参。2025年夏にリリースされた v7 では 4,500 以上のアイコンが追加され、Pro 版は 63,000 種類／30スタイル規模まで拡大しました。

**特徴**

- **企業ロゴ（Brands）の網羅率が圧倒的**。他のライブラリでは見つからないニッチなシンボルも高確率で存在する
- Classic / Duotone / Sharp / Sharp Duotone の4ファミリーと、Solid・Regular・Light・Thin の各スタイル

**ここが誤解されやすい**

:::message alert
**Light / Thin / Duotone / Sharp はすべて Pro（有料）専用です。**
無料版で使えるのは **Solid・Regular・Brands の約2,000種類のみ**（Regular は収録数がさらに限られます）。「Duotone で2色に塗り分けてリッチに見せる」といった表現は有料ライセンス前提なので、記事や提案書で紹介するときは要注意です。
:::

またライセンスも単一ではなく、**アイコンは CC BY 4.0、フォントは SIL OFL 1.1、コードは MIT** という組み合わせです。CC BY はソースコード内へのライセンス表記が必要になるため、他のライブラリ（MIT / ISC）より運用上のひと手間がかかります。

**おすすめのシーン**

- 業務システム・大規模ポータルなど、とにかくアイコンの種類を要求されるプロジェクト
- SNS やサービスのロゴを大量に扱う場合

---

### ② Lucide — React エコシステムの事実上の標準

![Lucide](https://raw.githubusercontent.com/Inosuke0718/Zenn/main/images/zenn-icon-libraries/lucide.png)

🔗 https://lucide.dev/

メンテナンスが止まった名作「Feather Icons」を2020年にコミュニティがフォークし、286個から1,600個以上まで拡張したプロジェクトです。

**特徴**

- **shadcn/ui の標準アイコン**として採用されており、Next.js + Tailwind 構成では実質デファクト
- 24×24 グリッド・2px ストローク・丸いキャップという明文化された作図ルールがあり、2020年に描かれたアイコンと先月追加されたアイコンを並べても違和感が出ない
- ISC ライセンス。商用利用可・帰属表示不要

**2026年6月：v1.0 で破壊的変更あり**

:::message alert
Lucide は 2026年6月に初の安定版 v1.0 をリリースし、**GitHub や Figma などの商標入りブランドアイコンをすべて削除しました**（法的リスクとメンテナンス負荷が理由）。ロゴが必要な場合は後述の Simple Icons への移行が公式に案内されています。既存プロジェクトを v1 に上げる際は移行ガイドの確認が必須です。
:::

**おすすめのシーン**

- Next.js + Tailwind CSS + shadcn/ui の構成
- 「迷ったらまずこれ」と言える汎用性の高さ

---

### ③ Phosphor Icons — 6ウェイトによる表現力

![Phosphor Icons](https://raw.githubusercontent.com/Inosuke0718/Zenn/main/images/zenn-icon-libraries/phosphor-icons.png)

🔗 https://phosphoricons.com/

約1,500種類のアイコンすべてに **Thin / Light / Regular / Bold / Fill / Duotone** の6ウェイトが用意されている、バリエーション重視のライブラリです。

**特徴**

- ホバー時に Outline → Fill へ切り替える、といったインタラクションが1つのライブラリで完結する
- SVG の viewBox は **256×256**（16px 表示を基準に設計されており、小さくても潰れない）
- props で直感的に制御できる

```tsx
import { HorseIcon } from "@phosphor-icons/react";

<HorseIcon weight="duotone" color="royalblue" size={32} />
```

なお Phosphor の Duotone は「任意の2色を指定する」方式ではなく、副パスを不透明度で薄く見せる方式です。Font Awesome Pro の Duotone とは仕様が異なる点に注意してください。

**おすすめのシーン**

- 状態変化でアイコンの太さや塗りを切り替えたいプロダクト
- タイポグラフィのウェイトに合わせてアイコンの太さも揃えたい場合

---

### ④ Hugeicons — トレンド感は随一。ただし無料版はワンスタイル

![Hugeicons](https://raw.githubusercontent.com/Inosuke0718/Zenn/main/images/zenn-icon-libraries/hugeicons.png)

🔗 https://hugeicons.com/

Figma コミュニティ経由で人気が急上昇した、角丸ストロークが美しいアイコンセットです。

**特徴**

- 24×24 グリッドで作図された `stroke-rounded` スタイルは、今のモダン UI との相性が抜群
- AI・SaaS・Web3 など、新しい概念を表すアイコンが充実している
- Figma プラグインの完成度が高く、デザイン↔実装の乖離が起きにくい

**ここが誤解されやすい**

:::message alert
Hugeicons は**フリーミアム**です。無料で使えるのは **Stroke Rounded の1スタイル・5,400種類前後**（MIT ライセンス）。Solid・Duotone・Bulk・Twotone などを含む10スタイル・59,000種類は Pro（年額有料・1ライセンス1シート）です。「スタイルが豊富」という紹介は Pro 前提なので、チームで使うならシート数を含めた予算確認を先に行ってください。
:::

**おすすめのシーン**

- デザイナーが Figma で Hugeicons を指定してきている案件
- モダンな SaaS プロダクト・LP

---

### ⑤ Heroicons — Tailwind ユーザーの最短ルート

![Heroicons](https://raw.githubusercontent.com/Inosuke0718/Zenn/main/images/zenn-icon-libraries/heroicons.png)

🔗 https://heroicons.com/

Tailwind CSS 開発元の Tailwind Labs 製。使用サイズごとに最適化された4種類が提供されます。

- 24×24 Outline
- 24×24 Solid
- 20×20 Solid（Mini）
- 16×16 Solid（Micro）

```tsx
import { BeakerIcon } from "@heroicons/react/24/solid";

<BeakerIcon className="size-6 text-blue-500" />
```

**ここが誤解されやすい**

:::message
Heroicons の収録数は **292種類**と、他のライブラリと比べて極端に少ないです。しかも公式リポジトリは**新規アイコンの追加リクエストやコントリビューションを受け付けていません**（バグ修正のみ）。「少数精鋭で光学的な重さが完璧に揃っている」のが売りである一方、ニッチな用途では確実にアイコンが足りなくなります。**単体で採用せず、不足分を補うサブライブラリとセットで検討する**のが現実的です。
:::

**おすすめのシーン**

- Tailwind CSS がメインで、必要なアイコンが一般的な UI 要素に収まるプロジェクト
- npm を増やさず SVG をコピペで済ませたい場合

---

### ⑥ Iconoir — 完全無料・制限なしのミニマリスト

![Iconoir](https://raw.githubusercontent.com/Inosuke0718/Zenn/main/images/zenn-icon-libraries/iconoir.png)

🔗 https://iconoir.com/

Pro 版という概念自体が存在しない、純粋なオープンソースライブラリです。

**特徴**

- 1,600種類以上すべてが MIT ライセンス、帰属表示不要
- 24×24 グリッド・1.5px ストロークで、Lucide より少し幾何学的・構造的な印象
- React / React Native / Vue / Flutter / Figma / Framer など対応先が広い

**おすすめのシーン**

- ライセンスの検討コストを一切かけたくない個人開発・OSS
- Lucide の雰囲気とは少し違う、硬質なミニマルデザインを狙いたいとき

---

### ⑦ Material Symbols — Variable Font による無段階調整

![Material Symbols](https://raw.githubusercontent.com/Inosuke0718/Zenn/main/images/zenn-icon-libraries/material-symbols.png)

🔗 https://fonts.google.com/icons

Google の「Material Icons」の後継。可変フォント技術を採用しています。

**特徴**

- **FILL（0〜100）／wght（100〜700）／GRAD（-50〜200）／opsz（20〜48）** の4軸を CSS で無段階に制御できる
- Outlined / Rounded / Sharp の3スタイル
- CSS transition と組み合わせれば「ホバーでじわっと塗りつぶされる」といった演出が数行で書ける
- Apache 2.0 ライセンス

**必ずやるべき最適化**

:::message alert
デフォルトの読み込み方だと **3,800種類以上のアイコン全部（約295KB）** がダウンロードされます。`&icon_names=` パラメータで使用アイコンだけをサブセット化すれば **1.7KB** まで削減できるので、本番投入時は必須の対応です。
:::

```html
<!-- NG: 全アイコン読み込み（約295KB） -->
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined" rel="stylesheet">

<!-- OK: 使うアイコンだけ（アルファベット順・カンマ区切り） -->
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined&icon_names=check,home,search" rel="stylesheet">
```

**おすすめのシーン**

- アニメーションでアイコンの太さや塗りを滑らかに変化させたいとき
- Android アプリや Google 系サービスと世界観を揃えたいとき

---

### ⑧ Tabler Icons — 無料最大級のボリューム

![Tabler Icons](https://raw.githubusercontent.com/Inosuke0718/Zenn/main/images/zenn-icon-libraries/tabler-icons.png)

🔗 https://tabler.io/icons

オープンソースのダッシュボードテンプレート「Tabler」から派生したライブラリ。

**特徴**

- **6,000種類以上（2026年8月時点で 6,184）が MIT ライセンスで完全無料**。汎用ライブラリとしては最大級
- **Outline だけでなく Filled バリアントも用意されています**（線画のみという説明をよく見かけますが、現在は両方あります）
- 24×24 グリッド・2px ストロークで統一
- 公式サイト上でストローク幅・色・サイズを調整してから SVG / JSX をコピー可能

```tsx
import { IconAward } from "@tabler/icons-react";

<IconAward size={36} color="red" stroke={1.5} />
```

**おすすめのシーン**

- 管理画面・ダッシュボードなど大量のアイコンを要求されるプロダクト
- Lucide や Heroicons で「欲しいアイコンが無い」となったときの駆け込み寺

---

### ⑨ React Icons — 複数セットを1つの記法で

![React Icons](https://raw.githubusercontent.com/Inosuke0718/Zenn/main/images/zenn-icon-libraries/react-icons.png)

🔗 https://react-icons.github.io/react-icons/

単一のアイコンセットではなく、Font Awesome・Material・Heroicons・Tabler・Phosphor など20以上のライブラリを共通の書き方で扱えるメタライブラリです。

```tsx
// セットごとにパスを分けて import する
import { FaBeer } from "react-icons/fa";     // Font Awesome
import { MdHome } from "react-icons/md";     // Material Design
import { TbAward } from "react-icons/tb";    // Tabler
```

**採用前に知っておくべき注意点**

:::message alert
- **本家より更新が遅れます。** react-icons は各ライブラリを取り込んで再パッケージする構造なので、上流の新アイコンがすぐには反映されません。特定のセットしか使わないなら、公式パッケージ（`lucide-react` など）を直接入れるほうが確実です
- **Tree-shaking は「効くが万能ではない」。** バレル import（`import * as Icons from "react-icons/fa"`）をすると全部入りになります。また開発サーバーの初回起動が重くなりやすいのも既知の挙動です
- **混ぜすぎるとデザインが崩れます。** 「便利だから」と3セット以上を併用すると、線の太さ・角丸・視覚的密度がバラバラになり、UI が一気に素人っぽくなります
:::

**おすすめのシーン**

- 複数セットの併用が避けられない場合の統合レイヤーとして
- プロトタイピングやモック段階でアイコンを高速に試したいとき

---

## 4. 補完的に知っておくと強い2つ

### ⑩ Simple Icons — ブランドロゴ専用

🔗 https://simpleicons.org/

3,000以上のブランド・サービスの公式ロゴを SVG で提供。Lucide が v1.0 でブランドアイコンを削除した今、**ロゴはここから調達するのが定石**になりつつあります。

:::message alert
ただしロゴは著作権とは別に**商標**の問題があります。ライブラリのライセンスが許諾しているのはあくまで SVG データの利用であって、そのロゴを自由に使う権利ではありません。他社サービスのロゴを掲載する際は、各社のブランドガイドラインを必ず確認してください。
:::

### ⑪ Iconify — 30万超のアイコンを横断検索

🔗 https://iconify.design/

Lucide・Tabler・Phosphor・Iconoir などをまとめて検索・利用できる巨大なフレームワークです。複数セットを跨いで少数ずつ使うようなケースでは、アイコン単位の import が効率的に働きます。逆に単一セットで完結するなら、公式パッケージを直接使うほうが軽量です。

---

## 5. シーン別・使い分けマトリクス

| 開発スタイル・要件 | 推奨 | 理由 |
| :--- | :--- | :--- |
| Next.js + Tailwind + shadcn/ui | **Lucide** | 事実上の標準。追加設定なしで統一感が出る |
| Tailwind でシンプルな UI | **Heroicons**（＋Tabler で補完） | 光学的な統一感は最高だが292種類なので補完前提 |
| 太さ・塗りを動的に変えたい | **Phosphor** / **Material Symbols** | 6ウェイト、あるいは可変フォントの無段階調整 |
| モダンな SaaS / LP（Figma 連携） | **Hugeicons** | 角丸線画のトレンド感と Figma プラグインの完成度 |
| 完全無料・帰属表示なしで種類重視 | **Tabler** / **Iconoir** | どちらも MIT。6,000種類と1,600種類で守備範囲が違う |
| ニッチなアイコンが必要 | **Font Awesome** / **Tabler** | 網羅性。ただし FA は Pro 前提の機能に注意 |
| ブランドロゴが必要 | **Simple Icons** | 商標ガイドラインの確認とセットで |
| 複数セットの併用が確定している | **React Icons** / **Iconify** | 統合レイヤーとして使う |

---

## 6. 運用のベストプラクティス

### ① 原則はアイコンフォントより SVG コンポーネント

Webフォント形式は、フォント読み込み前に文字化けやレイアウトシフトが起きる（FOUT / FOIT）、使わないアイコンまでダウンロードされる、スクリーンリーダーが意図しない読み上げをする、といった課題があります。基本は SVG コンポーネントを選びましょう。

ただし **Material Symbols のように、可変フォントであることが機能そのものになっている例外もあります**。この場合は前述のサブセット化（`&icon_names=`）を必ず併用し、フォント方式のデメリットを潰した上で採用してください。

### ② ライブラリは原則1つ、多くても2つまで

複数を混ぜると、ストローク幅・角丸・視覚的密度がばらつき、「なんとなく雑に見える UI」ができあがります。メインを1つ決め、足りない分だけをサブから借りる運用にしましょう。React Icons や Iconify は便利ですが、**混在を許可する道具ではなく、混在を管理する道具**として使うのが正解です。

### ③ アクセシビリティ（a11y）を必ず考慮する

装飾目的のアイコンには `aria-hidden="true"` を、意味を持つアイコン単体には `aria-label` を付与します。

```tsx
// 装飾（隣にテキストがある場合）
<button className="flex items-center gap-2">
  <Settings aria-hidden="true" className="size-5" />
  設定
</button>

// アイコンのみのボタン
<button aria-label="設定を開く" className="p-2">
  <Settings aria-hidden="true" className="size-5" />
</button>
```

なお `sr-only` は要素名ではなく **CSS クラス**です（`<span className="sr-only">設定を開く</span>` のように使います）。`<sr-only>` というタグは存在しないので注意。

### ④ ライセンスは「無料かどうか」ではなく「何が必要か」で見る

- MIT / ISC / Apache 2.0 … 商用利用可、UI 上の帰属表示は不要（ソース内へのライセンス表記は残す）
- CC BY 4.0（Font Awesome Free のアイコン）… 帰属表示が必要
- フリーミアム（Hugeicons、Font Awesome Pro）… どのスタイルが有料かを事前に確認。シート単位課金にも注意

法務レビューに備えて `THIRD_PARTY_LICENSES.md` のようなファイルにまとめておくと、後々の確認が一瞬で終わります。

### ⑤ Figma のライブラリと実装のライブラリを揃える

デザイナーがいる案件では、Figma プラグインが存在するライブラリを選び、デザインと実装で同一のセットを使うだけでコミュニケーションコストが劇的に下がります。Lucide・Phosphor・Hugeicons・Tabler・Heroicons はいずれも公式プラグインを提供しています。

---

## まとめ

アイコン選定は見た目の好みだけの話ではなく、**開発者体験・パフォーマンス・アクセシビリティ・ライセンスリスク**に直結する意思決定です。

- **迷ったら**：Lucide（React 系のデファクト、ISC）
- **数が必要**：Tabler Icons（6,000種類以上・MIT）
- **表現力重視**：Phosphor Icons（6ウェイト）／ Material Symbols（可変フォント）
- **デザイン性重視**：Hugeicons（無料版はワンスタイルである点に留意）
- **ロゴ**：Simple Icons（商標ガイドラインの確認とセットで）

そして最後にもう一度。**無料版の範囲と帰属表示の要否は、実装を始める前に確認しておきましょう。** 後から差し替えるのが一番コストの高い作業です。
