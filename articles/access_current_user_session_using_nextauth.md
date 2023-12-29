---
title: "【NextAuth.js】APIルートを通じて現在のユーザーセッションデータにアクセスする方法"
emoji: "😸" # アイキャッチとして使われる絵文字（1文字だけ）
type: "tech" # tech: 技術記事 / idea: アイデア記事
topics: ["NextAuth.js", "Next.js"] # タグ。["markdown", "rust", "aws"]のように指定する
published: true # 公開設定（falseにすると下書き）
---

# ズバリ、getServerSession() メソッドを使用してAPIルートを保護すればユーザーセッションデータにアクセスできる

## getServerSession() メソッド
```
const session = await getServerSession(req, res, authOptions)
```

## 全体のソースコード
```
import { getServerSession } from "next-auth"
import { authOptions } from "@/app/api/auth/[...nextauth]/route"


const prisma = new PrismaClient()
export default async function handler(req: NextApiRequest, res: NextApiResponse) {

    const session = await getServerSession(req, res, authOptions)

    if (!session) {
        return res.status(401).json({ error: 'You must be sign in to view the protected content.' });
    }
```

## 混乱するポイント
getSessionを使ってもユーザーセッションデータにアクセスできるが、なぜかPostリクエスト時は不可能！
GetリクエストだとgetSessionでもアクセスできるので、少しハマりました。。

その時のエラーはこちら
```
[next-auth][error][CLIENT_FETCH_ERROR] 
https://next-auth.js.org/errors#client_fetch_error "[object Object]" is not valid JSON {
  error: {
    message: '"[object Object]" is not valid JSON',
    stack: 'SyntaxError: "[object Object]" is not valid JSON\n' +
      '    at JSON.parse (<anonymous>)\n' +
      '    at parseJSONFromBytes (node:internal/deps/undici/undici:4553:19)\n' +
      '    at successSteps (node:internal/deps/undici/undici:4527:27)\n' +
      '    at fullyReadBody (node:internal/deps/undici/undici:1307:9)\n' +
      '    at process.processTicksAndRejections (node:internal/process/task_queues:95:5)\n' +
      '    at async specConsumeBody (node:internal/deps/undici/undici:4536:7)',
    name: 'SyntaxError'
  },
  url: 'http://localhost:3000/api/auth/session',
  message: '"[object Object]" is not valid JSON'
}
```

### 参考
https://github.com/nextauthjs/next-auth/discussions/3386