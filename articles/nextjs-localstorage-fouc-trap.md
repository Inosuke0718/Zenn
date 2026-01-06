---
title: "Next.jsでLocalStorageの状態復元にハマった話：FOUCとキー不一致の二重罠"
emoji: "💾"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ["nextjs", "react", "localstorage", "typescript", "hooks"]
published: false
---

# はじめに

Next.js アプリケーション開発において、「ユーザーが開いていたタブの状態をリロード後も維持したい」という要件はよくあります。
一見、LocalStorage を使えば簡単に実装できそうですが、SSR（Server-Side Rendering）と組み合わせた際に特有の挙動や、カスタムフックの些細な仕様により、**「画面が一瞬ちらつく」「保存したはずの状態が消える」** という問題に遭遇しました。

この記事では、その原因と解決までのプロセスを共有します。

# 遭遇した現象

開発していたのは、スポーツのコート割り振りアプリです。
アプリには「コート」「ランキング」「プレイヤー」「設定」の 4 つのタブがあり、ユーザーがタブを切り替えた情報を LocalStorage に保存して、次回アクセス時やリロード時に復元する機能を実装しようとしていました。

しかし、以下の 2 つの問題が発生しました。

1.  **FOUC (Flash of Unstyled Content) のような現象**:
    「プレイヤー」タブを開いている状態でリロードすると、一瞬デフォルトの「コート」タブが表示されてから、「プレイヤー」タブに切り替わる。
2.  **状態のリセット（上書き）**:
    さらに悪いことに、場合によってはリロード後にデフォルトの「コート」タブに戻ってしまい、保存したはずの情報が失われる。

# 原因の深掘り

調査の結果、原因は以下の 3 つの要素が絡み合っていました。

## 1. SSR と Hydration のタイミング (FOUC の原因)

Next.js (App Router) では、初回レンダリングはサーバー側で行われます（SSR）。サーバーには `localStorage` が存在しないため、初期状態（今回は「コート」タブ）で HTML が生成されます。

クライアント側で JS が実行（Hydration）された後、`useEffect` で LocalStorage から値を読み込んで状態を更新していましたが、このタイムラグにより**「初期状態 → 保存された状態」**への切り替わりが目に見えてしまい、画面のちらつきが発生していました。

## 2. 状態保存ロジックによる上書き

状態の保存（LocalStorage への書き込み）を、State の変更を検知する `useEffect` で行っていました。

```typescript
// 修正前のコードイメージ
useEffect(() => {
  // stateが変更されたら保存
  localStorage.setItem("key", JSON.stringify(state));
}, [state]);
```

しかし、前述の通り、アプリ起動時はまず「初期状態（デフォルト値）」で始まります。
復元処理が完了する前に、この保存処理が走ってしまい、**「LocalStorage に残っていた正しいデータ」を「デフォルト値」で上書きしてしまう** という事故が起きていました。

## 3. カスタムフックのプレフィックス (キー不一致)

これが一番の盲点でした。
`useLocalStorage` というカスタムフックを利用していましたが、このフック内部でキー名の衝突を防ぐためにプレフィックス（`nextwho-`）を自動付与する仕様になっていました。

一方、復元ロジックを実装した `useGameState` フック側では、その仕様を失念して生のキー名（`game-state`）で読み込もうとしていました。

- **保存時**: `nextwho-game-state` に保存される
- **読取時**: `game-state` を読みに行き、データが見つからない
- **結果**: 常に初期状態でスタートし、その初期状態で上書き保存される

# 解決策

これらの問題を解決するために、以下の対応を行いました。

## 1. `isHydrated` パターンの導入

クライアントサイドでのマウント（復元）が完了したことを保証するフラグ `isHydrated` を導入しました。

```typescript
// useGameState.ts

const [isHydrated, setIsHydrated] = useState(false);
const hasRestoredRef = useRef(false);

// 復元ロジック
useEffect(() => {
  if (hasRestoredRef.current) return;
  hasRestoredRef.current = true;

  try {
    // 正しいキー（プレフィックス付き）で読み込む
    const saved = localStorage.getItem(FULL_STORAGE_KEY);
    if (saved) {
      const parsed = JSON.parse(saved);
      dispatch({ type: "RESTORE_STATE", payload: parsed });
    }
  } catch (e) {
    console.error(e);
  }

  // 復元完了フラグを立てる
  setIsHydrated(true);
}, []);
```

## 2. 保存処理のガード

`isHydrated` が `true` になるまで（つまり、LocalStorage からの復元が完了するまで）は、LocalStorage への書き込みを行わないようにガードを入れました。これにより、デフォルト値による誤った上書きを防げます。

```typescript
// 保存ロジック
useEffect(() => {
  // 復元が完了するまでは保存しない！
  if (!isHydrated) return;

  // ...保存処理
}, [isHydrated, state]); // 依存配列にisHydratedを追加
```

## 3. 正しいキーの使用

復元ロジックで読み込むキーに、プレフィックスを含めた正しいキー名を指定するように修正しました。

```typescript
// useLocalStorageの仕様に合わせてプレフィックスを追加
const STORAGE_KEY = "game-state";
const FULL_STORAGE_KEY = "nextwho-" + STORAGE_KEY;

// ...
const saved = localStorage.getItem(FULL_STORAGE_KEY);
```

## 4. UI 側でのローディング制御

`page.tsx` 側でも `isHydrated` フラグを受け取り、復元が完了するまではローディング画面を表示するようにしました。これにより、一瞬デフォルトタブが表示される「ちらつき」を完全に防ぐことができました。

```tsx
// page.tsx
if (!isHydrated) {
  return <LoadingScreen />;
}

return <AppContent ... />;
```

# まとめ

Next.js で LocalStorage を扱う際は、以下の点に注意が必要です。

1.  **SSR との兼ね合い**: サーバーとクライアントで不整合が起きないよう、タイミングを制御する。
2.  **初期化の順序**: 「復元してから保存」という順序を強制するために、フラグ（`isHydrated`）を活用する。
3.  **キーの管理**: カスタムフックやライブラリがキーを加工していないかを確認する。

特に「復元完了前に保存が走ってデータが消える」現象は、非同期処理が絡む React の状態管理でハマりやすいポイントですので、同様の現象に悩んでいる方の参考になれば幸いです。
