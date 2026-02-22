---
title: "【Git×WSL2】GitHubをSSH接続にしたら、最後にremote URLもHTTPS→SSHへ切り替えよう"
emoji: "🔐"
type: "tech"
topics: ["wsl2", "ubuntu", "git", "github", "ssh"]
published: false
---

HTTPS で clone したあとに SSH 設定を終えると、「あれ、push のたびに認証が出る…？」って迷う瞬間、ありませんか？

結論、 **SSH 鍵を GitHub に登録しただけでは不十分** で、リポジトリ側の`origin`（リモート URL）を HTTPS→SSH に差し替えるのが決定版の手順です。

## 🧩 この記事でやること

この記事では、WSL2(Ubuntu)で GitHub に SSH 接続できる状態を作りつつ、最後に`git remote set-url`でリモート URL を SSH へ切り替えるところまでまとめます。

すでに SSH 鍵の登録まで終わっている人は「remote URL の切り替え」だけ読めば OK です。

## 🐧 WSL2 セットアップ（ざっくり）

WSL2 のインストールは PowerShell（管理者）で`wsl --install`を実行し、必要なら`wsl --update`も実行します。

初回起動でユーザー名・パスワードを設定したら、以降は Ubuntu 上で作業します。

## 🔑 GitHub を SSH 接続にする

SSH 鍵は Ubuntu で`ssh-keygen -t ed25519`を実行して作成します。

生成した公開鍵（例：`id_ed25519.pub`）を GitHub の SSH Keys に登録し、`ssh -T git@github.com`で疎通確認します。

## 🔁 HTTPS→SSH へ remote URL 切り替え（ここが本題）

SSH 接続ができても、リポジトリの`origin`が HTTPS のままだと、以降の通信も HTTPS のままです。

なので、`origin`の URL を SSH 形式に差し替えます。

### ✅ 事前確認：いまの origin を見る

まず、対象リポジトリ直下で`git remote -v`を実行します。

```bash
git remote -v
```

HTTPS の例（こうなっていたら切り替え対象）：

```text
origin  https://github.com/OWNER/REPOSITORY.git (fetch)
origin  https://github.com/OWNER/REPOSITORY.git (push)
```

### 🔧 変更：`git remote set-url`

次のコマンドで、HTTPS→SSH に変更できます。

```bash
git remote set-url origin git@github.com:OWNER/REPOSITORY.git
```

- `OWNER`：GitHub ユーザー名 or Organization 名
- `REPOSITORY`：リポジトリ名

### ✅ 再確認：ちゃんと変わった？

もう一度`git remote -v`で確認します。

```bash
git remote -v
```

SSH の例（こうなっていれば OK）：

```text
origin  git@github.com:OWNER/REPOSITORY.git (fetch)
origin  git@github.com:OWNER/REPOSITORY.git (push)
```

### 🧠 よくある「つまずき」あるある

- 悪い例：リポジトリじゃない場所で実行してしまう（`git remote -v`が通らない）
- 良い例：`cd`でプロジェクトへ移動 → `git remote -v`で確認 → `set-url` → もう一度`-v`

### 🧾 HTTPS と SSH の違い（パッと比較）

| 項目            | HTTPS                                     | SSH                                   |
| --------------- | ----------------------------------------- | ------------------------------------- |
| リモート URL 例 | `https://github.com/OWNER/REPOSITORY.git` | `git@github.com:OWNER/REPOSITORY.git` |
| 認証の考え方    | パスワード/トークン等                     | SSH 鍵                                |
| 今回やること    | -                                         | `git remote set-url`で差し替え        |

## まとめ

- WSL2(Ubuntu)で SSH 鍵を作り、GitHub に登録して疎通確認します。
- その後、`origin`が HTTPS のままだと通信も HTTPS のままなので、`git remote set-url`で SSH に差し替えるのがベストプラクティスです。
- 確認は`git remote -v`を「変更前 → 変更後」で 2 回やると安心です。

このテンプレを手元の`articles/xxx.md`に貼って、まずは 1 本公開まで進めてみましょう。公式ドキュメントも見てみましょう。
