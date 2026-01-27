---
title: "【完全無料】ポートフォリオを爆速で強化！Gemini APIを使って「普通のアプリ」を「AIアプリ」に進化させる方法"
emoji: "🚀"
type: "tech"
topics: ["Gemini", "AI", "API", "ポートフォリオ", "初心者"]
slug: "gemini-api-ai-app-upgrade-guide"
published: true
---

# 【完全無料】ポートフォリオを爆速で強化！Gemini APIを使って「普通のアプリ」を「AIアプリ」に進化させる方法

「ポートフォリオに差別化要素が欲しい」
「AI機能を組み込んでみたいけど、難しそうだしお金がかかりそう」

そんな悩みを抱えている開発者の方、多いのではないでしょうか？
実は、Googleが提供する **Gemini API** を使えば、**高性能なAI機能を無料**で、しかも**驚くほど簡単に**皆さんのアプリに追加できるんです。

この記事では、Gemini APIを使って「普通のアプリ」を「今っぽいAIアプリ」にアップグレードする方法と、そのメリットを紹介します。

## Gemini API が最強な理由

現在、OpenAIやAnthropicから強力なLLMモデルがありますが、個人開発において私が **Gemini API** を推す理由は以下の2点です。

### 1. 圧倒的なコストパフォーマンス（無料枠がすごい）

Gemini API（特に `Gemini 2.5 Flash` や `Gemini 2.5 Flash-Lite`）は、Google AI Studio経由で利用する場合、**無料枠（Free Tier）** が非常に寛容です。

- **高性能・高速**: Gemini 2.5 Flashは軽量ながら非常に賢く、レスポンスが高速です。価格性能のバランスに優れています。
- **最新モデル**: 2026年現在、AI Studioでは最新の `Gemini 3 Flash` や `Gemini 3 Pro` も標準的に選択でき、より高度な機能も無料で試せます。
- **無料**: 一定のレート制限（Rate Limits）内であれば、クレジットカード登録なしで無料で使い続けられます。
  - ※2026年時点での情報です。最新の制限は公式サイトをご確認ください。

学習用やポートフォリオ用であれば、無料枠を使い切ることはそうそうありません。

### 2. マルチモーダル対応

テキストだけでなく、画像や音声も理解できるため、アイデア次第で実装できる機能の幅が広がります。

## Google AI Studio での APIキー取得方法

まずはAPIキーを取得しましょう。3分で終わります。

