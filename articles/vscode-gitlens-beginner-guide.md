---
title: "【VS Codeだけで完結】VS Code × GitLensで実現する、やさしいGitHub操作入門 🎉"
emoji: "🎉"
type: "tech"
topics:
  ["vscode", "git", "github", "gitlens", "初心者", "Antigravity", "Cursor"]
published: true
---

# 【VS Codeだけで完結】VS Code × GitLensで実現する、一番やさしいGitHub操作入門 🎉

## はじめに：GitHubは「怖くない」

「ターミナルでコマンドを叩くのが怖い…」
「コンフリクト（競合）が起きて、コードが壊れたらどうしよう」
「今、自分が何をしているか分からなくなってしまう」

GitやGitHubを学び始めたとき、こんな風に迷う瞬間、ありませんか？

そんな "GitHubアレルギー" を持っている初心者の方へ。
実は、VS Code と強力な拡張機能である **「GitLens」** を使えば、GitHubの操作はスマホの写真管理くらい直感的になります。黒い画面（ターミナル）を開く必要は一切ありません！

この記事では、「コマンドを一切打たずに」 安全にGitHubを操作し、日々の開発を分かりやすく管理する方法を解説します。

## 📚 0. 前提知識

「そもそもGitやGitHubって何？」という方は、ぜひこちらの記事を先に読んでみてください。理解がグッと深まります。

