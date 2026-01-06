---
title: "Next.jsのAPI Routesを“入口”にしてElysiaJSへ寄せる（同居構成）入門"
emoji: "⚡"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ["nextjs", "elysia", "typescript", "openapi"]
published: true
---

Next.js の API Routes を全部自前で育てると、型・バリデーション・OpenAPI（Swagger）を整えるのが徐々に大変になります。そこで、API 実装を ElysiaJS に寄せて、Next.js は「UI + API への入口」だけ担当する構成を紹介します。

Elysia は OpenAPI プラグインで Swagger ページを自動生成でき、スキーマから型推論と実行時検証を同時に効かせられます。

## ゴール（この記事で作るもの）

- Next.js の`/api/*`に来たリクエストを、同一プロセス内の Elysia へ渡す。
- Elysia 側でルート定義 + バリデーション（TypeBox）を書く。
- OpenAPI プラグインで Swagger UI を出す（まずは動くところまで）。

## セットアップ（依存関係）

Elysia 本体と、OpenAPI 用のプラグインを入れます（bun でも npm/pnpm でも OK）。
Elysia の OpenAPI は`@elysiajs/openapi`を追加して`.use(openapi())`するだけで Swagger ページ生成が可能です。

```bash
# bunの例
bun add elysia @elysiajs/openapi
```

## Elysia 側（API の本体）を作る

`src/server/elysia.ts` のような場所に「Elysia アプリ本体」を作ります。OpenAPI を有効化し、サンプルとして GET と POST を用意します。

```ts
// src/server/elysia.ts
import { Elysia, t } from "elysia";
import { openapi } from "@elysiajs/openapi";

export const api = new Elysia({ prefix: "/api" })
  .use(openapi()) // Swaggerページを自動生成
  .get("/health", () => ({ ok: true }))
  .post("/mirror", ({ body }) => body, {
    body: t.Object({
      id: t.Number(),
      name: t.String(),
    }),
  });
```

- `prefix: '/api'` を付けて、Elysia 側の API を `/api/...` に揃えています（Next.js 側の`/api/*`と合わせやすい）。
- OpenAPI の詳細（summary/tags など）も`detail`で付けられ、OpenAPI v3 に沿って型安全に書けます。

## Next.js 側（入口）で catch-all プロキシを作る

次に、Next.js の Route Handler で`/api/*`を catch-all して、Elysia へ渡します。Next.js はルーティングの仕組みとして Dynamic Routes を提供しているので、これを利用します。

例（App Router 想定）:

```
src/app/api/[...path]/route.ts
```

```ts
// src/app/api/[...path]/route.ts
import { api } from "@/server/elysia";

export const runtime = "nodejs"; // Nodeランタイムで動かす（まずはここから）

async function handler(req: Request) {
  // Next.jsのRequestをElysiaに渡して処理してもらい、Responseを返すイメージ
  return api.handle(req);
}

export {
  handler as GET,
  handler as POST,
  handler as PUT,
  handler as PATCH,
  handler as DELETE,
};
```

この形にすると、`/api/health` や `/api/mirror` へのアクセスは Next.js の `/api/[...path]` に入り、最終的な処理は `api.handle(req)` で Elysia に寄ります（＝同居）。

## Swagger（OpenAPI UI）を見てみる

Elysia は OpenAPI プラグインで Swagger ページ（Scalar UI）を自動生成します。
どのパスに出るかは設定次第ですが、少なくとも「OpenAPI プラグインを入れるとドキュメントページが生成される」ことがこの記事の到達点です。
必要なら `openapi({ path: '/v2/openapi' })` のようにエンドポイントを変えられます。

## 型安全クライアント（Eden Treaty）は後で追加で OK

フロントから型安全に呼びたい場合は、Eden Treaty で「サーバー型（`typeof app`）」をクライアントに渡す方法があります。
Treaty はパスをツリー構造（`.hi.get()` など）で扱い、動的パスは関数呼び出しで表現します。
同居構成が動いてから導入した方が混乱が少ないので、この記事では“次のステップ”扱いにするのがおすすめです。

---

### 参考リンク

- [Eden Treaty Overview](https://elysiajs.com/eden/treaty/overview)
- [Elysia OpenAPI Patterns](https://elysiajs.com/patterns/openapi)
- [Next.js Dynamic Routes](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes)
