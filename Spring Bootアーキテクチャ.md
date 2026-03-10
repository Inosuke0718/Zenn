---
title: "【Spring Boot】3層アーキテクチャって何？ MVCとの関係をスッキリ図解！"
emoji: "🍃"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ["springboot", "java", "architecture", "mvc"]
published: false
---

Spring Bootを学び始めると、必ずと言っていいほど「 **3層アーキテクチャ** 」という言葉に出会いますよね。

「Controllerはわかるけど、ServiceとRepositoryってどう違うの？」
「全部Controllerに書いちゃダメなの？」
そんな風に迷う瞬間、ありませんか？

今回は、Spring Bootの基本的な考え方である「レイヤー構造」と、おなじみの「MVC」の関係を、初心者の方でも直感的に理解できるように整理してみました！

## 🏗️ ひと目でわかる！Spring Bootの全体像

まずは、リクエストがどのように処理されていくか、図で確認してみましょう。

![Spring Boot Architecture](https://github.com/Inosuke0718/Zenn/blob/main/images/spring-boot-architecture.png?raw=true)

このように、Spring Bootでは処理の種類によって「居場所」が決まっているんです。

## 🤝 MVCと各レイヤーの関係

「MVC（Model-View-Controller）」は、アプリを **役割別** に分ける伝統的な考え方です。
Spring Bootでは、特に「Model（データと処理）」が大きくなりやすいため、さらに細かく「Service」と「Repository」に分割して整理します。

| MVCの概念      | Spring Bootのレイヤー        | 役割のイメージ                                                                |
| :------------- | :--------------------------- | :---------------------------------------------------------------------------- |
| **View**       | **View層（またはフロント）** | **【画面】** ユーザーが目にする部分。HTMLやJSON。                             |
| **Controller** | **Controller層**             | **【受付窓口】** リクエストを受け取り、適切な「Service」へ案内する。          |
| **Model**      | **Service層**                | **【頭脳（ロジック）】** 複雑な計算、条件分岐、チェックなどの業務処理を行う。 |
| **Model**      | **Repository層**             | **【倉庫番】** データベース（DB）への保存や検索だけを専門に行う。             |

## 🤔 なぜわざわざ「3層」に分けるの？

「全部Controllerに書いたほうが楽じゃない？」と思うかもしれません。しかし、すべての処理を1ヶ所に詰め込むと、コードが長くなりすぎて「どこで何をしているか」が全くわからなくなってしまいます（これが有名な「ファットコントローラー」問題です）。

役割を分けることで、こんな **ハッピーなメリット** があります！

1. ⚙️ **テストがしやすい**
   - 「計算ロジック（Service）だけテストしたい」といったことが簡単にできます。
2. 🛠️ **変更に強い**
   - 「データベースの種類を変えたい」と思っても、直すのは「Repository層」だけで済みます。
3. 🤝 **チーム開発がスムーズ**
   - 「どこに何を書くか」のルールが明確なので、複数人で書いてもコードが綺麗に保たれます。

## 📦 データの運び屋たち（Form / DTO / Entity）

各レイヤー間をデータが移動するとき、Spring Bootでは専用の「データの運び屋（箱）」を使い分けるのがお作法です。

- ✉️ **Form（フォーム）**
  - **View ↔ Controller**
  - ユーザーが画面に入力したデータをそのまま受け取る箱です。
- 📦 **DTO（Data Transfer Object）**
  - **Controller ↔ Service**
  - レイヤー間でデータをやり取りするための、いわば「整理整頓された箱」です。
- 📑 **Entity（エンティティ）**
  - **Service ↔ Repository**
  - データベースのテーブル構成をそのまま映し出した「DB専用の箱」です。

## 🏁 まとめ

Spring Bootのアーキテクチャは、「誰が何を担当するか」を明確にするためのガイドラインです。

- **Controller** は受付。
- **Service** は頭脳。
- **Repository** は倉庫番。

まずはこの3つの役割を意識することから始めてみましょう！

「今はSpring Bootで画面も一緒に作っていますか？ それともReactなどを使ってAPIサーバーとして開発していますか？」
環境に合わせて、最適な実装方法も変わってきます。ぜひ、プロジェクトに合わせた設計を試してみてください！

---

### 📚 参考資料

- [Spring Boot Architecture - Tech Adseed](https://tech.adseed.co.jp/spring-boot-architecture)
- [Spring Bootのレイヤー構造について - Qiita](https://qiita.com/yut-nagase/items/039a1eb3108926c232a7)
- [Controller・Service・Repositoryの責務 - Qiita](https://qiita.com/yu-F/items/1e1b009fa248af9498e1)
- [Repository層とEntityの役割 - Smallit Blog](https://smallit.co.jp/blog/a2517/)
