---
title: "GoogleのPomelliで気になるサイトを分析してみよう：使い方とBrand Book作成ガイド"
emoji: "🎨"
type: "idea"
topics: ["google", "ai", "pomelli", "個人開発", "デザイン"]
published: true
---

「このサイト、雰囲気が好きだな」「見やすいけれど、どんな色や言葉を使っているんだろう？」と思ったことはありませんか。

この記事では、**気になるサイトの色・フォント・文章の雰囲気を、AIがどう読み取るかを見てみる**ことから始めます。自分のサイトを持っていない人も、まずは好きなサイトの見せ方を知るつもりで読み進めてみてください。

使うのは、Google Labsの **Pomelli** です。本来は、事業やサービスを宣伝するための画像・紹介コンテンツ・WebサイトをAIで作成するサービスで、WebサイトのURLからブランドの特徴を読み取ります。ここでいうブランドの特徴とは、「どんな色を使い、どんな雰囲気の言葉で、何を伝えているか」といった要素です。

たとえば、次のような視点で結果を見ていきます。

- **配色を知る**：サイトの雰囲気を作っている色は何か。
- **言葉づかいを知る**：親しみやすい、落ち着いているなど、文章にどんな特徴があるか。
- **伝えたいことを考える**：どんなサービスとして紹介され、どんな価値が読み取られるか。
- **見せ方を資料で振り返る**：ロゴ・配色・文章のトーンをまとめると、どんな印象になるか。

今回はKIKI NEKOのサイトを例に、分析結果を確認する **Business Profile** と、ブランドの見せ方をまとめた資料 **Brand Book** を作る流れを解説します。実際に出力された7ページのPDFも見ながら、サイトの特徴をどう整理できるか確かめます。

なお、結果はAIによる解釈であり、サイト運営者が定めた正式なブランド方針とは限りません。まずは元のサイトと見比べて、「なるほど」と思う点や「少し違うかも」と思う点を探してみましょう。自分のサイトがある人は、その見直しや紹介素材づくりにもつなげられます。

