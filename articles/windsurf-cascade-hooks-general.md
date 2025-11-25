---
title: "Windsurf Hooks 入門：AI 開発を自動化する全能テクニック"
emoji: "🏄"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ["windsurf", "cursor", "ai", "automation", "devtools"]
published: true
---

Windsurf の強力な AI エージェント "Cascade" には、**「Cascade Hooks (Beta)」** という隠れた（しかし公式の）機能があります。

これは「AI がファイルを読んだとき」「コマンドを実行したとき」などのイベントをフックして、**任意のスクリプトを自動実行できる** 仕組みです。
Cursor の `.cursorrules` や Hooks に似ていますが、Windsurf ではシェルスクリプトや Python を直接呼び出せるため、**OS レベルでの自由な自動化** が可能です。

この記事では、言語やフレームワークを問わず使える **「汎用的な Hooks 設定とスクリプト」** を紹介します。

## Hooks の基本

Hooks は `.windsurf/hooks.json` という設定ファイルで管理します。
Cascade が特定のアクションを行うと、設定されたコマンドに **JSON 形式のイベント情報** が標準入力で渡されます。

### 利用できる主なイベント
- **pre_read_code / post_read_code**: AI がファイルを読む前後
- **pre_write_code / post_write_code**: AI がファイルを編集する前後
- **pre_run_command / post_run_command**: AI がターミナルコマンドを実行する前後

---

## 準備：設定ファイルの作成

まずはプロジェクトのルート（または `~/.codeium/windsurf/`）に設定ディレクトリを作ります。

```
.windsurf/
  ├── hooks.json        # 設定のエントリーポイント
  └── hooks/            # スクリプトを置く場所
```

---

## レシピ 1: 保存時に自動フォーマット（言語汎用版）

AI がコードを修正した直後に、そのファイルの拡張子に応じて適切なフォーマッタを実行します。
これを入れておくと、AI 特有のインデント崩れやスタイル違反を気にせず開発できます。

### `.windsurf/hooks.json`

```json
{
  "hooks": {
    "post_write_code": [
      {
        "command": "bash .windsurf/hooks/format.sh",
        "show_output": false
      }
    ]
  }
}
```

### `.windsurf/hooks/format.sh`

```bash
#!/usr/bin/env bash
# 標準入力からコンテキストを取得
input=$(cat)
# jq で変更されたファイルのパスを抽出
file_path=$(echo "$input" | jq -r '.tool_info.file_path')

case "$file_path" in
  # JavaScript / TypeScript / JSON / Markdown
  *.js|*.jsx|*.ts|*.tsx|*.json|*.md)
    if command -v prettier >/dev/null 2>&1; then
      npx prettier --write "$file_path"
    fi
    ;;
  
  # Python
  *.py)
    if command -v black >/dev/null 2>&1; then
      black "$file_path"
    fi
    ;;

  # Go
  *.go)
    if command -v gofmt >/dev/null 2>&1; then
      gofmt -w "$file_path"
    fi
    ;;

  # Rust
  *.rs)
    if command -v rustfmt >/dev/null 2>&1; then
      rustfmt "$file_path"
    fi
    ;;
esac

exit 0
```

---

## レシピ 2: 長時間コマンドの完了通知

AI に「テスト全部回して」や「ビルドして」と頼んだ後、別の作業をしていても完了に気づけるようにします。

### `.windsurf/hooks.json`

```json
{
  "hooks": {
    "post_run_command": [
      {
        "command": "python3 .windsurf/hooks/notify.py",
        "show_output": false
      }
    ]
  }
}
```

### `.windsurf/hooks/notify.py` (Python)

特定のキーワード（build, test, install 等）を含むコマンドが終わったときだけ通知を出します。

```python
#!/usr/bin/env python3
import sys, json, subprocess, platform

data = json.loads(sys.stdin.read())
cmd = data.get("tool_info", {}).get("command_line", "")

# 通知対象にするコマンドのキーワード
WATCH_KEYWORDS = ["build", "test", "install", "docker-compose up"]

if any(k in cmd for k in WATCH_KEYWORDS):
    message = f"Command finished: {cmd}"
    
    if platform.system() == "Darwin": # macOS
        subprocess.run(["osascript", "-e", f'display notification "{message}" with title "Windsurf Cascade"'])
    elif platform.system() == "Windows": # Windows (PowerShell)
        subprocess.run(["powershell", "-Command", f"New-BurntToastNotification -Text '{message}'"], shell=True)
    # Linux なら notify-send など
    
sys.exit(0)
```

---

## レシピ 3: 機密ファイルの読み込みブロック（セキュリティ）

AI が誤って `.env` ファイルや SSH 鍵などを読み込もうとした場合に、強制的にブロックします。
企業利用や配信中の利用で特に有効です。

### `.windsurf/hooks.json`

```json
{
  "hooks": {
    "pre_read_code": [
      {
        "command": "bash .windsurf/hooks/security-check.sh",
        "show_output": true
      }
    ]
  }
}
```

### `.windsurf/hooks/security-check.sh`

終了コード `1` (または非ゼロ) を返すと、Windsurf はそのアクションをキャンセルします。

```bash
#!/usr/bin/env bash
input=$(cat)
file_path=$(echo "$input" | jq -r '.tool_info.file_path')

# ブロックしたいファイル名のパターン
if [[ "$file_path" == *".env"* || "$file_path" == *".ssh"* || "$file_path" == *"aws/credentials"* ]]; then
  echo "🚫 Access denied by Hooks: Sensitive file access is blocked."
  exit 1 # ここでエラーを返すと、Cascade は読み込みに失敗する
fi

exit 0
```

---

## レシピ 4: AI の行動ログ（監査用）

AI が「いつ」「どのファイルを」変更したかをログに残します。
Git の履歴だけでは追いきれない、AI との試行錯誤のプロセスを記録できます。

### `.windsurf/hooks.json`

```json
{
  "hooks": {
    "post_write_code": [
      { "command": "python3 .windsurf/hooks/logger.py" }
    ],
    "post_run_command": [
      { "command": "python3 .windsurf/hooks/logger.py" }
    ]
  }
}
```

### `.windsurf/hooks/logger.py`

```python
#!/usr/bin/env python3
import sys, json, datetime, os

LOG_FILE = os.path.expanduser("~/.windsurf/cascade_history.log")
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

data = json.loads(sys.stdin.read())
event = data.get("agent_action_name")
timestamp = datetime.datetime.now().isoformat()

with open(LOG_FILE, "a", encoding="utf-8") as f:
    f.write(f"[{timestamp}] {event}\n")
    f.write(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    f.write("-" * 40 + "\n")

sys.exit(0)
```

---

## まとめ

Windsurf の Cascade Hooks は、**「AI の行動に対するミドルウェア」** のようなものです。

- **品質担保**: 自動フォーマット、Lint
- **効率化**: 長時間タスクの通知
- **安全性**: 機密ファイルへのアクセス制御
- **透明性**: 行動ログの記録

これらを組み合わせることで、単なるコード生成ツールを超えた、自分好みの最強の開発パートナーを作ることができます。ぜひ試してみてください。
