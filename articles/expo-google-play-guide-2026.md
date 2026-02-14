---
title: "【2026年版】Expo React NativeアプリをGoogle Play Storeに公開する完全ガイド"
emoji: "🚀"
type: "tech"
topics: ["reactnative", "expo", "android", "googleplay", "eas"]
published: false
---

# はじめに

この記事では、Expo（EAS）で作成したReact NativeアプリをGoogle Play Storeに公開するまでの全工程を、初心者向けに詳しく解説します。

この記事を読むと、以下のことができるようになります：

- EASを使ってAndroid向けプロダクションビルドを作成
- Google Play Consoleでアプリを登録
- 自動提出の仕組みを構築
- 審査に通りやすいストアリスティングを作成

## 前提条件

作業を始める前に、以下を用意してください：

- **Google Play Developer Account**（登録料25ドルが必要）
- **Expo アカウント**（無料）
- **開発済みのExpo/React Nativeアプリ**
- **Node.js と npm/yarn がインストール済みの環境**

:::message
Google Play Developer Accountの登録には本人確認が必要で、承認まで数日かかる場合があります。早めに登録しておきましょう。
:::

---

# 全体の流れ

公開までの大まかなステップは以下の通りです：

1. Google Cloudでサービスアカウントを作成
2. サービスアカウントをGoogle Play Consoleに紐付け
3. EAS CLIをセットアップ
4. Androidプロダクションビルドを作成
5. Google Play Consoleでアプリ情報を登録
6. 内部テスト → 本番リリースを作成
7. 自動提出の設定（オプション）

それでは、順番に見ていきましょう。

---

# Step 1: Google Service Accountの作成

Google Service Accountは、EASから自動的にビルドを提出するための「技術的な窓口」です。

## 1-1. Google Cloud Consoleでプロジェクトを作成