1.  [Google AI Studio](https://aistudio.google.com/) にアクセスし、Googleアカウントでログインします。
2.  左上の **"Get API key"** をクリックします。
3.  **"Create API key"** をクリックし, 既存のGoogle Cloudプロジェクトを選択するか、新しくプロジェクトを作成します。
    ![Google AI Studio APIキー取得画面](https://github.com/Inosuke0718/Zenn/blob/main/images/get-gemini-api-key.png?raw=true)
4.  生成されたキーをコピーして完了です！

- ※APIキーは`.env`ファイルなどで厳重に管理し、GitHub等に流出させないように注意しましょう。

## 「ちょい足し」でアプリを進化させるアイデア集

ここが本題です。皆さんが既に持っている、あるいはこれから作るアプリにAIを「ちょい足し」するだけで、機能性が一気に向上します。

### 例1：TODOアプリ × 要約・アドバイス

よくあるTODOリストも、AIがあれば専属コーチに早変わりします。

- **Before**: タスクを追加して消化するだけ。
- **After**:
  - 「今日のタスク量、多すぎない？優先順位をつけて！」とボタン一つでAIがスケジュールを提案。
  - 「ダイエット」というタスクに対し、「具体的なアクションプラン（食事制限、運動メニュー）」を自動生成してサブタスクに追加。

### 例2：日記・チャットアプリ × 感情分析

- **Before**: テキストを投稿して保存するだけ。
- **After**:
  - 投稿内容からAIが感情（喜び、怒り、悲しみ）を分析し、UIの背景色をフワッと変化させる。
  - ネガティブな投稿に対して、AIキャラクターが励ましのコメントを自動返信してくれる。

### 例3：チャットアプリ × 音声読み上げ・翻訳

- **Before**: 文字のやり取りだけ。
- **After**:
  - 外国語のメッセージをリアルタイムで翻訳。
  - 受け取ったメッセージを「関西弁のキャラクター」として読み上げさせる（テキスト変換指示＋音声機能）。

## 実装イメージ：3つの言語での書き方

Gemini APIは非常に扱いやすく、主要な言語であればすぐに動かすことができます。ここでは **Node.js (Next.js)**、**Python**、**Java** の3パターンを紹介します。

### 1. Node.js / Next.js の場合

公式の `@google/generative-ai` パッケージを使えば、直感的に記述できます。

```bash
npm install @google/generative-ai
```

```javascript
import { GoogleGenerativeAI } from "@google/generative-ai";

// 環境変数からAPIキーを取得
const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);

export async function getAiResponse(userMessage) {
  // 高速＆低コストな Gemini 2.5 Flash モデルを指定
  const model = genAI.getGenerativeModel({ model: "gemini-2.5-flash" });

  const prompt = `以下のタスクに対してアドバイスをください: ${userMessage}`;

  const result = await model.generateContent(prompt);
  const response = await result.response;
  return response.text();
}
```

### 2. Python の場合

データ分析やAI開発で人気のPythonも、公式SDKを使えばわずか数行です。FlaskやFastAPI、Streamlitで作るアプリに最適です。

```bash
pip install -q -U google-generativeai
```

```python
import google.generativeai as genai
import os

# APIキーの設定
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def get_ai_response(user_message):
    # モデルの準備 (価格性能バランスのよい Gemini 2.5 Flash)
    model = genai.GenerativeModel("gemini-2.5-flash")

    # コンテンツ生成
    response = model.generate_content(f"以下のタスクにアドバイスをください: {user_message}")

    return response.text

# 実行例
if __name__ == "__main__":
    print(get_ai_response("ダイエットしたいけど続かない"))
```

### 3. Java の場合

Java（Spring Bootなど）で開発している場合、外部ライブラリを入れずに標準の `HttpClient` (Java 11以降) でREST APIを叩くのが最も手軽です。
※本格的な開発では **Spring AI** や **LangChain4j** の利用もおすすめです。

```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.http.HttpRequest.BodyPublishers;

public class GeminiService {
    private static final String API_KEY = System.getenv("GEMINI_API_KEY");
    // エンドポイントURL (最新の Gemini 2.5 Flash を使用)
    private static final String API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=" + API_KEY;

    public String getAiResponse(String userMessage) {
        try {
            // リクエストボディの作成（簡易的なJSON構築）
            // 実際はJacksonやGsonを使うことを推奨します
            String jsonBody = String.format(
                "{ \"contents\": [{ \"parts\": [{ \"text\": \"以下のタスクにアドバイスをください: %s\" }] }] }",
                userMessage
            );

            HttpClient client = HttpClient.newHttpClient();
            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create(API_URL))
                    .header("Content-Type", "application/json")
                    .POST(BodyPublishers.ofString(jsonBody))
                    .build();

            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

            // レスポンスのJSONからテキスト部分を抽出する処理が必要です
            return response.body();

        } catch (Exception e) {
            e.printStackTrace();
            return "エラーが発生しました";
        }
    }
}
```

どの言語を使っても、**「APIキーをセットする」「モデルを選ぶ」「プロンプトを送る」** という3ステップは共通です。まずは使い慣れた言語で試してみてください！

## 結論：就活用ポートフォリオのクオリティを上げよう

採用担当者は多くのポートフォリオを見ています。
ありきたりなチュートリアル通りのアプリではなく、**「APIを活用して、ユーザーにどんな価値を提供できるか」** を考えられたアプリは目に留まります。

Gemini APIなら、コストゼロでその「工夫」を実現できます。

ぜひ、皆さんの手元のプロジェクトに `npm install` して、AIの力を借りてみてください。アプリ開発がもっと楽しくなるはずです！

## 参考リンク

- [Google AI Studio](https://aistudio.google.com/)
- [Gemini API ドキュメント](https://ai.google.dev/docs)
