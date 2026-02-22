---
title: "Electronデスクトップアプリの配布・自動更新・課金設計 完全ガイド"
emoji: "🐱"
type: "tech"
topics:
  ["electron", "electronbuilder", "githubactions", "lemonsqueezy", "autoupdate"]
published: true
---

## はじめに

Electronでデスクトップアプリを作ったあと、「どうやって配布・アップデートするか」の設計で詰まる人は多いです。
この記事では以下のケースを想定した設計をまとめます。

- **ソースコードは公開したくない（Privateリポジトリ）**
- **買い切り課金（Lemon Squeezy）を使う**
- **自社サイトのDLボタンから配布したい**
- **アプリの自動更新をしたい**

---

## 全体アーキテクチャ

```
[ユーザー]
  ↓ 購入
[Lemon Squeezy] → ライセンスキー発行
  ↓ メール/購入後ページ
自社サイトの「Download」ボタン
  ↓
[GitHub Releases] ← インストーラ(.exe)を置く場所
  ↓ インストール・起動
[Electronアプリ]
  ├── Lemon Squeezyでライセンス認証
  └── electron-updaterで自動更新チェック
          ↓
    [GitHub Releases] の latest.yml を参照
```

---

## 1. リポジトリ構成

「ソースPrivate + リリース専用Publicリポジトリ」が個人・小規模開発のベストプラクティスです。

| リポジトリ           | 公開設定    | 中身                                |
| -------------------- | ----------- | ----------------------------------- |
| `mewmodoro`          | **Private** | ソースコード一式                    |
| `mewmodoro-releases` | **Public**  | インストーラ(.exe)・latest.yml のみ |

### なぜPublicリポジトリが必要か？

electron-updaterはアプリ起動時にGitHub Releasesの`latest.yml`を確認して更新を検知します。
Privateリポジトリのままでも技術的には可能ですが、以下の問題があります。

- **GH_TOKENの露出リスク**: Privateリポジトリから更新チェックするには`GH_TOKEN`が必要ですが、
  これをアプリに埋め込むとユーザーがトークンを読み取れてしまいます
- **公式も非推奨**: electron-builder公式が「very special cases向けであり、全ユーザー向けではない」と明記しています

### 解決策: リリース専用Publicリポジトリを作る

ソースコードは完全Privateを保ちつつ、ビルド成果物（インストーラ）だけを別のPublicリポジトリに置きます。
`electron-builder.yml`でリリース先を指定するだけです。

```yaml
publish:
  provider: github
  owner: your-github-username
  repo: mewmodoro-releases # ← ソースとは別のPublicリポジトリ
```

---

## 2. 課金設計：GitHub Releases Public + アプリ内ライセンス制御

買い切り課金の場合、よくある2パターンがあります。

| パターン                              | 内容                                             | 向いているケース           |
| ------------------------------------- | ------------------------------------------------ | -------------------------- |
| **A. Releases Public + アプリ内認証** | バイナリは誰でもDL可、起動時にライセンスキー認証 | まず売って改善したい       |
| **B. 認証付き配信サーバ**             | 購入者だけがDL・更新可能                         | バイナリ自体を渡したくない |

個人開発の初期フェーズなら **Aが最短** です。
未購入者がインストーラを入手できても、ライセンスがなければ機能が使えない設計にすれば商売として成立します。

### Lemon Squeezyでのライセンス認証フロー

```
1. ユーザーが自社サイトでLemon Squeezyの購入フォームから購入
2. Lemon Squeezyがライセンスキーを自動発行・メール送付
3. アプリ起動時にキー入力欄を表示
4. Lemon Squeezy License APIにactivateリクエスト
5. 返ってきた instance.id をローカルに保存
6. 以後の起動はvalidateで認証
```

Lemon Squeezy License APIのエンドポイント：

```typescript
// アクティベーション
const res = await fetch("https://api.lemonsqueezy.com/v1/licenses/activate", {
  method: "POST",
  headers: { "Content-Type": "application/x-www-form-urlencoded" },
  body: new URLSearchParams({
    license_key: inputKey,
    instance_name: os.hostname(),
  }),
});

// 検証（起動時）
const res = await fetch("https://api.lemonsqueezy.com/v1/licenses/validate", {
  method: "POST",
  headers: { "Content-Type": "application/x-www-form-urlencoded" },
  body: new URLSearchParams({
    license_key: savedKey,
    instance_id: savedInstanceId,
  }),
});
```

---

## 3. 自社サイトのDLボタン設定

