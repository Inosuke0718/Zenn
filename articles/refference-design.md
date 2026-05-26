---
title: "Scrollytelling・Parallax・Motion Designを学べる美しいWebサイトまとめ"
emoji: "🎬"
type: "tech"
topics: ["webdesign", "ui", "ux", "animation", "frontend"]
published: false
---

# Scrollytelling・Parallax・Motion Designを学べる美しいWebサイトまとめ

Webサイトに「物語性」や「奥行き」があると、ただ情報を読むだけでなく、体験として記憶に残りやすくなります。

最近の美しいWebサイトでは、単に画像や文字を並べるだけではなく、

- スクロールに合わせて情報が展開される
- 背景と前景に動きの差がある
- カードやボタンに奥行きがある
- DOMアニメーションで視線が誘導される
- 画面全体に空間性がある

といった表現がよく使われています。

これらは感覚的に「おしゃれ」と言われがちですが、実はちゃんと名前のある考え方です。

この記事では、以下のデザイン理論・表現を効果的に使っているWebサイトを、URL付きで紹介します。

```txt
Scrollytelling
Parallax Scrolling
Motion Design
Layered UI / Spatial Design
Elevation
````

---

# まず用語を整理する

## Scrollytelling

Scrollytellingは、**Scroll + Storytelling** を組み合わせた言葉です。

ユーザーがスクロールすることで、文章・画像・動画・アニメーション・3D表現などが順番に展開され、物語が進んでいくWeb表現です。

単に縦に長いページではなく、スクロールそのものを「ストーリーの進行装置」として使うのが特徴です。

---

## Parallax Scrolling

Parallax Scrollingは、背景・中景・前景などのレイヤーを異なる速度で動かし、奥行きを感じさせる表現です。

たとえば、

```txt
背景画像：ゆっくり動く
中景画像：少し速く動く
前景のテキストやカード：通常速度で動く
```

のようにすることで、平面的なWebページに立体感が生まれます。

---

## Motion Design

Motion Designは、UIやDOM要素に意味のある動きを付ける設計です。

重要なのは、ただ派手に動かすことではありません。

```txt
視線を誘導する
状態変化を伝える
操作結果を伝える
画面の関係性を示す
ブランドの印象を作る
```

このように、動きに役割があることが大切です。

---

## Layered UI / Spatial Design

Layered UIやSpatial Designは、UIを平面ではなく、奥行きのある空間として設計する考え方です。

```txt
背景
↓
装飾
↓
画像
↓
カード
↓
テキスト
↓
ボタン
↓
モーダル
```

このように、要素に前後関係を持たせることで、情報の階層や操作対象が分かりやすくなります。

---

## Elevation

Elevationは、UI要素がどの高さにあるかを表す考え方です。

カード、ボタン、モーダル、ドロップダウンなどを、影・背景・ぼかし・重なりによって「手前にあるもの」として見せます。

```txt
背景：低い
カード：少し浮いている
ボタン：操作対象として目立つ
モーダル：一番手前にある
```

というように、UIの階層を視覚的に伝えます。

---

# 参考になるWebサイト一覧

## 1. Apple Vision Pro

URL：
[https://www.apple.com/apple-vision-pro/](https://www.apple.com/apple-vision-pro/)

学べる要素：

```txt
Spatial Design
Layered UI
Motion Design
Product Storytelling
```

Apple Vision Proのページは、空間性を意識したWeb表現の参考になります。

製品そのものが「空間コンピューティング」をテーマにしているため、ページ全体も奥行きや浮遊感を強く感じる構成になっています。

見るべきポイントは、画像・テキスト・背景の重なり方です。

単に製品写真を大きく見せるのではなく、スクロールに合わせて情報が少しずつ展開され、製品の世界観に引き込まれるようになっています。

---

## 2. Apple AirPods Pro

URL：
[https://www.apple.com/airpods-pro/](https://www.apple.com/airpods-pro/)

学べる要素：

```txt
Scrollytelling
Scroll Animation
Motion Design
Product Storytelling
```

AirPods Proのページは、製品LPにおけるスクロール演出の参考になります。

製品画像、音の波紋、機能説明などが、スクロールに合わせて自然に展開されます。

特に参考になるのは、**製品の特徴を文章で説明しすぎず、ビジュアルとモーションで理解させている点**です。

スクロールするたびに、

```txt
機能が見える
体験が想像できる
製品の魅力が分かる
```

という流れになっています。

---

## 3. Stripe

URL：
[https://stripe.com/](https://stripe.com/)

学べる要素：

```txt
Layered UI
Elevation
Motion Design
SaaS Design
```

Stripeは、SaaS系Webサイトのデザインで非常に参考になります。

派手なパララックスというより、情報量の多いサービスを美しく整理するレイヤー設計が優れています。

見るべきポイントは、

```txt
グラデーション背景
カードUI
プロダクト画面の重ね方
図版とテキストのバランス
CTAの見せ方
```

です。

Stripeのようなサービスは、説明すべき情報が多いです。
しかし、カードや図版をうまく重ねることで、情報量が多くても重く見えない構成になっています。

---

## 4. Linear

URL：
[https://linear.app/](https://linear.app/)

学べる要素：

```txt
Elevation
Layered UI
Product UI
Dark UI
```

Linearは、WebアプリやSaaSの見せ方として非常に参考になります。

特に、黒背景の上にUIカードやプロダクト画面を浮かせる設計が美しいです。

見るべきポイントは、

```txt
背景とUIのコントラスト
カードの浮かせ方
実際のアプリ画面の見せ方
余白の取り方
テキストの情報階層
```

です。

派手に動かすというより、プロダクトUI自体を主役にして、美しく見せるタイプのデザインです。

---

## 5. Lusion

URL：
[https://lusion.co/](https://lusion.co/)

学べる要素：

```txt
3D
Motion Design
Interactive Web
Scrollytelling
```

Lusionは、3D・モーション・インタラクティブ表現を強く使ったWebサイトです。

通常の企業サイトやLPというより、Webそのものを体験コンテンツに近づけているタイプです。

見るべきポイントは、

```txt
3Dオブジェクトの使い方
マウス操作への反応
スクロールと空間演出
モーションの気持ちよさ
```

です。

かなり高度な表現ですが、Webサイトに没入感を出す考え方として参考になります。

---

## 6. The New York Times “Snow Fall”

URL：
[https://www.nytimes.com/projects/2012/snow-fall/index.html](https://www.nytimes.com/projects/2012/snow-fall/index.html)

学べる要素：

```txt
Scrollytelling
Narrative Design
Editorial Design
```

Snow Fallは、Scrollytellingの代表例としてよく紹介されるWebコンテンツです。

長文記事、写真、動画、図解、アニメーションを組み合わせ、スクロールしながら物語を読み進める構成になっています。

見るべきポイントは、情報の出し方です。

```txt
文章
↓
写真
↓
映像
↓
図解
↓
また文章
```

というように、ユーザーが飽きずに読み進められるように設計されています。

ブログやメディア記事、特集ページを作る場合に参考になります。

---

## 7. The Boat

URL：
[https://www.sbs.com.au/theboat/](https://www.sbs.com.au/theboat/)

学べる要素：

```txt
Scrollytelling
Motion Design
Sound Design
Immersive Web
```

The Boatは、スクロール・音・アニメーション・イラストを組み合わせた没入型のストーリーコンテンツです。

通常のWebサイトというより、Web上で読むインタラクティブな物語に近いです。

見るべきポイントは、

```txt
スクロールによる場面転換
音と動きの組み合わせ
イラストのレイヤー感
読者を物語に引き込む演出
```

です。

Scrollytellingを「情報整理」ではなく「体験」として使う場合に参考になります。

---

## 8. NASA Eyes

URL：
[https://science.nasa.gov/eyes/](https://science.nasa.gov/eyes/)

学べる要素：

```txt
Scrollytelling
3D
Interactive Design
Educational Design
```

NASA Eyesは、宇宙や地球観測をインタラクティブに学べるWebコンテンツです。

3D表現とスクロールによる説明が組み合わさっていて、教育系・データビジュアライゼーション系の参考になります。

見るべきポイントは、

```txt
3Dモデルを使った理解促進
スクロールによる説明の流れ
難しい情報を視覚的に伝える工夫
```

です。

技術系・教育系・データ系のサイトを作る場合に参考になります。

---

## 9. The Pudding

URL：
[https://pudding.cool/](https://pudding.cool/)

学べる要素：

```txt
Scrollytelling
Data Visualization
Interactive Article
```

The Puddingは、データビジュアライゼーション型のScrollytellingで有名なサイトです。

スクロールに合わせてグラフや図が変化し、データの意味が少しずつ理解できるようになっています。

見るべきポイントは、

```txt
データを一気に見せない
スクロールに合わせて理解を進める
グラフと文章を連動させる
```

です。

データを扱う記事、分析レポート、調査コンテンツを作る場合に非常に参考になります。

---

## 10. Bruno Simon Portfolio

URL：
[https://bruno-simon.com/](https://bruno-simon.com/)

学べる要素：

```txt
Spatial Design
3D
Interactive Web
Motion Design
```

Bruno Simonのポートフォリオは、Webサイト全体を3D空間として作っている有名な例です。

車を操作して、ポートフォリオ内を移動するような体験になっています。

見るべきポイントは、

```txt
Webサイトを空間として扱っている
ユーザー操作が体験そのものになっている
ポートフォリオをゲーム的に見せている
```

です。

一般的なWebサイトにはそのまま使いにくいですが、Spatial Designやインタラクティブ表現を学ぶには非常に参考になります。

---

## 11. Jitter

URL：
[https://jitter.video/](https://jitter.video/)

学べる要素：

```txt
Motion Design
Layered UI
Animation UI
```

JitterはモーションデザインツールのWebサイトです。

そのため、サイト自体にもモーションの考え方がよく反映されています。

見るべきポイントは、

```txt
文字の動かし方
UIパーツのアニメーション
カードやテンプレートの見せ方
グラデーション・ブラー・影の使い方
```

です。

UIに軽やかな動きを入れたい場合に参考になります。

---

## 12. Framer

URL：
[https://www.framer.com/](https://www.framer.com/)

学べる要素：

```txt
Motion Design
Layered UI
Web App Design
No-code Website Design
```

FramerはWeb制作ツールですが、公式サイト自体もかなり洗練されています。

見るべきポイントは、

```txt
スクロール中の要素の出し方
カードの重ね方
プロダクト画面の見せ方
CTAの配置
余白とタイポグラフィ
```

です。

Web制作ツール、SaaS、スタートアップ系LPを作るときに参考になります。

---

# 追加で参考サイトを探せるギャラリー

## Awwwards Parallax Collection

URL：
[https://www.awwwards.com/websites/parallax/](https://www.awwwards.com/websites/parallax/)

Parallax Scrollingを使ったWebサイトを探すなら、Awwwardsのパララックスカテゴリが便利です。

最新のデザイン事例も見つけやすいです。

---

## Awwwards Scrolling Websites

URL：
[https://www.awwwards.com/websites/scrolling/](https://www.awwwards.com/websites/scrolling/)

スクロール演出が強いサイトを探すなら、このカテゴリが参考になります。

ScrollytellingやScroll Animationを使ったサイトを探したいときに便利です。

---

## Awwwards Motion Websites

URL：
[https://www.awwwards.com/websites/motion/](https://www.awwwards.com/websites/motion/)

Motion Designを強く使っているサイトを探せます。

DOMアニメーション、3D、WebGL、スクロール連動演出などの参考になります。

---

## One Page Love Parallax Collection

URL：
[https://onepagelove.com/tag/parallax-scrolling](https://onepagelove.com/tag/parallax-scrolling)

1ページ完結型のパララックスLPを探すなら、One Page Loveも便利です。

LP制作の参考にしやすいサイトが多く掲載されています。

---

## Webflow Scrollytelling

URL：
[https://webflow.com/made-in-webflow/scrollytelling](https://webflow.com/made-in-webflow/scrollytelling)

Webflowで作られたScrollytellingサイトを探せます。

ノーコード寄りの実装例を見たい場合に参考になります。

---

## Webflow Scroll Animation

URL：
[https://webflow.com/made-in-webflow/scroll-animation](https://webflow.com/made-in-webflow/scroll-animation)

スクロールアニメーションの実例を探すのに便利です。

Webflowで実装されたサイトが多いため、構成やアニメーションの考え方を学びやすいです。

---

# 実際に見るときのチェックポイント

これらのサイトを見るときは、ただ「かっこいい」で終わらせないことが大切です。

以下の視点で見ると、実務に落とし込みやすくなります。

## 1. 何が主役かを見る

まず、そのページの主役を確認します。

```txt
商品なのか
ストーリーなのか
データなのか
ブランドの世界観なのか
アプリ画面なのか
```

主役が明確なサイトほど、デザインが美しく見えます。

---

## 2. レイヤー構造を見る

画面を次のように分解して見ます。

```txt
背景
中景
前景
操作要素
```

たとえばAppleやStripeのサイトでは、背景・画像・テキスト・ボタンがきれいに分離されています。

奥行きのあるサイトは、情報の重なり方が整理されています。

---

## 3. スクロールの役割を見る

スクロール演出を見るときは、次のように考えます。

```txt
ただ動いているだけか
情報理解を助けているか
視線誘導になっているか
ストーリーが進んでいるか
```

良いスクロール演出は、ユーザーの理解を助けます。

悪いスクロール演出は、ただ邪魔になります。

---

## 4. 文字が読めるかを見る

どれだけモーションや3Dが美しくても、文字が読みにくければUIとしては弱いです。

```txt
見出しは目に入るか
本文は読めるか
CTAは見つけやすいか
背景と文字のコントラストは十分か
```

ここを見ると、見た目だけではなく実用性も判断できます。

---

## 5. CTAが邪魔されていないかを見る

Webサイトでは、最終的にユーザーに行動してもらう必要があります。

```txt
購入する
登録する
問い合わせる
資料請求する
アプリを試す
```

このようなCTAが、演出に埋もれていないかを見ることが大切です。

美しいサイトほど、CTAは派手すぎず、でも確実に見つけられる位置にあります。

---

# 自分のWeb制作に落とし込むなら

実際に自分のWebサイトやアプリに取り入れるなら、いきなり派手な3Dや複雑なパララックスを入れる必要はありません。

まずは次のような小さな表現から始めるのがおすすめです。

## 1. 背景・中景・前景を分ける

```txt
背景：グラデーションや写真
中景：装飾・図形・商品画像
前景：見出し・本文・ボタン
```

これだけでも、平面的なサイトに奥行きが出ます。

---

## 2. スクロールで少しだけ動かす

すべての要素を動かす必要はありません。

```txt
背景だけゆっくり動かす
画像だけ少し遅れて表示する
カードだけふわっと出す
CTAは固定して安定させる
```

このくらいで十分です。

---

## 3. ボタンやカードにElevationをつける

```css
.card {
  border-radius: 16px;
  background: #fff;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
}

