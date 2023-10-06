---
title: "OpenCVのTrackingモデルDaSiamRPNの読み込みエラーCan't read ONNX file: dasiamrpn_model.onnx"の解決方法
emoji: "😸" # アイキャッチとして使われる絵文字（1文字だけ）
type: "tech" # tech: 技術記事 / idea: アイデア記事
topics: ["OpenCV", "Android Studio", "java"] # タグ。["markdown", "rust", "aws"]のように指定する
published: false # 公開設定（falseにすると下書き）
---

# dasiamrpn_modelが読み込めない
AndroioプロジェクトでOpenCVのTrackerモデルの一つであるDaSiamRPNを使おうとするが、エラーが発生し読み込めませんでした。

## Error内容
```
OpenCV(4.6.0) Error: Bad argument (Can't read ONNX file: dasiamrpn_model.onnx) in ONNXImporter, file D:~~~\opencv\src\opencv\modules\dnn\src\onnx\onnx_importer.cpp, line 198
The terminal process "C:\...\bash.exe '-l', '-c', 'g++.exe -o "E:\...\Test"/bin/main.exe -I "E:\...\Test"/headers -I "D:/.../include" -ggdb "E:\...\Test"/source/*.cpp "D:/.../install/lib/**.a" && "E:\...\Test"/bin/main.exe'" terminated with exit code: 3.
```
エラーを見てみるとdasiamrpn_model.onnxというファイルが必要な模様。。

## 解決方法
### dasiamrpnを利用するための以下3つのmodelファイルをDLする
- network:     https://www.dropbox.com/s/rr1lk9355vzolqv/dasiamrpn_model.onnx?dl=0
- kernel_r1:   https://www.dropbox.com/s/999cqx5zrfi7w4p/dasiamrpn_kernel_r1.onnx?dl=0
- kernel_cls1: https://www.dropbox.com/s/qvmtszx5h339a0w/dasiamrpn_kernel_cls1.onnx?dl=0

### modelファイルを設置
設置場所はAndroidプロジェクトであれば、app/src/main/assetsに設置

### モデルをTrackerDaSiamRPNに読み込ませる
```
@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);

    if(OpenCVLoader.initDebug()){
        try {
            // これを追加 ここから
            TrackerDaSiamRPN_Params params = new TrackerDaSiamRPN_Params();
            String modelPath = copyAssetToFile("dasiamrpn_model.onnx", this);
            String kernelCls1Path = copyAssetToFile("dasiamrpn_kernel_cls1.onnx", this);
            String kernelR1Path = copyAssetToFile("dasiamrpn_kernel_r1.onnx", this);
            params.set_model(modelPath);
            params.set_kernel_cls1(kernelCls1Path);
            params.set_kernel_r1(kernelR1Path);

            tracker = TrackerDaSiamRPN.create(params);
            // ここまで

        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
```

### 余談
DaSiamRPNは何やらTrackingの精度が良いらしいです。実際、私も試しましたがMILやGoTurnよりもDaSiamRPNの方が良さげでした。（自分の用途にはですが、）

このエラーは検索ではあまりHitしないので、誰かのお役に立てれば幸いです。

### 参考
https://forum.opencv.org/t/interesting-onnx-error-when-trying-to-set-rect-using-keypoints-variables/7416
https://github.com/opencv/opencv/blob/1605d1d24dc152db64b958b9cfddfddf5fceb714/samples/python/tracker.py#L8-L11
