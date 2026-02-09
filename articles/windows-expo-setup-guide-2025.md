---
title: "WindowsでExpo (React Native) 環境構築完全ガイド 〜JDKの罠とエミュレータ設定まで〜"
emoji: "🚀"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ["reactnative", "expo", "androidstudio", "windows", "環境構築"]
published: true
---

React Native 開発を Windows で始めようとしたとき、環境構築でつまずいた経験はありませんか？
「JDK のバージョンが合わない」「環境変数が通らない」「エミュレータが動かない」……。
そんな **3大ハマりポイント** を完全に網羅したガイドを作成しました。

この手順通りに進めれば、 `npx react-native doctor` で **オールグリーン** の快適な開発環境が手に入ります。さっそく進めていきましょう！

## 1. 🛠️ Android Studio のインストールと SDK 設定

まずは公式サイトから **Android Studio** をインストールします。
インストール後、 SDK Manager （ `More Actions` > `SDK Manager` ）を開き、以下の 2 つのタブを設定してください。

### ① 📱 SDK Platforms タブ (OSバージョン)

以下の項目にチェックを入れてインストールします。

- **Android 15.0 ("VanillaIceCream")**
- **Android 14.0 ("UpsideDownCake")** ← Google Play 要件（API 34）のために必須です

**【重要】**
各バージョンの左にある「＞」を展開し、以下がチェックされているか必ず確認してください。

- `Google Play Intel x86_64 Atom System Image`

これがないとエミュレータが動きません。 AMD (Ryzen) の場合も最近はこれで動くことが多いですが、もし動作しない場合は `Google APIs ...` を試してみてくださいね。

### ② ⚙️ SDK Tools タブ (ビルド道具)

ここが最大の落とし穴です。以下の項目を必ずチェックしてください。

1. **Android SDK Build-Tools 34.0.0**
   - 右下の **[Show Package Details]** にチェックを入れないと詳細バージョンが見えません。
   - リストを展開し、 **34.0.0** をピンポイントでインストールしてください（ React Native がこれを要求します）。
2. **Android SDK Command-line Tools (latest)**
   - これがないと `doctor` コマンドで SDK が見つからない（N/A）エラーになります。
3. **Android Emulator**
4. **Android SDK Platform-Tools**
5. **Intel x86 Emulator Accelerator (HAXM)** または **AMD Hypervisor**

![Android SDK Tools の設定](https://github.com/Inosuke0718/Zenn/blob/main/images/android-sdk.png?raw=true)

## 2. 🌐 環境変数の設定 (手動必須)

Android Studio を入れただけでは、コマンドラインツールへのパスが通っていません。
Windows の「環境変数」を開き、以下の設定を追加しましょう。

### ユーザー環境変数の新規作成

- 変数名: `ANDROID_HOME`
- 値: `C:\Users\<ユーザー名>\AppData\Local\Android\Sdk`
  （ Android Studio の SDK Manager 上部に表示されているパスをコピペするのが確実です）

### Path の編集

ユーザー環境変数の `Path` に、以下の 3 つを追加します。

- `%ANDROID_HOME%\emulator`
- `%ANDROID_HOME%\platform-tools`
- `%ANDROID_HOME%\cmdline-tools\latest\bin`

## 3. ☕ JDK (Java) のバージョン問題

ここもよくハマるポイントです。
**React Native は JDK 17 推奨です。** 最新の JDK 21 などを入れるとビルドエラーが出ることがあるので注意しましょう。

### 確認方法

ターミナルで以下のコマンドを叩いてみてください。

```powershell
java -version
```

### もし「JDK 21」などになっている場合

1. **JDK 17** (Microsoft Build of OpenJDK 17 等) をインストールします。
2. 環境変数 `JAVA_HOME` の値を JDK 17 のパスに変更します。
3. 環境変数 `Path` の中で、 Oracle などの `javapath` が勝手に追加されている場合は削除するか、 `%JAVA_HOME%\bin` を一番上に移動させてください。

## 4. 🩺 診断コマンドで最終確認

設定が終わったら、ターミナル（ PowerShell ）を再起動して以下のコマンドを実行しましょう。

```powershell
npx react-native doctor
```

全ての項目にチェック（✓）がついていれば完璧です！
※ `Adb` のバツ印は「今デバイスがつながっていない」だけなので、この段階では無視して大丈夫ですよ。

## 5. 🚀 VS Code からエミュレータを起動する

開発のたびに Android Studio を開くのは少し面倒ですよね。 VS Code から直接起動できるように設定しておきましょう。

### 手順

1. `emulator -list-avds` でエミュレータ名を確認します。
   （例： `Pixel_3a_API_34` ）
2. `emulator -avd Pixel_3a_API_34` で起動できます。

### さらに便利に（npm scripts）

`package.json` に以下を追記しておくと、 `npm run android:emu` だけでサクッとエミュレータが立ち上がります。

```json
"scripts": {
  "android": "expo start --android",
  "android:emu": "emulator -avd Pixel_3a_API_34",
  "ios": "expo start --ios",
  "start": "expo start"
}
```

## 📝 まとめ

いかがでしたでしょうか？ Windows での環境構築は少し手順が多いですが、ポイントを抑えれば怖くありません。

- **Android Studio** で Build-Tools 34.0.0 をピンポイントで入れる
- **環境変数** `ANDROID_HOME` と `Path` を手動で設定する
- **JDK 17** を使用する（最新すぎないのがコツ！）
- **npx react-native doctor** で定期的に診断する

これで快適な React Native ライフの始まりです！さっそくアプリを作ってみましょう。

さらに詳しく知りたい方は、 [Expo 公式ドキュメント](https://docs.expo.dev/get-started/installation/) もぜひチェックしてみてくださいね。