![Pomelliで作成されたKIKI NEKOのBrand Book表紙](https://raw.githubusercontent.com/Inosuke0718/Zenn/main/images/pomelli-guide/brand-cover.png)
*完成したBrand Bookの表紙。ブランド名とビジュアルを組み合わせた資料になっています。*

:::message
2026年10月16日時点の公式情報と、操作画面・出力PDFをもとにしています。画面で確認できるBusiness Profile／Brand Bookを中心に説明し、Campaigns・Photoshoot・Websitesは機能概要を紹介します。
:::

## Pomelliとは？

Pomelliは、Google LabsがGoogle DeepMindと共同で開発した、ビジネス向けのAIマーケティングツールです。Webサイトからブランドの特徴を読み取り、その情報に沿ったコンテンツ作成を支援します。

公式の初期紹介ではブランド情報を「Business DNA」と呼んでいます。今回の画面では、その情報を確認・編集する場所が **Business Profile** と表示されています。[Google公式の紹介記事](https://blog.google/innovation-and-ai/models-and-research/google-labs/pomelli/)

最初の画面では、次の4つの使い方が案内されます。

![Pomelliのウェルカム画面に表示された4つの機能](https://raw.githubusercontent.com/Inosuke0718/Zenn/main/images/pomelli-guide/welcome.png)

| 機能 | できること |
| --- | --- |
| Business Profile | ブランドの色・フォント・価値観などを整理する |
| Campaigns | ブランドに合ったキャンペーン案や素材を作る |
| Photoshoot | 商品画像をもとに、紹介用のビジュアルを作る |
| Brand Book / Websites | ブランド資料やWebサイトを作る |

これらの土台になるのがBusiness Profileです。最初にここを確認しておくと、後から生成するコンテンツの方向性を合わせやすくなります。

### 日本から使える？ 料金は？

確認時点の公式ヘルプでは、日本は提供対象国に含まれています。対象年齢は18歳以上、対応言語は英語です。日本から利用できることと、日本語UIに対応していることは別なので、この記事ではボタン名を画面の英語表記に合わせます。[提供地域と言語](https://support.google.com/labs/answer/16945066)

料金については、現時点では無料と案内されています。ただし、生成回数には上限があるため、無制限に使えるという意味ではありません。最新の条件は[公式の利用案内](https://support.google.com/labs/answer/16715058)で確認できます。

## 1. サイトのURLを入力する

[Pomelli公式サイト](https://labs.google.com/pomelli/about)を開き、案内に沿って進みます。ウェルカム画面の **Let's go!** を選択すると、WebサイトのURLを入力する画面になります。

![WebサイトのURLを入力する画面](https://raw.githubusercontent.com/Inosuke0718/Zenn/main/images/pomelli-guide/website-input.png)
*「Enter your website」で解析したいサイトを指定します。*

今回は `https://kiki-neko.com/` をもとにした結果を見ていきます。まずはこの例で、URLからどんな情報が読み取られるのかを確認しましょう。URLを入力し、**Continue** を選択すると解析が始まります。

この画面には、Google Business Profileの情報を含めるチェックボックスもあります。読み込ませたいブランドと、表示されているビジネスが一致しているか確認しましょう。別の事業の情報を混ぜたくない場合はチェックを外します。

Webサイトがない場合は、**No website yet?** から始める方法も用意されています。詳しい手順は[Business Profileの公式ヘルプ](https://support.google.com/labs/answer/17090488)を参照してください。

## 2. Business Profileで「どう解釈されたか」を確認する

解析後の画面がこちらです。

![KIKI NEKOのロゴ・フォント・配色・ブランドの特徴が整理されたBusiness Profile](https://raw.githubusercontent.com/Inosuke0718/Zenn/main/images/pomelli-guide/business-profile.png)
*上部にロゴ・フォント・色、下部にタグラインや価値観などが並びます。*

今回の結果では、黒猫の画像とともに、次のような情報が整理されていました。

| 項目 | 今回表示された内容 |
| --- | --- |
| ブランド名 | KIKI NEKO |
| フォント | Sans-serif |
| 色 | `#FAF4F0`、`#1B3D82`、`#3876D8` |
| タグライン | Live smarter, live better. |
| 価値観 | Practicality、Privacy、Simplicity、Focus |
| 文章のトーン | Friendly、Playful、Practical、Empathetic |

「どんな色を使うか」だけでなく、「どんな言葉で伝えるか」までまとめられているのが特徴です。

たとえば、実用性やシンプルさを重視するブランドなら、紹介文でも大げさな表現を重ねるより、何が便利になるのかを具体的に説明する方針につなげられます。

ただし、ここに表示されるのはAIが整理した結果です。ブランドの正式な方針として使う前に、事業内容や対象ユーザーが意図どおりに伝わっているか確認します。

### 具体的に確認したいところ

まず見たいのは、事業説明です。今回の説明文では、KIKI NEKOが日常の手間や時間管理などを助けるWeb・デスクトップツール群として紹介されています。提供していない機能や、意図しない事業説明が混ざっていないかを見ます。

次にロゴと色です。サイト内の一部の画像や、特定サービスの色が、ブランド全体の代表として選ばれる可能性もあります。自分が共通ルールにしたいものと一致するか確認しましょう。

右側の **Pomelli Agent** には、変更したい内容を文章で伝えられます。以下は、修正を依頼するときの入力例です。今回実行したプロンプトではありません。

```text
Focus the business overview on practical tools for everyday tasks.
Keep the tone friendly and clear.
Do not add features that are not described on the website.
```

「どこを、どう直したいか」を具体的に伝えると、修正後の確認もしやすくなります。直接編集できる項目もあります。[Business Profileの編集方法](https://support.google.com/labs/answer/17090488)

## 3. Brand Bookの表紙を選ぶ

Business Profileを確認したら、左メニューの **Brand Book** に進みます。

Brand Bookは、ロゴ・配色・文章のトーンなど、ブランドの見せ方を一つにまとめた資料です。デザインを依頼するときや、複数の告知素材に統一感を持たせたいときの参考になります。

最初に表示されるのが、表紙を選ぶ画面です。

![Brand Bookの表紙を選択する画面](https://raw.githubusercontent.com/Inosuke0718/Zenn/main/images/pomelli-guide/cover-selection.png)
*Step 1 of 2。背景画像付きの表紙と、単色の表紙が候補に並んでいます。*

画面には **Select image** と **Generate image** があり、用意された候補を選ぶ以外の入口もあります。今回は、立体的な図形を背景にした表紙が選択されています。

候補を選んだら **Confirm** で次へ進みます。

なお、見栄えのよさとブランドへの適合は別々に確認したいところです。今回の表紙は落ち着いた立体表現ですが、黒猫のピクセルアートを主役にしたいなら、そちらに合わせた画像を選ぶ余地があります。

## 4. Brand Bookに載せる画像を選ぶ

次に、資料内に載せる画像を選びます。

![Brand Bookに掲載する画像の選択画面](https://raw.githubusercontent.com/Inosuke0718/Zenn/main/images/pomelli-guide/image-selection.png)
*Step 2 of 2。画像候補と、配置のプレビューが表示されています。*

この画面では **Select 3–7 images** と案内されています。候補画像から選ぶほか、**Upload** から画像を追加することもできます。

この段階では、単に枚数を埋めるよりも、初めてブランドを見る人に何を伝えたいかを考えて選ぶとよさそうです。

- ロゴやキャラクターがはっきり分かる画像
- 代表的なサービスの紹介画像
- 実際の利用イメージが伝わる画面

小さな文字が多いスクリーンショットは、資料内で縮小されると読みにくくなります。配置プレビューを見ながら、画像の見せたい部分が残っているかも確認します。

選択を終えたら **Confirm** で確定します。表紙や画像の変更、PDFの保存手順は[Brand Bookの公式ヘルプ](https://support.google.com/labs/answer/17094292)にもまとまっています。

## 5. 出力された7ページのPDFを見る

完成したBrand Bookは **Download PDF** から保存できます。今回のPDFは次の構成でした。ページ数や内容は今回の出力例です。

| ページ | 内容 |
| --- | --- |
| 1 | 表紙 |
| 2 | Brand Overview：ブランド概要 |
| 3 | Brand Logo：ロゴと使い方 |
| 4 | Typography：フォント |
| 5 | Color Palette：配色 |
| 6 | Imagery：ブランドの画像 |
| 7 | Brand Voice：価値観・見た目・文章のトーン |

### ロゴの使い方まで資料になる

![Brand Bookのロゴ紹介ページ](https://raw.githubusercontent.com/Inosuke0718/Zenn/main/images/pomelli-guide/brand-logo.png)
*元のロゴに加えて、白黒のバリエーションや余白・最小サイズの説明が配置されています。*

ロゴを載せるだけでなく、周囲に確保する余白や最小サイズまで記載されています。今回のPDFでは、余白は各辺45px、最小幅は108pxという記載がありました。

ただし、これらは生成された資料内の数値です。既存のロゴ利用ルールと一致することを確認できるまでは、正式な規定として採用せず、実際の表示サイズで読みやすさを確かめたいところです。

### 配色を数値で共有できる

![Brand Bookのカラーパレットのページ](https://raw.githubusercontent.com/Inosuke0718/Zenn/main/images/pomelli-guide/brand-colors.png)

色には名前が付けられ、HEX・RGB・CMYK・HSLの値が並んでいました。

| 色名 | HEX |
| --- | --- |
| Chalk White | `#FAF4F0` |
| Twilight Blue | `#1B3D82` |
| Royal Blue | `#3876D8` |

「この青を使う」と言葉だけで説明するより、コードと見本がある方が共有しやすくなります。Webサイトや告知画像を作るときに、参照先を一つにまとめられる点が便利です。

### 画像の組み合わせでサービスの雰囲気が伝わる

![Brand BookのImageryページに配置されたサービス画像と黒猫](https://raw.githubusercontent.com/Inosuke0718/Zenn/main/images/pomelli-guide/brand-imagery.png)

今回のImageryページには、Mewmodoro、KIKI SNAP、黒猫の画像が配置されています。ロゴだけでは分からない、個々のサービスの雰囲気も見せられます。

一方で、配置によって画像の端が切れることもあります。今回も画像の一部がトリミングされているため、サービス名や重要な要素が読めるかを、出力後のPDFで確認しておきたいです。

### フォントの指定は補足したい

Typographyページのフォント名は **sans-serif** でした。これは具体的なフォントファミリーの名前ではなく、書体の分類です。

そのままだと、資料を受け取った人がどのフォントを使えばよいか判断できません。実際に運用するなら、使用するフォント名やウェイト、日本語用フォントなどを決めて補うと、再現しやすい資料になります。

**生成直後のBrand Bookを、ブランドのルールを整えるための初稿として使う**と、確認すべき点が見えてきます。

## Brand BookからWebサイト作成へ

Pomelliには **Websites** も用意されています。Business Profileの画面下部にも **Create Website** ボタンがあり、整理したブランド情報をサイト制作につなげられる構成です。

以下は公式ヘルプに基づく手順です。今回の画面・PDFにはWebサイトの生成結果が含まれていないため、完成サイトの品質についてはここでは評価しません。

1. Business Profileを作成・確認する。
2. **Websites → Create Website** でサイトを生成する。
3. **Edit** で修正内容を入力し、**Generate** で反映する。
4. **Preview in New Tab** で見え方を確認する。
5. 内容を確認したうえで、**Publish** をオンにして公開する。

URLの末尾を変更する機能や、生成した別バージョンを扱う機能も案内されています。独自ドメインやコードの書き出しについては、ここで参照したヘルプだけでは判断できません。[Webサイト作成の公式ヘルプ](https://support.google.com/labs/answer/17090489)

Brand Bookにも公開・共有機能があります。**PDFとして保存する操作と、URLで公開する操作は別**です。資料を手元で確認したい段階では、まずPDFをダウンロードして内容を確認すると進めやすいです。[Brand Bookの公開と共有](https://support.google.com/labs/answer/17094292)

## CampaignsとPhotoshootはどんなときに使う？

Brand Bookがブランドの方向性をまとめる資料だとすると、CampaignsとPhotoshootは発信に使う素材を作る機能です。

**Campaigns** は、ブランド情報に合わせた企画や告知素材を考えたいときに使えます。たとえば個人開発なら、新しいサービスの紹介や機能追加のお知らせなどが活用先になります。[Google公式の機能紹介](https://blog.google/innovation-and-ai/models-and-research/google-labs/pomelli-in-europe/)

**Photoshoot** は、商品画像をもとに紹介用のビジュアルを作る機能です。実物商品の見せ方を検討する用途がイメージしやすいと思います。[Photoshootの公式紹介](https://blog.google/innovation-and-ai/models-and-research/google-labs/pomelli-photoshoot/)

個人開発のアプリを紹介する場合は、生成したイメージ画像と、実際の操作画面を区別して使いたいところです。機能説明の画像には実際のスクリーンショットを使えば、利用者が画面を探すときにも役立ちます。

## 個人開発でどう活用できそうか

今回の例で便利だと感じるのは、ロゴ、色、サービスの説明、言葉のトーンを一か所にまとめられることです。

個人で複数のサービスを作っていると、それぞれの紹介ページはあっても、開発者全体としてどんな雰囲気で伝えるかは曖昧になりがちです。Business Profileを確認する作業は、自分のサイトが外からどう見えるのかを見直すきっかけになります。

そこからBrand Bookを作れば、次の告知画像や紹介ページを考えるときに参照できます。毎回ゼロから色や文章の方向性を考える負担を減らせそうです。

自分のサイトがまだない人は、今回の例を見ながら、好きなサイトの配色や文章の雰囲気にも目を向けてみてください。「なぜこのサイトが好きなのか」を言葉にする練習になります。自分のサイトがある人は、Business Profileの説明と配色を確認し、Brand BookをPDFにするところまで試すと、「この情報は使えそう」「フォント指定は補いたい」と具体的に判断できます。

## 参考リンク

- [Pomelli公式サイト](https://labs.google.com/pomelli/about)
- [Google公式：Pomelliの紹介](https://blog.google/innovation-and-ai/models-and-research/google-labs/pomelli/)
- [Google公式：Pomelli Agent、Brand Book、Websitesの追加](https://blog.google/innovation-and-ai/models-and-research/google-labs/pomelli-agentic-capabilities/)
- [利用条件・料金などの公式ヘルプ](https://support.google.com/labs/answer/16715058)
- [提供地域と言語](https://support.google.com/labs/answer/16945066)
- [Business Profileの作成と編集](https://support.google.com/labs/answer/17090488)
- [Brand Bookの作成と管理](https://support.google.com/labs/answer/17094292)
- [Webサイトの作成と管理](https://support.google.com/labs/answer/17090489)
