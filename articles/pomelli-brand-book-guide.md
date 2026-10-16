---
title: "【Google Pomelli】Webサイトの配色や雰囲気をAIが自動分析！ブランドブックの作り方ガイド"
emoji: "🎨"
type: "idea"
topics: ["google", "ai", "pomelli", "個人開発", "デザイン"]
published: true
---

![Pomelliのトップページ](https://raw.githubusercontent.com/Inosuke0718/Zenn/main/images/pomelli-guide/pomelli-top.png)

個人開発やサービス運営をしていると、「自分のサイトの世界観や雰囲気って客観的にどう見えているんだろう？」「デザインやトンマナを統一したいけれど、言語化するのが難しい…」と悩む瞬間、ありませんか？

そんなときに試してみたいのが、Google Labsが公開した **Pomelli** です。

https://labs.google.com/pomelli/about

WebサイトのURLを入力するだけで、AIがロゴ・配色・フォント・文章のトーン＆マナーを自動で読み取り、整理してくれます。

さらに、その情報を **Brand Book（ブランドブック）** というPDFにまとめられます。「ロゴはこれ」「色はこの青」「文章は親しみやすく」といった、サイト制作や告知画像を作るときのデザインガイドライン（ブランドの取扱説明書）のような資料です。

![Pomelliで作成されたKIKI NEKOのBrand Book表紙](https://raw.githubusercontent.com/Inosuke0718/Zenn/main/images/pomelli-guide/brand-cover.png)
*今回作成したBrand Bookの表紙。*

この記事では、**私が個人開発・運営しているWebサイト「KIKI NEKO」** を例に、実際に次の3ステップを試してみます。

1. **サイトのURLを入力する**
2. **AIが読み取った特徴を確認する**
3. **表紙と画像を選び、PDFにする**

ご自身の運営サイトはもちろん、お気に入りのWebサイトで試してみても新しい発見があって面白いですよ！

:::message
2026年10月16日時点の公式情報と、操作画面・出力PDFをもとにしています。
実際に自分で運営しているサイトを入力してみたところ、「AIにはこう見えているのか！」という客観的な発見が多くて驚きました。
:::

## 🎨 Pomelliでできること

Pomelliは、Google LabsとGoogle DeepMindが共同で開発した、ビジネス向けのAIツールです。サイトの特徴をもとに、紹介資料や宣伝用の画像・文章などを作れます。[Google公式の紹介](https://blog.google/innovation-and-ai/models-and-research/google-labs/pomelli/)

![Pomelliのウェルカム画面](https://raw.githubusercontent.com/Inosuke0718/Zenn/main/images/pomelli-guide/welcome.png)

今回使うのは、次の2つです。

| 画面の名前 | 何をするところ？ |
| --- | --- |
| **Business Profile** | サイトから読み取ったロゴ・色・文章の雰囲気などを確認・修正する |
| **Brand Book** | ブランドのロゴや配色、トーン＆マナーを1冊の資料（PDF）にまとめる |

まずBusiness Profileで内容を確認し、Brand BookでPDFにする、という順番です。

### 💴 日本から使える？ 料金は？

確認時点では、**日本から利用でき、料金は無料**です。ただし、生成回数には上限があります。対象年齢は18歳以上、対応言語は英語なので、この記事でもボタン名は英語で紹介します。

最新の条件は、公式ヘルプの[提供地域と言語](https://support.google.com/labs/answer/16945066)・[利用条件と料金](https://support.google.com/labs/answer/16715058)をご確認ください。

## 🌐 1. サイトのURLを入力する

まずはPomelliのサイトを開き、案内に沿って進みましょう。

https://labs.google.com/pomelli/about

トップページの **Let's go!** を押すと、URLの入力画面が表示されます。

![WebサイトのURLを入力する画面](https://raw.githubusercontent.com/Inosuke0718/Zenn/main/images/pomelli-guide/website-input.png)

今回は、私が運営しているサイト `https://kiki-neko.com/` を使って試してみます。URLを入力して **Continue** を押すと、解析が始まります。

Google Business Profileの情報を含めるチェックボックスがある場合は、表示されたビジネスが解析したいサイトと合っているか確認します。別の事業なら、チェックを外してください。

なお、サイトがない場合は **No website yet?** から始める方法もあります。[詳しくは公式ヘルプへ](https://support.google.com/labs/answer/17090488)

## 🔍 2. 読み取られた特徴を確認する

解析が終わると、**Business Profile** に結果が表示されます。

![KIKI NEKOのロゴ・フォント・配色・ブランドの特徴が整理されたBusiness Profile](https://raw.githubusercontent.com/Inosuke0718/Zenn/main/images/pomelli-guide/business-profile.png)
*上部にロゴ・フォント・色、下部にサービスの説明や文章の雰囲気などが並びます。*

実際に私のサイト「KIKI NEKO」を解析してみたところ、次のような結果になりました。英語の項目には、日本語の意味を添えています。

| 項目 | 読み取られた内容 |
| --- | --- |
| 名前 | KIKI NEKO |
| フォント | Sans-serif（書体の分類） |
| 色 | `#FAF4F0`、`#1B3D82`、`#3876D8` |
| キャッチコピー | Live smarter, live better.（より賢く、よりよく暮らす） |
| 大切にしていること | 実用性、プライバシー、シンプルさ、集中 |
| 文章の雰囲気 | 親しみやすい、遊び心がある、実用的、相手に寄り添う |

色やロゴだけでなく、**「どんな言葉で伝えるか」も整理される**のが面白いところです。

### ✅ まずは3点をチェック

- **説明は合っている？** 提供していない機能が書かれていないか。
- **ロゴと色は合っている？** サイトの一部の画像が、全体の代表として選ばれていないか。
- **文章の雰囲気は合っている？** 自分が伝えたい印象とずれていないか。

直したいときは、右側の **Pomelli Agent** に変更内容を伝えます。たとえば、次のような依頼です。これは入力例で、今回実行したものではありません。

```text
Keep the tone friendly and clear.
Do not add features that are not described on the website.
```

意味は「親しみやすく、分かりやすい文章にしてください。サイトに書かれていない機能は追加しないでください」です。

直接編集できる項目もあります。内容を確認してから、次に進みましょう。[編集方法の公式ヘルプ](https://support.google.com/labs/answer/17090488)

## 📄 3. 表紙と画像を選び、PDFにする

左メニューの **Brand Book** を開きます。ここでは、表紙と資料に載せる画像を順番に選びます。

### 🖼️ 表紙を選ぶ

![Brand Bookの表紙を選択する画面](https://raw.githubusercontent.com/Inosuke0718/Zenn/main/images/pomelli-guide/cover-selection.png)

候補から表紙を選び、**Confirm** を押します。今回は、立体的な図形を背景にした表紙を選びました。

画面には、画像を選ぶ **Select image** と、画像を生成する **Generate image** もあります。自分のサービスに合う雰囲気の表紙を選びましょう。

### 📸 資料に載せる画像を選ぶ

![Brand Bookに掲載する画像の選択画面](https://raw.githubusercontent.com/Inosuke0718/Zenn/main/images/pomelli-guide/image-selection.png)

次に、資料内に載せる画像を **3〜7枚** 選びます。**Upload** から手元の画像を追加することもできます。

ロゴ、代表的なサービスの画像、実際の利用画面など、「何のサービスか」が伝わるものを選ぶとよさそうです。プレビューで、文字や見せたい部分が切れていないかも確認します。

選び終えたら **Confirm** を押します。

### 💾 PDFを保存する

完成したら **Download PDF** で保存します。今回できたのは、次の7ページでした。ページ数や内容は、今回の出力例です。

| ページ | 内容 |
| --- | --- |
| 1 | 表紙 |
| 2 | ブランドの概要 |
| 3 | ロゴと使い方 |
| 4 | フォント |
| 5 | ブランドカラー（配色パレット） |
| 6 | サービスやキャラクターの画像 |
| 7 | 価値観や文章の雰囲気 |

PDFの保存とは別に、URLで公開・共有する機能もあります。[Brand Bookの公式ヘルプ](https://support.google.com/labs/answer/17094292)

## 👀 完成したPDFを見てみる

### 🔤 ロゴの使い方がまとまる

![Brand Bookのロゴ紹介ページ](https://raw.githubusercontent.com/Inosuke0718/Zenn/main/images/pomelli-guide/brand-logo.png)

元のロゴに加えて、白黒のバリエーションや、周りに空ける余白、小さく表示するときのサイズまで載っていました。

ただし、**余白やサイズもAIが作った案**です。そのままルールにする前に、実際に使う大きさで見やすいか確認しましょう。

### 🎨 色をカラーコードで共有できる

![Brand Bookのカラーパレットのページ](https://raw.githubusercontent.com/Inosuke0718/Zenn/main/images/pomelli-guide/brand-colors.png)

色の見本と一緒に、色を指定するコードも載ります。

| 色名 | 色コード（HEX） |
| --- | --- |
| Chalk White | `#FAF4F0` |
| Twilight Blue | `#1B3D82` |
| Royal Blue | `#3876D8` |

「青を使って」と伝えるより、このコードを渡すほうが同じ色を再現しやすくなります。サイトやSNS画像の色をそろえるときに便利です。

### 🖼️ サービスの画像を一覧にできる

![Brand BookのImageryページに配置されたサービス画像と黒猫](https://raw.githubusercontent.com/Inosuke0718/Zenn/main/images/pomelli-guide/brand-imagery.png)

今回は、サイト内で公開しているツール（Mewmodoro、KIKI SNAP）やマスコットの黒猫の画像が並びました。ロゴだけでは伝わりにくい、サービスの空気感も視覚的に伝わります。

画像の一部は自動で切り取られるため、保存したPDFでも、サービス名や大事な部分が見えているか確認しておくと安心です。

### ⚠️ フォント名は補う必要があった

今回のフォント欄は **sans-serif** でした。これは書体の分類で、具体的なフォント名ではありません。

このままでは使うフォントを一つに決められないので、制作に使うなら、フォント名や文字の太さ、日本語用のフォントを補っておくと役立ちます。

Brand Bookは、**自分で確認・修正して使う下書き**として考えるとよさそうです。

## 🚀 ほかにできること

整理したブランド情報は、資料以外にも使えます。以下の機能は今回試していないため、公式情報に基づく紹介です。

| 機能 | できること | 使う場面の例 |
| --- | --- | --- |
| **Campaigns** | 告知のアイデアや画像・文章の案を作る | 新しいサービスをSNSで紹介する |
| **Photoshoot** | 手元の商品写真から、背景や光を演出した画像を作る | 商品をスタジオで撮ったように見せる |
| **Websites** | ブランド情報をもとに紹介サイトを作る | 事業やサービスの紹介ページを用意する |

詳しくは、公式の[Campaignsの紹介](https://blog.google/innovation-and-ai/models-and-research/google-labs/pomelli-in-europe/)・[Photoshootの紹介](https://blog.google/innovation-and-ai/models-and-research/google-labs/pomelli-photoshoot/)・[Websitesの使い方](https://support.google.com/labs/answer/17090489)をご覧ください。

## 🏁 まとめ

Pomelliを使ってみて感じたポイントをまとめます。

- **URLを入れるだけでブランド要素を自動分析**: ロゴ、カラー、トーン＆マナーをAIが手早く整理してくれます。
- **Brand Bookで世界観をPDF化**: サイトや告知画像を作るときにデザインがブレない「ガイドライン（ブランドの取扱説明書）」が作れます。
- **最後は人の目で微調整**: 自動抽出されたフォント名や説明文は、必要に応じて手動で調整して仕上げるのがコツです。

「自分のサイトの雰囲気を客観的に整理したい」「デザインの統一感を出したい」という方は、ぜひPomelliを試してみてください！

## 🔗 参考リンク

- [Pomelli公式サイト](https://labs.google.com/pomelli/about)
- [Google公式：Pomelliの紹介](https://blog.google/innovation-and-ai/models-and-research/google-labs/pomelli/)
- [Google公式：Pomelli Agent、Brand Book、Websitesの追加](https://blog.google/innovation-and-ai/models-and-research/google-labs/pomelli-agentic-capabilities/)
- [Business Profileの作成と編集](https://support.google.com/labs/answer/17090488)
- [Brand Bookの作成と管理](https://support.google.com/labs/answer/17094292)

