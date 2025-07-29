---
title: "npx prisma generate実行時に発生するエラー「EPERM: operation not permitted, unlink」の解決方法"
emoji: "😁" # アイキャッチとして使われる絵文字（1文字だけ）
type: "tech" # tech: 技術記事 / idea: アイデア記事
topics: ["nextjs", "prisma"] # タグ。["markdown", "rust", "aws"]のように指定する
published: true # 公開設定（falseにすると下書き）
---

# npx prisma generate 実行時に発生するエラー"EPERM: operation not permitted, unlink"の 解決方法

## Error 内容

```
EPERM: operation not permitted, unlink '...node_modules\prisma\query_engine-windows.dll.node'
```

## ズバリの解決方法

@prisma/client を手動でインストールする

1. Delete node_modules
2. Run npm install
3. Run npm install @prisma/client
4. Run npx prisma generate / npm prisma migrate dev

## 参考

https://github.com/prisma/prisma/issues/9184