GitHub Releasesのアセットには **直リンク** が使えます。
自社サイトのボタンにこのURLを貼るだけで、クリックと同時にダウンロードが始まります。

```
https://github.com/<owner>/<repo>/releases/latest/download/<filename>
```

**ポイント** : 毎リリースで同じファイル名にすること。

```
# 良い例（固定ファイル名）
https://github.com/yourname/mewmodoro-releases/releases/latest/download/Mewmodoro-Setup.exe

# 悪い例（バージョン付きファイル名→都度URLが変わる）
https://github.com/yourname/mewmodoro-releases/releases/download/v1.0.3/Mewmodoro-Setup-1.0.3.exe
```

---

## 4. electron-updaterの仕組みと実装

electron-updaterは「 **アプリの中（メインプロセス）** 」で動くライブラリです。
GitHub Releasesは「 **更新ファイルの置き場** 」です。この2つが連携して自動更新が成立します。

### 全体フロー

```
【リリース時】
  electron-builder でビルド
      ↓
  GitHub Actions が走る
      ↓
  GitHub Releases に自動アップロード
  ├── Mewmodoro-Setup.exe   ← インストーラ本体
  └── latest.yml            ← 「最新バージョン情報」

【アプリ起動時】
  electron-updater が latest.yml を確認
      ↓
  現バージョン < latest.yml のバージョン なら通知
      ↓
  バックグラウンドでダウンロード
      ↓
  「再起動して更新」でインストール完了
```

### 各ツールの役割分担

| 名前               | タイミング       | 役割                                                       |
| ------------------ | ---------------- | ---------------------------------------------------------- |
| `electron-builder` | **ビルド時**     | インストーラ生成・GitHubへのアップロード・`latest.yml`生成 |
| `electron-updater` | **アプリ実行時** | `latest.yml`の監視・ダウンロード・インストール             |

### 実装

```bash
npm install electron-updater
```

```typescript
// main.ts（メインプロセス）
import { autoUpdater } from "electron-updater";

app.whenReady().then(() => {
  autoUpdater.checkForUpdatesAndNotify();
});
```

これだけで「チェック→ダウンロード→通知」まで自動で行われます。
`electron-builder`でビルドすると`app-update.yml`がアプリ内に自動生成され、
どのリポジトリを見に行くかの情報が書き込まれるため、手動での`setFeedURL()`は不要です。

---

## 5. GitHub Actionsによる自動ビルド・リリース

ソースPrivateリポジトリのActionsから、リリース専用Publicリポジトリへ成果物をアップロードします。

```yaml
# .github/workflows/release.yml（ソースPrivateリポジトリ側）
name: Release

on:
  push:
    tags:
      - "v*"

jobs:
  build:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 20

      - name: Install dependencies
        run: npm ci

      - name: Build and publish
        env:
          # リリース専用Publicリポジトリへの書き込み権限があるトークン
          GH_TOKEN: ${{ secrets.GH_TOKEN }}
        run: npm run build -- --publish always
```

`GH_TOKEN`はGitHubのSecrets（Settings → Secrets）で安全に管理します。
アプリ本体には埋め込まれないため、セキュリティリスクはありません。

---

## 6. SmartScreen警告への対応

Windowsでは署名なしのアプリに「WindowsによってPCが保護されました」という青い警告が出ます。

| 対策                                  | コスト         | 効果     |
| ------------------------------------- | -------------- | -------- |
| 説明文を書いて回避手順を案内          | **無料**       | △ UX悪い |
| OV証明書で署名（実績で評判が上がる）  | **年数万円**   | ○        |
| EV証明書で署名（即時SmartScreen突破） | **年10万円〜** | ◎        |

初期フェーズでは「READMEや配布ページに回避手順（詳細情報→実行）を明記する」運用カバーが現実的です。
ユーザーが増えてきたらEV証明書の取得を検討しましょう。

---

## まとめ

| 項目                   | 採用技術                                         |
| ---------------------- | ------------------------------------------------ |
| 課金・ライセンス発行   | Lemon Squeezy                                    |
| アプリ内認証           | Lemon Squeezy License API                        |
| ソースコード管理       | GitHub（Private）                                |
| 配布・更新ホスティング | GitHub Releases（Public、別リポジトリ）          |
| ビルド・リリース自動化 | electron-builder + GitHub Actions                |
| 自動更新               | electron-updater                                 |
| DLボタン               | `releases/latest/download/<filename>` の直リンク |

「まず売って回して改善する」フェーズに最適な、コスト最小・実装最短の構成です。
