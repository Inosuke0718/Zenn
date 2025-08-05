---
title: "【完全ガイド】夜間にAIがIssueを自動実装するGitHub Actions＋Claude Code活用法"
emoji: "🤖"
type: "tech"
topics: ["github", "githubactions", "ai", "claude", "automation"]
published: true
---

# 【完全ガイド】夜間に AI が Issue を自動実装する GitHub Actions ＋ Claude Code 活用法

ソフトウェア開発の効率化に AI を活用できる「Claude Code GitHub Actions」。本記事では、深夜に未処理 Issue を自動でピックアップし、AI が実装から PR 作成まで行うワークフローを、ブログ向けにまとめます。

## 1. はじめに

- **課題**: 夜間に発生した Issue を翌朝まとめて確認・実装するのは手間
- **解決策**: GitHub Actions のスケジュール＋ Claude Code Action で、夜間自動処理
- **効果**: 朝起きたら AI が生成した PR がずらり。レビューするだけで完了

## 2. 全体フロー

1. GitHub Issues に`@claude`メンションとともに実装してほしい内容を記載して投稿
2. GitHub Actions が"夜間"を判定し定期実行
3. 未処理 Issue を優先度順（high→middle→low）に検索
4. Claude Code Action がコメントを検知し、実装 →PR 作成

## 3. ワークフロー設定

### 3.1 ファイル設置場所

リポジトリのルート下、次のパスにワークフローファイル（YAML）を配置します。

```
.github/
└─ workflows/
   └─ auto-issue-resolver.yml
```

ファイル名は任意ですが、分かりやすい名前にしましょう。

### 3.2 schedule トリガーの記述

```yaml
name: Auto Issue Resolver

on:
  schedule:
    - cron: "0,30 14-20 * * *" # JST 23:00-05:30 (UTC 14:00-20:30)
    - cron: "0 21 * * *" # JST 06:00 (UTC 21:00)
  workflow_dispatch: # 手動実行用

jobs:
  process-issue:
    runs-on: ubuntu-latest
    steps:
      - name: Find and process highest priority Issue
        uses: actions/github-script@v7
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          script: |
            const priorities = ['high','middle','low'];
            const processedLabel = 'claude-code-requested';

            for (const priority of priorities) {
              const issues = await github.rest.issues.listForRepo({
                owner: context.repo.owner,
                repo: context.repo.repo,
                labels: priority,
                state: 'open',
                sort: 'created',
                direction: 'desc',
                per_page: 100
              });
              const issue = issues.data.find(i =>
                !i.labels.some(l => l.name === processedLabel)
              );
              if (issue) {
                await github.rest.issues.createComment({
                  owner: context.repo.owner,
                  repo: context.repo.repo,
                  issue_number: issue.number,
                  body: [
                    `@claude このIssue #${issue.number} を解決してください。`,
                    '',
                    '**タイトル**: ' + issue.title,
                    '',
                    '**説明**:',
                    issue.body || '説明なし',
                    '',
                    `優先度: ${priority}`
                  ].join('\n')
                });
                await github.rest.issues.addLabels({
                  owner: context.repo.owner,
                  repo: context.repo.repo,
                  issue_number: issue.number,
                  labels: [processedLabel]
                });
                console.log('Triggered Claude Code Action for Issue #' + issue.number);
                return;
              }
            }
            console.log('No unprocessed issues found');
```

- `cron`は UTC 基準。JST との変換に注意
- `workflow_dispatch`で手動実行も可能

## 7. まとめ

夜間の定期トリガー ×Claude Code で、眠っている間に Issue を次々と解決。
朝はレビューだけで OK な、まさに"寝ている間も動く開発チーム"を実現しましょう。

## 8. 参考文献

- [GitHub Actions で Claude 3.5 Sonnet を使ったコード生成の自動化](https://zenn.dev/r_kaga/articles/731fe4636289dc) - r_kaga
- [Claude Code GitHub Actions - Anthropic](https://docs.anthropic.com/ja/docs/claude-code/github-actions)