.button {
  border-radius: 999px;
  padding: 12px 20px;
}
```

影や角丸を少し使うだけで、操作対象が分かりやすくなります。

ただし、影を強くしすぎると古く見えるので注意です。

---

## 4. モーションには意味を持たせる

アニメーションを入れるときは、必ず次のように考えます。

```txt
この動きは何を伝えるためのものか？
ユーザーの理解を助けているか？
操作の邪魔になっていないか？
```

意味のない動きは、かっこよく見えてもユーザー体験を悪くすることがあります。

---

# 注意点

ScrollytellingやParallax、Motion Designはとても魅力的ですが、使いすぎると逆効果です。

特に注意したいのは以下です。

```txt
ページが重くなる
スマホで見づらくなる
スクロールが不自然になる
文字が読みにくくなる
CTAが見つけにくくなる
アクセシビリティが下がる
```

美しいWebサイトを作るには、動かすことよりも、**動かす理由**が大切です。

---

# まとめ

今回紹介したサイトは、以下の考え方を学ぶのに役立ちます。

```txt
Scrollytelling
Parallax Scrolling
Motion Design
Layered UI / Spatial Design
Elevation
```

特におすすめの見方は、以下です。

```txt
Apple系：製品を美しく見せる型
Stripe / Linear：SaaSやWebアプリを美しく見せる型
The Boat / Snow Fall：物語を体験化する型
NASA / The Pudding：データや知識を分かりやすく見せる型
Lusion / Bruno Simon：Webを空間や体験として扱う型
```

Webデザインに物語性や奥行きを持たせると、単なる情報ページではなく、ユーザーの記憶に残る体験になります。

ただし、大切なのは派手に動かすことではありません。

```txt
背景は世界観を作る
画像は理解を助ける
テキストは情報を伝える
ボタンは行動を促す
モーションは視線を導く
```

この役割分担ができていると、ScrollytellingやMotion Designはとても効果的に機能します。

美しいWebサイトは、見た目が派手なサイトではありません。

**情報・空間・動き・操作が自然につながっているサイト。**

それが、ユーザーにとって本当に心地よいWeb体験だと思います。

```
