---
title: "お名前.comの独自ドメインで無料メールを作る方法【Cloudflare Email Routing + Gmail】"
emoji: "📩"
type: "tech"
topics: ["Cloudflare", "Gmail", "DNS", "メール", "お名前.com"]
published: true
---

# お名前.comで取得した独自ドメインメールを無料で使う方法【Cloudflare Email Routing + Gmail】

## はじめに

独自ドメインを取得すると、次にやりたくなるのが、

```text
info@example.com
contact@example.com
support@example.com
```

のような独自ドメインメールの作成です。

今回は、**お名前.comで取得したドメイン**を使って、できるだけ無料で

```text
info@kiki-neko.com
```

のようなメールアドレスを使えるようにした手順をまとめます。

構成としては、以下のようになります。

```text
受信：
info@独自ドメイン
↓
Cloudflare Email Routing
↓
Gmailに転送

送信：
Gmail
↓
差出人を info@独自ドメイン に切り替えて送信
```

## 今回の構成

今回使ったサービスは以下です。

| 用途       | サービス                     |
| -------- | ------------------------ |
| ドメイン取得   | お名前.com                  |
| DNS管理    | Cloudflare               |
| メール受信・転送 | Cloudflare Email Routing |
| メール送信    | Gmail                    |
| 送信用認証    | Googleアプリパスワード           |

今回の例では、以下のメールアドレスを作成します。

```text
info@kiki-neko.com
```

## この方法は本当に無料なのか？

結論から言うと、**すでにドメインを持っている場合、追加費用は基本的に0円で始められます。**

ただし、完全な意味での無料メールサーバーではありません。

この構成では、

```text
Cloudflare Email Routing：無料
Gmail：無料
Cloudflare DNS：無料
```

を使います。

一方で、以下の費用は別途必要です。

```text
ドメイン取得費用
ドメイン更新費用
```

つまり、すでにドメインを持っていれば、メール機能のために追加で月額費用を払わずに始められる、という意味です。

## 注意点

この方法は、**正式なメールホスティングサービスではありません。**

Cloudflare Email Routingは、基本的にメールを受信して別のメールアドレスへ転送するサービスです。

そのため、

```text
受信：かなり便利
送信：Gmail経由で工夫して送る
```

という構成になります。

業務用として完璧に運用したい場合は、Zoho Mail、Google Workspace、Microsoft 365、お名前メールなどの正式なメールホスティングサービスを使う方が安心です。

## 手順1：Cloudflareにドメインを追加する

まず、Cloudflareにログインしてドメインを追加します。

```text
Cloudflareにログイン
↓
ドメインを追加
↓
お名前.comで取得したドメインを入力
↓
Freeプランを選択
```

Cloudflareにドメインを追加すると、Cloudflare用のネームサーバーが2つ表示されます。

例：

```text
xxxx.ns.cloudflare.com
yyyy.ns.cloudflare.com
```

この2つを控えておきます。

## 手順2：お名前.comでネームサーバーをCloudflareに変更する

次に、お名前.com側でネームサーバーをCloudflareに変更します。

```text
お名前.com Navi
↓
ネームサーバー / DNS
↓
ネームサーバーの変更
↓
対象ドメインを選択
↓
その他のネームサーバーを使う
↓
Cloudflareで表示された2つのネームサーバーを入力
↓
保存
```

これで、ドメインのDNS管理がCloudflare側に移ります。

```text
ドメイン取得：お名前.com
DNS管理：Cloudflare
```

という状態です。

反映には数分〜数時間かかる場合があります。

## 手順3：Cloudflare Email Routingを有効化する

Cloudflareで対象ドメインを開きます。

```text
Cloudflare
↓
対象ドメイン
↓
メールサービス
↓
Email Routing
```

ここで注意したいのが、Cloudflareには似たようなメニューとして、

```text
Email Sending
Email Routing
```

があります。

今回使うのは **Email Routing** です。

| 機能            | 用途                               | 今回使うか |
| ------------- | -------------------------------- | ----- |
| Email Sending | Cloudflare Workersなどからメールを送信する機能 | 使わない  |
| Email Routing | 独自ドメイン宛のメールをGmailなどへ転送する機能       | 使う    |

Email Sendingは有料Workersプランが必要になる場合があります。今回の無料構成では使いません。

## 手順4：不足しているDNSレコードを追加する

