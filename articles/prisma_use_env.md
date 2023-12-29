---
title: "【Prisma】複数の.envを分けてNext.jsのPrismaを利用する"
emoji: "😘" # アイキャッチとして使われる絵文字（1文字だけ）
type: "tech" # tech: 技術記事 / idea: アイデア記事
topics: ["Prisma", "Next.js"] # タグ。["markdown", "rust", "aws"]のように指定する
published: true # 公開設定（falseにすると下書き）
---

# dotenv-cli を使う
prisma公式では.envの使い分けは存在しないので、dotenv-cliを使用しましょう

## dotenv-cliインストール
```
npm add dotenv-cli
```

## prismaコマンドを利用するサンプル
.env.developmentを使ってprismaコマンドを実行するには
```
dotenv -e .env.development -- npx prisma db push

```

## package.jsonのbuild変更も忘れずに
```json:package.json
  "scripts": {
    "build": "dotenv -e .env.production -- npx prisma generate && dotenv -e .env.production -- npx prisma db push && dotenv
  },
```



### 参考
https://www.prisma.io/docs/orm/more/development-environment/environment-variables/using-multiple-env-files