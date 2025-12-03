---
title: "【初心者向け】Firebase App Check + reCAPTCHA v3でDDoS攻撃からアプリを守る方法"
emoji: "🛡️"
type: "tech"
topics: ["firebase", "security", "recaptcha", "appcheck", "初心者"]
published: true
---

# 【初心者向け】Firebase App Check + reCAPTCHA v3でDDoS攻撃からアプリを守る方法

## はじめに

個人開発でWebアプリを公開すると、「APIキーを抜かれて不正アクセスされないか」「DDoSで従量課金が跳ね上がらないか」といった不安は避けられません。Firebaseでは `apiKey` や `projectId` をフロントエンドに埋め込むため、ブラウザの開発者ツールから誰でも参照できてしまいます。本記事では、**Firebase App Check** と **reCAPTCHA v3** を組み合わせて、こうしたリスクを最小化するための考え方と実装手順を初心者向けに解説します。

## なぜ対策が必要なのか？

悪意ある第三者がAPIキーを用いて自動リクエストを投げると、次のような問題が起こります。

- FirestoreやStorageのリクエスト数が急増し、課金が爆発する
- 無料枠を使い切り、正規ユーザーのリクエストが拒否される
- RTDBやFunctions経由でスパム的な更新が入り、サービス品質が低下する

App Checkは「正規アプリからのアクセスだけをFirebaseリソースに通す」認証レイヤーです。reCAPTCHA v3をプロバイダに設定することで、**人間らしさをスコア化しながら自動的にトークンを発行**し、App Checkがそのトークンを検証して安全性を担保します。従来の「信号機を選ぶ」ようなUIはなく、ユーザー体験を壊さないのが特徴です。

## 仕組み：2つのガードマンで守る

1. **reCAPTCHA v3（監視役）**: アクセス元の挙動をスコア化し、証明書（トークン）を発行。
2. **App Check（門番）**: Firebaseへのリクエストにトークンが添付されているか、改ざんされていないかを検証。

この2段構えにより、トークンが取得できない環境（curlやbot）からのアクセスは原則拒否されます。

## 実装ステップ

以下では、Firebase v9（Modular SDK）を利用したWebアプリを想定します。

### 手順1：reCAPTCHA v3のキーを取得する

1. [reCAPTCHA Admin Console](https://www.google.com/recaptcha/admin/create) にアクセス
2. サイト登録フォームで以下を設定
   - **ラベル**: 自身が識別しやすい名前
   - **reCAPTCHAタイプ**: `reCAPTCHA v3`
   - **ドメイン**: 本番ドメイン（例: `myapp.com`）＋ 開発用に `localhost`
3. 登録後に表示される **サイトキー（公開）** と **シークレットキー（非公開）** を控える

### 手順2：FirebaseコンソールでApp Checkを設定

1. Firebaseコンソール左メニューから **App Check** を開き「始める」
2. 対象のWebアプリを選び、プロバイダに **reCAPTCHA v3** を指定
3. 取得したシークレットキーを入力して保存
4. この時点では「適用（Enforce）」せず、まずはメトリクスを観察するのが無難です

### 手順3：フロントエンドでApp Checkを初期化

```javascript
// firebase.js
import { initializeApp } from "firebase/app";
import { initializeAppCheck, ReCaptchaV3Provider } from "firebase/app-check";

const firebaseConfig = {
  apiKey: "...",
  authDomain: "...",
  projectId: "...",
  // ...
};

const app = initializeApp(firebaseConfig);

if (typeof window !== "undefined") {
  // ローカル開発でのデバッグトークン（本番では無効）
  self.FIREBASE_APPCHECK_DEBUG_TOKEN = process.env.NODE_ENV === "development";

  const appCheck = initializeAppCheck(app, {
    provider: new ReCaptchaV3Provider("ここにサイトキー"),
    isTokenAutoRefreshEnabled: true,
  });
}
```

- `initializeAppCheck` はブラウザ環境のみで呼び出します（SSRではガード条件必須）
- `isTokenAutoRefreshEnabled` を有効にするとトークンを自動更新し、長時間のセッションでも安全性を維持できます

### 手順4：ローカル開発でデバッグトークンを登録

1. `self.FIREBASE_APPCHECK_DEBUG_TOKEN = true;` としてアプリを起動
2. ブラウザコンソールに表示される `App Check debug token: "xxxx"` をコピー
3. Firebaseコンソール > App Check > 対象アプリ > **デバッグトークンの管理** に貼り付けて保存
4. 登録済みマシンからのアクセスのみ「特例」として許可されるため、CIや他開発者が増えたらトークンを個別発行しましょう

## 運用開始：Enforce（強制適用）までの流れ

1. 実装後しばらくは **メトリクス** をウォッチし、「未確認のトラフィック」が減っているか確認
2. すべてのクライアントバージョンがApp Check対応していることを確認
3. 問題がなければ「適用（Enforce）」をオンにして未検証アクセスを完全遮断
4. Cloud Logging や BigQuery Export を併用し、異常トラフィックの兆候を継続監視するとなお安心

## 料金のアップデート（2025年時点）

- **Firebase App Check**: 利用自体は無料
- **reCAPTCHA v3**: 2024年8月以降、無料枠が **月間1万回（Essentialsプラン）** までに縮小。超過すると課金もしくは応答停止があり得ます
- アクセス数が多い場合は、Cloudflare Turnstileなど無料枠が広い代替プロバイダをカスタムで利用する選択肢も検討してください

## よくあるつまずきと対策

| 症状 | 主な原因 | 対策 |
| ---- | ---- | ---- |
| ローカルでreCAPTCHAが失敗 | `localhost` をドメインに登録していない | Admin Consoleで追加登録し、デバッグトークンを使う |
| 旧バージョンのアプリがアクセスに失敗 | App Check非対応のコードがまだ動いている | リリースノートで告知し、段階的ロールアウトにする |
| 未確認トラフィックが減らない | `initializeAppCheck` の呼び出し漏れやSSRとの競合 | ブラウザ判定と依存パッケージの整合性を再確認 |

## まとめ

- APIキーが公開されていても、**App Check + reCAPTCHA v3** で正規トラフィックだけを通過させられる
- 導入ステップは「reCAPTCHAキー取得」「FirebaseでApp Check設定」「フロントで初期化」「デバッグトークン登録」の4段階
- 運用では **メトリクス監視 → Enforce** の順に進め、安全性と可用性を両立
- 2024年以降は **reCAPTCHA v3の無料枠が月1万回** とタイトなので、アクセス規模に応じたプラン選択が重要

転ばぬ先の杖として、個人開発でもぜひ今日から導入してみてください！

## 参考リンク

- [Firebase公式: App Check × reCAPTCHA Webガイド（日本語）](https://firebase.google.com/docs/app-check/web/recaptcha-provider?hl=ja)
- [Firebase公式: App Check × reCAPTCHA Webガイド（英語）](https://firebase.google.com/docs/app-check/web/recaptcha-provider)
- [irohani note: reCAPTCHA無料枠変更まとめ](https://irohani-note.blog/recaptcha-limit/)
- [Qiita: reCAPTCHA v3設定手順（s_satoh）](https://qiita.com/s_satoh/items/a949f52fa89ac368aad5)
- [Datum Studio: Firebase App Check導入記](https://datumstudio.jp/blog/1115_firebase_app_check/)
- [Qiita: App Check + reCAPTCHA v3導入メモ（yuta-katayama-23）](https://qiita.com/yuta-katayama-23/items/e071e167caef2e2f780e)