Email Routingを有効化すると、DNSレコードの設定画面が表示されます。

そこで、

```text
不足しているレコードを追加
↓
接続
```

を実行します。

これにより、Cloudflare Email Routingに必要なMXレコードやTXTレコードが自動で追加されます。

設定後、画面上で以下のようになっていればOKです。

```text
ステータス：有効
DNSレコード：ロック済み
```

## 手順5：宛先アドレスを追加する

次に、転送先となるGmailアドレスを登録します。

```text
Email Routing
↓
宛先アドレス
↓
宛先アドレスを追加
```

ここに、普段使っているGmailアドレスを入力します。

例：

```text
example@gmail.com
```

追加すると、GmailにCloudflareから確認メールが届きます。
メール内のリンクをクリックして承認します。

これでCloudflareからGmailへ転送できるようになります。

## 手順6：ルーティングルールを作成する

次に、実際に使いたいメールアドレスを作成します。

```text
Email Routing
↓
ルーティングルール
↓
＋ ルーティングルールを作成
```

今回作るのは以下です。

```text
info@kiki-neko.com
```

入力内容は以下のようにします。

```text
メールパターン：
info

ドメイン：
kiki-neko.com

アクション：
メールに送信 / Send to email

宛先：
登録済みのGmailアドレス
```

ここで注意点があります。

メールパターンには、

```text
info@kiki-neko.com
```

ではなく、

```text
info
```

だけを入力します。

これで、

```text
info@kiki-neko.com
↓
Gmailに転送
```

というルーティングが完成します。

## 手順7：受信テストをする

別のメールアドレスから、

```text
info@kiki-neko.com
```

宛にメールを送ってみます。

Gmailに届けば、受信設定は完了です。

## 手順8：Gmailから独自ドメインメールとして送信できるようにする

ここからは、Gmailで

```text
info@kiki-neko.com
```

として送信できるようにします。

Gmailを開いて、以下に進みます。

```text
Gmail
↓
右上の歯車
↓
すべての設定を表示
↓
アカウントとインポート
↓
名前
↓
他のメールアドレスを追加
```

入力内容は以下です。

```text
名前：
任意の名前

メールアドレス：
info@kiki-neko.com

エイリアスとして扱います：
チェックあり
```

次にSMTP設定を行います。

## 手順9：SMTP設定を入力する

SMTP設定では、CloudflareのMXサーバーではなく、GmailのSMTPサーバーを使います。

重要なのはここです。

```text
route3.mx.cloudflare.net
```

のようなCloudflareのMXサーバーは、**受信用のサーバー**です。
Gmailから送信するためのSMTPサーバーではありません。

正しくは以下のように入力します。

```text
SMTPサーバー：
smtp.gmail.com

ポート：
587

ユーザー名：
自分のGmailアドレス

パスワード：
Googleのアプリパスワード

セキュリティ：
TLS
```

## 手順10：Googleアプリパスワードを作成する

SMTP設定のパスワード欄には、普段のGoogleログインパスワードではなく、**Googleのアプリパスワード**を入力します。

アプリパスワードとは、外部アプリやSMTP接続用にGoogleが発行する専用パスワードです。

作成手順は以下です。

```text
Googleアカウント
↓
セキュリティとログイン
↓
2段階認証を有効化
↓
アプリパスワードを作成
```

アプリパスワード画面が見つからない場合は、以下のURLを直接開くと早いです。

```text
https://myaccount.google.com/apppasswords
```

アプリ名は、たとえば以下でOKです。

```text
Gmail SMTP
```

作成すると、16桁程度のパスワードが表示されます。

このパスワードをGmailのSMTP設定画面に貼り付けます。

## 手順11：Gmail側の確認を完了する

SMTP設定後、Gmailが

```text
info@kiki-neko.com
```

宛に確認メールを送信します。

すでにCloudflare Email Routingで、

```text
info@kiki-neko.com
↓
Gmail
```

の設定ができていれば、その確認メールはGmailに届きます。

メール内の確認リンクをクリックするか、確認コードを入力すれば完了です。

完了すると、

```text
Gmailユーザーは info@kiki-neko.com としてメールを送信できるようになりました。
```

のような表示が出ます。

## 手順12：Gmailから送信する

Gmailでメールを作成するときに、差出人を切り替えます。

```text
Gmail
↓
作成
↓
差出人をクリック
↓
info@kiki-neko.com を選択
↓
送信
```

