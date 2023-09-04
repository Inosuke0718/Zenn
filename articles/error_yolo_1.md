---
title: "エラーIndexError: index 1 is out of bounds for dimension 1 with size 1の解決方法"
emoji: "😸" # アイキャッチとして使われる絵文字（1文字だけ）
type: "tech" # tech: 技術記事 / idea: アイデア記事
topics: [] # タグ。["markdown", "rust", "aws"]のように指定する
published: false # 公開設定（falseにすると下書き）
---

# エラーIndexError: index 1 is out of bounds for dimension 1 with size 1

## 原因
ラベルのIDと設定ファイルのクラス数（nc）の不一致
ラベルに ID 0 と 1 があり、構成で nc=1 を設定している場合、このエラーが発生します。

## 解決方法
検出したいTargetが一つだけの場合は、data.yamlのncを1にする。
```
train: ./train/images
val: ./valid/images

nc: 1
names: ['surfer']
```

そしてラベルのクラスIDが全て0であることを確認する
0 0.480273 0.328488 0.259766 0.647287


その後、labels.cacheを削除し、再実行すればエラー解決！

## 参考
https://github.com/ultralytics/ultralytics/issues/472