---
title: "【Java入門】Windows環境構築！JDKのインストールから環境変数の設定まで"
emoji: "☕"
type: "tech"
topics: ["java", "jdk", "windows", "環境構築", "初心者"]
published: true
---

これから Java を学習しようとしている皆さん、「環境構築」でつまづいていませんか？

「インストーラーを実行したのに動かない…」
「環境変数って何？パスを通すってどういうこと？」

そんな悩みを持つ方のために、今回は Windows における**JDK（Java Development Kit）のインストール方法**を、画像付きでステップバイステップ解説します。
ついでに、多くの人が苦戦する「環境変数の設定」もしっかりカバーしますので、一緒にやっていきましょう！

## 📦 JDK のダウンロードとインストール

まずは JDK のインストーラーをダウンロードして実行しましょう。
Oracle の公式サイトや OpenJDK のサイトから、用途に合ったバージョンをダウンロードしてください。
（学習用であれば、個人的に 21 がおすすめです）

https://www.oracle.com/jp/java/technologies/downloads/#java21

インストーラーを起動すると、以下のような画面が表示されます。

![](https://github.com/Inosuke0718/Zenn/blob/main/images/java-set-up/jdk%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB.png?raw=true)

基本的には「次へ（Next）」をクリックしてデフォルト設定のまま進めていけば OK です。
インストール先（例: `C:\Program Files\Java\jdk-xx`）は後で使うので、心の片隅に留めておいてくださいね。

## ⚙️ 環境変数の設定

インストールが終わったら、Windows に「Java はここにあるよ！」と教えてあげる作業が必要です。これが**環境変数の設定**です。

### 1. 環境変数の設定画面を開く

まずは Windows の検索バー（スタートメニュー）に「環境変数」と入力し、「システム環境変数の編集」を開きます。

![](https://github.com/Inosuke0718/Zenn/blob/main/images/java-set-up/variables1.png?raw=true)

すると、「システムのプロパティ」という小難しい画面が出てきますが、怖がることはありません。
右下にある**「環境変数(N)...」**というボタンをクリックしてください。

![](https://github.com/Inosuke0718/Zenn/blob/main/images/java-set-up/variables2.png?raw=true)
![](https://github.com/Inosuke0718/Zenn/blob/main/images/java-set-up/variables3.png?raw=true)

### 2. JAVA_HOME の作成

次に、Java のインストール場所を示す `JAVA_HOME` という変数を作ります。
「システム環境変数(S)」の方にある**「新規(W)...」**ボタンをクリックします。

![](https://github.com/Inosuke0718/Zenn/blob/main/images/java-set-up/variables4.png?raw=true)

新しいユーザー変数（またはシステム変数）の入力画面が出たら、以下のように入力します。

- **変数名**: `JAVA_HOME`
- **変数値**: JDK をインストールしたフォルダのパス（例: `C:\Program Files\Java\jdk-21\bin` など）

![](https://github.com/Inosuke0718/Zenn/blob/main/images/java-set-up/variables5.png?raw=true)

入力できたら「OK」を押して保存します。

### 3. Path の設定（パスを通す）

最後に、どのフォルダからでも `java` コマンドを使えるように、`Path` を編集します。
システム環境変数の一覧から **`Path`** を探して選択し、**「編集(I)...」**ボタンをクリックします。

![](https://github.com/Inosuke0718/Zenn/blob/main/images/java-set-up/variables6.png?raw=true)

環境変数名の編集画面が開いたら、右上の**「新規(N)」**をクリックし、以下を追加します。

```text
%JAVA_HOME%\bin
```

![](https://github.com/Inosuke0718/Zenn/blob/main/images/java-set-up/variables7.png?raw=true)

これは「さっき作った `JAVA_HOME` の中にある `bin` フォルダを参照してね」という意味です。
入力が終わったら、開いている全てのウィンドウで「OK」を押して閉じてください。

## ✅ 動作確認

最後に、正しくインストールできたか確認しましょう。
コマンドプロンプト（または PowerShell）を新しく開き、以下のコマンドを入力します。

```bash
java -version
```

以下のようにバージョン情報が表示されれば大成功です！🎉

![](https://github.com/Inosuke0718/Zenn/blob/main/images/java-set-up/java-v.png?raw=true)

もしエラーが出る場合は、コマンドプロンプトを再起動するか、パスの設定が間違っていないかもう一度確認してみてください。

## まとめ

お疲れ様でした！これで Java の開発を始める準備が整いました。

- **JDK のインストール**: インストーラーに従って入れるだけ！
- **JAVA_HOME**: インストール場所を教える変数
- **Path**: コマンドを使えるようにする設定

環境構築は最初の難関ですが、一度できてしまえばこっちのものです。
さあ、これからの Java ライフを楽しんでくださいね！

---

参考になったら、ぜひ記事への「いいね」をお願いします！
わからないことがあれば、公式ドキュメントもチェックしてみてください。