相手には、基本的に以下のように表示されます。

```text
差出人：名前 <info@kiki-neko.com>
```

毎回 `info@kiki-neko.com` から送りたい場合は、Gmailで以下の設定をします。

```text
Gmail
↓
設定
↓
すべての設定を表示
↓
アカウントとインポート
↓
名前
↓
info@kiki-neko.com をデフォルトに設定
```

## 迷惑メールに入る問題

実際にテストしたところ、送信したメールが迷惑メールに入ることがありました。

これは、この無料構成の弱点です。

理由は以下です。

```text
見た目：
info@kiki-neko.com から送信

実際：
GmailのSMTPから送信

Cloudflare：
受信転送のみで、送信サーバーではない
```

つまり、受信側から見ると、

```text
本当に kiki-neko.com から送っているのか？
```

と疑われる場合があります。

その結果、迷惑メールに振り分けられることがあります。

## 迷惑メール対策1：DMARCを追加する

CloudflareのDNSにDMARCレコードを追加します。

```text
Cloudflare
↓
対象ドメイン
↓
DNS
↓
レコード
↓
レコードを追加
```

入力内容は以下です。

```text
タイプ：
TXT

名前：
_dmarc

コンテンツ：
v=DMARC1; p=none; rua=mailto:info@kiki-neko.com

TTL：
自動
```

`_dmarc` と入力すると、実際には以下のレコードになります。

```text
_dmarc.kiki-neko.com
```

最初は `p=none` にして様子を見るのが無難です。

## 迷惑メール対策2：SPFを修正する

次に、SPFレコードを修正します。

Cloudflare Email Routingを設定した時点で、以下のようなTXTレコードが入っている場合があります。

```text
v=spf1 include:_spf.mx.cloudflare.net ~all
```

Gmail経由で送信する場合は、GmailのSPFも含めます。

```text
v=spf1 include:_spf.mx.cloudflare.net include:_spf.google.com ~all
```

注意点として、SPFレコードは複数作らないようにします。

ダメな例：

```text
v=spf1 include:_spf.mx.cloudflare.net ~all
v=spf1 include:_spf.google.com ~all
```

正しい例：

```text
v=spf1 include:_spf.mx.cloudflare.net include:_spf.google.com ~all
```

`v=spf1` から始まるTXTレコードは、基本的に1つだけにします。

## DNS反映の待ち時間

CloudflareのDNS反映は比較的早いです。

目安は以下です。

```text
5〜10分：反映され始めることが多い
30分：だいたい確認できる
1〜2時間：まだ怪しい場合の待機目安
最大24時間：DNS的にはあり得る
```

SPFやDMARCを修正したら、10〜30分ほど待ってから再テストするとよいです。

## この構成が向いているケース

この無料構成は、以下のような用途に向いています。

```text
個人サイトのお問い合わせ用
小規模サービスの連絡先
名刺やWebサイトに info@ を載せたい
たまに返信する程度
できるだけ無料で始めたい
```

## この構成が向いていないケース

一方で、以下のような用途にはあまり向いていません。

```text
営業メールを頻繁に送る
請求書や契約書を送る
初対面の会社に重要メールを送る
絶対に迷惑メールに入ってほしくない
複数人で本格運用する
```

この場合は、正式なメールホスティングサービスを使った方が安心です。

候補としては以下があります。

```text
Zoho Mail Lite
Google Workspace
Microsoft 365
お名前メール
```

## まとめ

今回は、お名前.comで取得した独自ドメインを使って、Cloudflare Email RoutingとGmailで独自ドメインメールを使う方法をまとめました。

最終構成は以下です。

```text
受信：
info@kiki-neko.com
↓
Cloudflare Email Routing
↓
Gmail

送信：
Gmail
↓
差出人を info@kiki-neko.com に切り替えて送信
```

この方法なら、すでにドメインを持っていれば追加費用なしで始められます。

ただし、送信に関してはGmail経由になるため、迷惑メールに入る可能性があります。
SPFやDMARCを設定することで多少改善できますが、完全に解決できるとは限りません。

本格的な業務メールとして使う場合は、Zoho Mail Liteなどの正式なメールホスティングサービスを検討した方が安心です。

必要なら、このあと **Zenn向けにタイトル・emoji・topics・記事冒頭のFront Matter** まで付けた形式にもできます。
