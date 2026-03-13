---
title: "【JSP & Servlet】Eclipseで爆速！Web開発の初期設定と動作確認の完全ガイド"
emoji: "🚀"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ["java", "eclipse", "jsp", "servlet", "tomcat"]
published: false
---

![アイキャッチ](https://github.com/Inosuke0718/Zenn/blob/main/images/eclipse-jsp-servlet-eyecatch.png?raw=true)

JavaでのWeb開発を学び始めたばかりの皆さん、開発環境を整えた後に「さて、どうやって動かせばいいんだ……？」と迷ったことはありませんか？

Eclipse（特にPleiades All in One）を使えば、JSPやサーブレットの動作確認は驚くほど簡単です。
今回は、最小構成で **JSPとサーブレットを連携させて動かす方法** を、現役講師がステップバイステップで優しく解説しますね！

## 🛠️ 開発環境の準備

まずは、Java Web開発に欠かせないツールを確認しましょう。

- **Eclipse IDE** （Enterprise Java and Web Developers 版）
- **Apache Tomcat** （実行用サーバー）

Pleiades All in One を使っている方は、これらが最初からセットになっているので安心してください。
Eclipseはソースコードを書くだけでなく、Tomcatと連携して **自動的にサーバーへデプロイ** してくれる頼もしい相棒です。

---

## 📁 ステップ1：プロジェクトの作成

まずは、Webプロジェクトの箱を作るところからスタートです。

1. Eclipseのメニューから `ファイル` > `新規` > `その他` を選択します。
2. `Web` フォルダの中にある **「動的Webプロジェクト（Dynamic Web Project）」** を選んで `次へ` 。
3. プロジェクト名（例： `HelloWeb` ）を入力します。
4. **ターゲット・ランタイム** に「Apache Tomcat」が指定されていることを確認して `完了` をクリック！

これで、JavaコードやJSPを配置するためのディレクトリ構造が自動的に生成されました。

---

## ☕ ステップ2：サーブレットの実装

次に、バックエンドの司令塔となる **サーブレット** を作成しましょう。
サーブレットは、ブラウザからのリクエストを受け取って、データを処理する役割を持ちます。

1. `Javaリソース/src` （または `src/main/java` ）を右クリックして `新規` > `サーブレット` を選択。
2. クラス名（例： `HelloServlet` ）を入力して `作成` 。

コードを以下のように書き換えてみてください。

```java:HelloServlet.java
import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

// このアノテーションでアクセスURLを指定します
@WebServlet("/hello")
public class HelloServlet extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response) 
            throws ServletException, IOException {
        
        // リクエストスコープに「message」という名前でデータをセット
        request.setAttribute("message", "Hello from Servlet!");
        
        // 表示担当のJSP（index.jsp）にバトンタッチ（フォワード）
        request.getRequestDispatcher("/index.jsp").forward(request, response);
    }
}
```

**重要** : `@WebServlet("/hello")` というアノテーションを使うことで、複雑な設定ファイル（ `web.xml` ）を書かずにURLマッピングができるようになります。便利ですよね！

---

## 📄 ステップ3：JSPファイルの作成

今度は、ユーザーのブラウザに表示される画面（ビュー）となる **JSP** を作成します。

1. `WebContent` （または `src/main/webapp` ）フォルダを右クリック。
2. `新規` > `JSPファイル` を選択。
3. ファイル名を `index.jsp` にして `完了` 。

中身を以下のように記述しましょう。

```html:index.jsp
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>JSP & Servlet Test</title>
</head>
<body>
    <h2>🚀 動作確認テスト</h2>
    <!-- サーブレットから渡されたメッセージをEL式で表示 -->
    <p>Message: ${message}</p>
</body>
</html>
```

ここで使っている `${message}` は **EL式** と呼ばれるもので、サーブレットから渡されたデータを簡単に取り出すことができます。

---

## 🏃 ステップ4：サーバーでの実行

いよいよ動かしてみましょう！

1. 作成した `HelloServlet.java` を右クリック。
2. `実行(R)` > **「1 サーバーで実行」** を選択。
3. 使用するTomcatサーバーを選んで `完了` をクリック。

コンソールにログが流れ、しばらくするとEclipse内のブラウザが自動的に開きます。
URLの末尾が `/hello` になっていて、 **「Message: Hello from Servlet!」** と表示されれば大成功です！ 🎉

---

## 💡 まとめ

お疲れ様でした！JSPとサーブレットの基本サイクルは理解できましたか？

- **動的Webプロジェクト** を作成して土台を作る
- **Servlet** でリクエストを受け取り、データをセットする
- **JSP** でデータを動的に受け取って表示する
- **サーバーで実行** を使ってTomcatを起動する

これがJava Web開発の **ベストプラクティス** な基本形です。
次は、データベース（MySQLなど）と連携させて、より本格的なアプリ作りに挑戦してみましょう！

もしエラーが出た時は、コンソールの赤い文字をじっくり読んでみてください。解決のヒントが必ず隠れていますよ。

もっと詳しく知りたい方は、 [公式ドキュメント](https://tomcat.apache.org/) も覗いてみてくださいね！