1. [Google Cloud Console](https://console.cloud.google.com/)にアクセス
2. 新規プロジェクトを作成（例: `my-expo-app`）

## 1-2. Google Play Android Developer APIを有効化

1. 検索バーで「Google Play Android Developer API」を検索
2. 「有効にする」をクリック

## 1-3. サービスアカウントを作成

1. 左メニューから **IAM & Admin → Service Accounts** を選択
2. 「+ CREATE SERVICE ACCOUNT」をクリック
3. サービスアカウント名を入力（例: `expo-eas-submit`）
4. 「CREATE AND CONTINUE」をクリック
5. ロールで **Service Account User** を選択
6. 「CONTINUE」→「DONE」をクリック

## 1-4. JSONキーをダウンロード

1. 作成したサービスアカウントの右側の「Actions」メニュー（︙）をクリック
2. 「Manage keys」を選択
3. 「ADD KEY → Create new key」をクリック
4. 形式で「JSON」を選択してダウンロード

:::message alert
このJSONファイルは機密情報です。Gitにコミットしないよう、必ず `.gitignore` に追加してください。
:::

ダウンロードしたJSONファイルは、プロジェクトルートに配置します（例: `service-account-key.json`）。

---

# Step 2: Service AccountをGoogle Play Consoleに紐付け

次に、作成したサービスアカウントにGoogle Play Consoleへのアクセス権限を付与します。

1. [Google Play Console](https://play.google.com/console)にアクセス
2. 左メニューから **Setup → Users and permissions** を選択
3. 「Invite new users」をクリック
4. サービスアカウントのメールアドレス（`***@***.iam.gserviceaccount.com`形式）を入力
5. 「Account permissions」で **Admin（すべてにアクセス）** を選択
6. 「Invite user」をクリック

これで、EASからGoogle Play Consoleを操作できるようになります。

---

# Step 3: EAS CLIのセットアップ

## 3-1. EAS CLIをインストール

ターミナルで以下のコマンドを実行します：

```bash
npm install -g eas-cli
```

## 3-2. Expoアカウントにログイン

```bash
eas login
```

ログイン状態を確認するには：

```bash
eas whoami
```

## 3-3. EAS Buildの設定

プロジェクトルートで以下を実行：

```bash
eas build:configure
```

このコマンドにより、プロジェクトに `eas.json` ファイルが作成されます。

---

# Step 4: 初回のプロダクションビルドを作成

## 4-1. app.jsonの設定を確認

`app.json` または `app.config.js` で以下の項目を確認・設定します：

```json
{
  "expo": {
    "name": "Your App Name",
    "slug": "your-app-slug",
    "version": "1.0.0",
    "android": {
      "package": "com.yourcompany.yourapp",
      "versionCode": 1,
      "adaptiveIcon": {
        "foregroundImage": "./assets/adaptive-icon.png",
        "backgroundColor": "#FFFFFF"
      }
    }
  }
}
```

:::message
`versionCode` は整数で、ビルドごとに増やす必要があります。Google Playでは同じバージョンコードのビルドは受け付けられません。
:::

## 4-2. ビルドを実行

```bash
eas build --platform android
```

初回ビルド時に、キーストア（アプリ署名用の鍵）の生成を求められます。「Yes」を選択してExpoに自動生成させましょう。

ビルドが完了すると、EASダッシュボードのURLが表示されます。そこから `.aab` ファイルをダウンロードできます。

:::message
`.aab`（Android App Bundle）は、Google Playで推奨されているアプリ配布形式です。APKよりもファイルサイズが最適化されます。
:::

---

# Step 5: Google Play Consoleでアプリを登録

## 5-1. 新しいアプリを作成

1. [Google Play Console](https://play.google.com/console)にアクセス
2. 「Create app」をクリック
3. 以下の情報を入力：
   - **App name**: アプリ名
   - **Default language**: 日本語
   - **App or game**: Game または App を選択
   - **Free or paid**: Free（無料）または Paid（有料）
4. デベロッパープログラムポリシーとアメリカ輸出法に同意
5. 「Create app」をクリック

## 5-2. セットアップタスクを完了させる

ダッシュボードに表示される「Set up your app」のタスクを順番にこなしていきます。

### プライバシーポリシー

プライバシーポリシーのURLが必要です。自分で用意するか、以下のようなジェネレーターを使えます：

- [App Privacy Policy Generator](https://app-privacy-policy-generator.nisrulz.com/)
- [TermsFeed](https://www.termsfeed.com/)

生成したプライバシーポリシーをどこか（自分のサイトやGitHub Pagesなど）にホストし、URLを入力します。

### App access

アプリに特別なログインや制限がない場合は「All functionality is available without special access」を選択。

### Ads

広告を表示しない場合は「No, my app does not contain ads」を選択。

### Content rating

質問票に答えて年齢レーティングを取得します：

1. メールアドレスを入力
2. アプリのカテゴリを選択（例: Game, Utility）
3. 暴力、性的コンテンツ、違法薬物などに関する質問に答える
4. 「Submit」して結果を確認

### Target audience

対象年齢層を選択します（例: 13歳以上）。

### News app

ニュースアプリでなければ「No」を選択。

### Data safety

アプリが収集・共有するユーザーデータについて申告します。データ収集をしていない場合は「No data collected」を選択。

### Government apps

政府機関向けアプリでなければ「No」。

### その他のカテゴリ

Financial features、Health、など該当しない項目はすべて「No」で進めます。

### App category and contact details

- **Category**: アプリのカテゴリを選択（例: Games > Puzzle）
- **Tags**: 任意でタグを追加
- **Email address**: サポート用のメールアドレスを入力

---

# Step 6: Store listingを作成

ストアリスティングは、ユーザーがGoogle Playで最初に目にする情報です。審査の合否にも影響する重要な部分です。

## 6-1. アプリの詳細

左メニューの **Grow → Store presence → Main store listing** を選択。

### App name

最大30文字。ストアで表示されるアプリ名です。

### Short description

最大80文字。アプリの簡潔な説明。

### Full description

最大4000文字。アプリの機能を詳しく説明します。

:::message alert
**重要**: 説明が曖昧だと審査で却下される可能性があります。各画面で何ができるかを具体的に書きましょう。例：

- ○「タスクを追加、編集、削除できます」
- ×「便利なアプリです」
  :::

## 6-2. グラフィックアセット

### App icon（512×512 PNG）

既存のアイコンがサイズ要件を満たしていない場合、以下のツールで調整できます：

- [Android Asset Studio](https://romannurik.github.io/AndroidAssetStudio/icons-launcher.html)
- [App Icon Generator](https://www.appicon.co/)

### Feature graphic（1024×500 PNG）

ストアページのヘッダー画像です。以下のツールで簡単に作成できます：

- [Hotpot.ai Feature Graphic Maker](https://hotpot.ai/google-play-feature-graphic-maker)
- Canva
- Figma

### Screenshots

最低2枚、最大8枚のスクリーンショットが必要です：

- **Phone**: 縦向き・横向きどちらでも可
- **7-inch tablet**: タブレット用（任意だが推奨）
- **10-inch tablet**: タブレット用（任意だが推奨）

エミュレーターや実機でスクリーンショットを撮影してアップロードします。

---

# Step 7: 内部テストリリースを作成

## 7-1. テスターを設定

1. 左メニューから **Release → Testing → Internal testing** を選択
2. 「Create email list」でテスターのメールリストを作成
3. 自分のメールアドレスを追加

## 7-2. リリースを作成

1. 「Create new release」をクリック
2. App signing で「Use Google-generated key」を選択（推奨）
3. 「Upload」をクリックし、先ほどダウンロードした `.aab` ファイルをアップロード
4. Release name に「1.0.0」などバージョン番号を入力
5. Release notes に「Initial release」などリリース内容を記載
6. 「Save」→「Review release」→「Start rollout to Internal testing」をクリック

## 7-3. Play Integrity APIを有効化

1. 左メニューから **Release → App integrity** を選択
2. 「Link Cloud project」をクリック
3. 先ほど作成したGoogle Cloudプロジェクトを選択

## 7-4. 内部テストで確認

テスターのメールアドレスに招待リンクが届きます。リンクからアプリをダウンロードして動作確認しましょう。

---

# Step 8: 本番リリースを準備

内部テストで問題がなければ、本番リリースに進みます。

## 8-1. 対象国・地域を設定

1. 左メニューから **Release → Production** を選択
2. 「Countries / regions」タブを開く
3. 「Add countries / regions」で配信したい国を選択（全世界なら「Select all」）

## 8-2. 本番リリースを作成

1. 「Create new release」をクリック
2. 内部テストと同様に `.aab` をアップロード
3. Release name と Release notes を入力
4. 「Save」→「Review release」→「Start rollout to Production」

## 8-3. 審査に提出

1. ダッシュボードに戻り、残っているエラーや警告を解消
   - 例: Advertising ID の使用有無
2. すべてクリアしたら「Send changes for review」をクリック

:::message
審査には数時間〜数日かかります。審査状況はメールとPlay Consoleで確認できます。
:::

---

# Step 9: 自動提出の設定（オプション）

2回目以降のビルドから、EAS Submitを使って提出を自動化できます。

## 9-1. eas.jsonに設定を追加

プロジェクトルートの `eas.json` に以下を追加します：

```json
{
  "build": {
    "production": {
      "android": {
        "buildType": "app-bundle"
      }
    }
  },
  "submit": {
    "production": {
      "android": {
        "serviceAccountKeyPath": "./service-account-key.json",
        "track": "internal"
      }
    }
  }
}
```

- `serviceAccountKeyPath`: Step 1でダウンロードした JSON ファイルのパス
- `track`: 提出先トラック（`internal`, `alpha`, `beta`, `production`）

## 9-2. .gitignoreと.easignoreを設定

**`.gitignore`** に以下を追加：

```
service-account-key.json
```

**`.easignore`** を作成し、以下を記載：

```
!service-account-key.json
```

これにより、GitHubにはアップロードされず、EASビルドサーバーではファイルが利用可能になります。

## 9-3. 自動ビルド＆提出を実行

```bash
eas build --platform android --auto-submit
```

このコマンド1つで、ビルド作成 → Google Playへの提出が自動で行われます。

提出状況は[Expo Dashboard](https://expo.dev/)の「Submissions」タブで確認できます。

---

# よくあるエラーと対処法

## エラー1: 「Version code has already been used」

**原因**: 同じ `versionCode` のビルドをアップロードしようとしている。

**対処法**:

1. `app.json` の `android.versionCode` を増やす（例: 1 → 2）
2. 再ビルド: `eas build --platform android`
3. 新しい `.aab` をアップロード

## エラー2: 「You need to use a different package name」

**原因**: すでに使われているパッケージ名を指定している。

**対処法**: `app.json` の `android.package` を一意の名前に変更（例: `com.yourname.uniqueappname`）。

## エラー3: 「App Bundle was not signed」

**原因**: キーストアが正しく設定されていない。

**対処法**: EASビルド時にキーストアの自動生成を「Yes」にする。すでに生成済みの場合、Expo Dashboardで確認できます。

## エラー4: 審査で却下される

**原因**: ストアリスティングの説明が不十分、またはポリシー違反。

**対処法**:

- 説明文を具体的に書き直す
- スクリーンショットを追加・改善
- プライバシーポリシーを正確に記載
- Googleからのフィードバックを確認して修正

---

# バージョン更新時のチェックリスト

アプリを更新する際は、以下を忘れずに行いましょう：

- [ ] `app.json` の `version` を更新（例: `1.0.0` → `1.1.0`）
- [ ] `app.json` の `android.versionCode` を増やす（例: 1 → 2）
- [ ] `eas build --platform android` で新しいビルドを作成
- [ ] Google Play Consoleで新しいリリースを作成
- [ ] Release notesに変更内容を記載
- [ ] 内部テストで動作確認してから本番公開

---

# まとめ

この記事では、Expo React Nativeアプリを初めてGoogle Play Storeに公開するまでの全手順を解説しました。

**重要なポイント**:

- Google Service Accountを作成してEASとの連携を構築
- 初回は手動提出が必要だが、2回目以降は自動化可能
- ストアリスティングは審査の合否に影響するため丁寧に作成
- `versionCode` は必ずインクリメント
- `.gitignore` と `.easignore` でService Account Keyを適切に管理

最初は複雑に感じるかもしれませんが、一度流れを理解すれば、次回からはスムーズに公開できるようになります。

継続的デリバリー（CD）の仕組みを整えれば、コード変更から公開までを大幅に効率化できます。ぜひチャレンジしてみてください！

## 参考リンク

- [React Native Expo を Google Play ストアに公開 - YouTube](https://www.youtube.com/watch?v=sruasvn7klU)
- [Android 向けプロダクションビルドの作成方法 | EAS チュートリアル - YouTube](https://www.youtube.com/watch?v=nxlt8uwqhpE)
- [Expo EAS Build Documentation](https://docs.expo.dev/build/introduction/)
- [Expo EAS Submit Documentation](https://docs.expo.dev/submit/introduction/)
- [Google Play Console Help](https://support.google.com/googleplay/android-developer)
- [Android App Bundle について](https://developer.android.com/guide/app-bundle)

---

もし不明な点があれば、コメント欄で質問してください。Happy coding! 🚀