[【Git頼むからこれだけは知っておけ】初心者でも迷わない！Git & GitHub の基本をサクッと解説 🌲](https://zenn.dev/imohuke/articles/git-github-beginner-guide)

※またこの記事ではAntigravityを使って操作しています。VS Code(Cursor, Kiro, WindSurf)でも同様の操作が可能です。

## 🔍 1. 準備：相棒「GitLens」を入れる

まずはVS Codeに拡張機能を入れましょう。これがあるだけで、目に見えないGitの履歴がパッと見て分かるようになります。

- **拡張機能名** : `GitLens — Git supercharged`
- **インストール方法** : VS Code左側の **拡張機能タブ（四角いブロックのアイコン）** を開き、「GitLens」と検索してインストールを押します。

![GitLensのインストール画面](https://github.com/Inosuke0718/Zenn/blob/main/images/git/git-lens.png?raw=true)
_画像補足：検索窓に「GitLens」と入力すると、一番上に公式のGitLensが表示されます。右下の「Install」ボタンをクリックしましょう。_

:::message
**💡 ポイント**
インストールすると、エディタ上のコードの横に薄い文字で「誰が・いつ・この行を書いたか」が表示されるようになります（インラインBlame機能）。
「これ、いつ書いたコードだっけ？」が1秒で分かるようになり、開発の安心感が段違いにアップします！
:::

## 🎬 2. プロジェクトを初期化する（git init）

まずはVS Codeで開発するフォルダ（プロジェクト）を開きます。
次に、左側のメニューから **ソース管理（枝が分かれているアイコン）** をクリックします。

まだGitで管理されていないフォルダの場合は、青い **「Initialize Repository（リポジトリを初期化する）」** というボタンが表示されるので、それをクリックしてください。

![リポジトリの初期化](https://github.com/Inosuke0718/Zenn/blob/main/images/git/git-init.png?raw=true)
_画像補足：左側のパネルに大きく「Initialize Repository」と書かれた青いボタンが現れます。これを押すだけで、そのフォルダがGitの管理下に入ります。_

## 👀 3. 変更を確認してステージングする（git add）

コードを書いたり修正したりしたら、いきなり保存記録を作るのではなく、「何を変えたか」を確認するステップを踏みましょう。

1. VS Code左側の **ソース管理アイコン** をクリックします。
2. **Changes（変更）** 欄に、新しく作ったファイルや編集したファイルの名前が一覧表示されます。

![変更の確認](https://github.com/Inosuke0718/Zenn/blob/main/images/git/git-changes.png?raw=true)
_画像補足：ファイル名の右横に「U（追跡されていない）」や「M（変更された）」という記号がつき、変更があったことが一目で分かります。_

変更内容を確認したら、次はその記録を「保存対象」にするために **ADD（ステージング）** します。
ファイル名の右側にカーソルを合わせると現れる **＋（プラス）ボタン** を押しましょう。

![変更をADDする](https://github.com/Inosuke0718/Zenn/blob/main/images/git/git-add.png?raw=true)
_画像補足：プラスボタン（Stage Changes）を押すと、対象のファイルが「Staged Changes（ステージされた変更）」という一つ上の枠に移動します。これで保存準備が整いました。_

## 📝 4. 変更に名前をつける（git commit）

保存準備ができたら、その変更に対して「何をしたか」という **コミットメッセージ** を付けます。

![COMMIT Messageの入力](https://github.com/Inosuke0718/Zenn/blob/main/images/git/git-commit-msg.png?raw=true)
_画像補足：ソース管理パネルの上部にある入力ボックス（Message）に、「ヘッダーのデザインを修正」などの分かりやすい説明を入力します。_

メッセージを入力したら、すぐ下にある青い **「Commit」** ボタンをクリックします。

![COMMITの実行](https://github.com/Inosuke0718/Zenn/blob/main/images/git/git-commit.png?raw=true)
_画像補足：「Commit」ボタンを押すと変更の履歴が確定し、左パネルの表示がクリアされます。これであなたのパソコン上（ローカル）での記録は完了です！_

## ☁️ 5. GitHubにプッシュする（git push）

ローカルで保存した記録を、インターネット上のGitHubにも反映させましょう。これを **プッシュ（Push）** と呼びます。

まだGitHubにリポジトリを作っていない場合は、青い **「Publish Branch」** ボタンを押します。
（※GitHubにログインしていない場合は、ここでログインを求められます。）

すると、画面の上部に以下のような選択肢が表示されます。

- **Publish to GitHub private repository** （自分だけが見れる非公開リポジトリ）
- **Publish to GitHub public repository** （誰でも見れる公開リポジトリ）

![PublicかPrivateの選択](https://github.com/Inosuke0718/Zenn/blob/main/images/git/git-select-private-public.png?raw=true)
_画像補足：ポートフォリオとして公開したい場合は「public」を、個人的なメモや公開前のプロジェクトなら「private」を選びましょう。_

これでGitHubへのプッシュが完了しました！自分のGitHubページにアクセスして、先ほどプッシュしたデータが反映されているか確認してみましょう。

---

ここからは、さらに一歩進んだ **「作業ブランチを分ける」** という実践的な方法を解説します。実際の開発現場では必須のスキルです！

## 🌿 6. 新しいブランチを作成する

機能を追加したりバグを直したりするときは、メインの履歴から枝分かれさせた **ブランチ** を作って作業するのがベストプラクティスです。

VS Codeの左下、あるいはGitLensのメニューから新しいブランチを作成します。
ここでは例として `fix/ui-bug` というブランチ名にします。

![ブランチの作成](https://github.com/Inosuke0718/Zenn/blob/main/images/git/git-create-branch.png?raw=true)
_画像補足：画面上部のコマンドパレットに新しく作りたいブランチ名「fix/ui-bug」を入力し、エンターを押して作成・移動します。_

作成したら、VS Codeの一番左下の表示を見てみましょう。現在の作業場所が `main` から新しいブランチ名に変わっているはずです。

![新しいブランチの確認](https://github.com/Inosuke0718/Zenn/blob/main/images/git/git-confirm-new-branch.png?raw=true)
_画像補足：左下の小さなブランチアイコンの横に「fix/ui-bug」と表示されていれば、無事に新しいブランチに移動（チェックアウト）できています。_

## 🔄 7. ブランチ内で作業して、プッシュする

新しいブランチでファイルの修正が終わったら、先ほどの **「3〜5」と同じ操作** を行います。
今回は例として、コミットメッセージを `fix ui` として進めます。

![Git AddとCommit](https://github.com/Inosuke0718/Zenn/blob/main/images/git/git-add-commit2.png?raw=true)
_画像補足：同じようにファイルを「＋」で「Staged Changes」に追加し、メッセージを書いてCommitボタンを押します。_

その後、青い **「Publish Branch（またはSync Changes）」** ボタンを押して、このブランチごとGitHubにアップロードしましょう。

![新しいブランチをPush](https://github.com/Inosuke0718/Zenn/blob/main/images/git/git-push2.png?raw=true)
_画像補足：これで、作業用の枝である `fix/ui-bug` ブランチにプッシュされ、インターネット上に保存されました。_

## 🤝 8. Mainブランチにマージ（合流）する

作業が終わったら、その変更を本流の `main` ブランチに合流（マージ）させましょう。

まずは自分の作業場所（いるブランチ）を `main` に戻す必要があります。
VS Code左下のブランチ名をクリックし、一覧から `main` を選ぶか、GitLensメニューから `main` ブランチを右クリックして「Switch to Branch...」を選択します。

![Mainブランチへの移動](https://github.com/Inosuke0718/Zenn/blob/main/images/git/git-checkout.png?raw=true)
_画像補足：ベースとなる `main` ブランチに戻ります。この瞬間、エディタ上のコードはいったん作業する前の古い状態に戻ります。_

左下が `main` になっていることを確認したら、先ほどまで作業していた `fix/ui-bug` ブランチを右クリックし、 **「Merge Branch into Current...」** を選択します。

![ブランチのマージ](https://github.com/Inosuke0718/Zenn/blob/main/images/git/git-merge.png?raw=true)
_画像補足：これで「今の場所（ `main` ）に `fix/ui-bug` の変更内容をドッキングして！」という指示を出せます。_

すると画面上部に最終確認が出ますので、 **Merge** を選択します。

![マージの実行](https://github.com/Inosuke0718/Zenn/blob/main/images/git/git-merge2.png?raw=true)
_画像補足：確認ダイアログで「Merge」を押せば完了です！最後に `main` ブランチを再びSync（Push）すれば、すべての作業が完了してGitHubの `main` も最新になります。_

## ✨ まとめ

お疲れ様でした！VS CodeとGitLensを使えば、黒い画面に怯えることなく、直感的にGitHubを使いこなせることが分かったのではないでしょうか。

今回の重要なポイントをおさらいしましょう。

- **作業の確認はしっかり行う** ：何が変わったか（Changes）、どれを保存対象にしたか（Staged）を視覚的にチェックしましょう。
- **Commitには分かりやすいメッセージを** ：後から振り返ったときに困らないよう、「何をしたか」を一言で添えましょう。
- **機能追加は新ブランチで** ： `main` ブランチを直接触らず、新しい枝（ブランチ）を作って安全に開発しましょう。
- **UI（画面）を信じる** ：ポチポチとクリックするだけで、複雑なコマンドと同じことができるので、落ち着いて操作しましょう。

まずは自分の小さなプロジェクトで、いろいろ試しにポチポチと触ってみてください。操作に慣れれば、これらのツールは開発を支える最高の相棒になってくれますよ！
