---
title: "「Classification Model」と「Object Detection」モデルの違い" 
emoji: "😸" # アイキャッチとして使われる絵文字（1文字だけ）
type: "tech" # tech: 技術記事 / idea: アイデア記事
topics: [] # タグ。["markdown", "rust", "aws"]のように指定する
published: false # 公開設定（falseにすると下書き）
---

# TensorFlowのモデル

## TensorFlowのモデルには大きく２つの目的がある。
- 分類を目的としたモデルは一般的に「分類モデル」(Classification Model)
- 物体の位置情報や境界ボックスの座標を提供するタスクは「物体検出」(Object Detection)


## Classification Modelのサンプル
```
import os
import numpy as np
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.utils import to_categorical
import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

# 画像ファイルのパス
from tensorflow.python.keras.layers import Activation

IMG_SIZE = 64


# モデルの作成とトレーニング
data = []
labels = []
classes = ["cat", "dog"]

for c in classes:
    path = os.path.join(os.getcwd(), c)
    for img in os.listdir(path):
        try:
            img_path = os.path.join(path, img)
            image = cv2.imread(img_path)
            image = cv2.resize(image, (IMG_SIZE, IMG_SIZE))
            data.append(image)
            labels.append(classes.index(c))
            print(img_path)
        except Exception as e:
            print(e)

data = np.array(data)
labels = np.array(labels)

# データをシャッフルする
idx = np.arange(data.shape[0])
np.random.shuffle(idx)
data = data[idx]
labels = labels[idx]

# データをトレーニング用と検証用に分割する
num_samples = len(data)
num_train = int(num_samples * 0.8)
x_train = data[:num_train]
y_train = labels[:num_train]
x_val = data[num_train:]
y_val = labels[num_train:]

# 画像データの正規化
x_train = x_train / 255.0
x_val = x_val / 255.0

# ラベルをone-hotエンコーディングに変換する
y_train = to_categorical(y_train)
y_val = to_categorical(y_val)

# モデルを構築する
model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=x_train.shape[1:]))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation("relu"))
model.add(Dense(2))
model.add(Activation("softmax"))

# モデルをコンパイルする
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# モデルをトレーニングする
model.fit(x_train, y_train, epochs=10, batch_size=32, validation_data=(x_val, y_val))

# GUIの作成
root = tk.Tk()
root.title("Cat or Dog Classifier")
root.geometry("500x500")


def imread(filename, flags=cv2.IMREAD_COLOR, dtype=np.uint8):
    try:
        n = np.fromfile(filename, dtype)
        img = cv2.imdecode(n, flags)
        return img
    except Exception as e:
        print(e)
        return None


# ボタンのクリック時の処理
def predict():
    # 画像を選択する
    file_path = filedialog.askopenfilename()

    # 選択された画像を表示する
    image_tk = Image.open(file_path).resize((IMG_SIZE, IMG_SIZE))
    image_tk = ImageTk.PhotoImage(image_tk)
    img_label.configure(image=image_tk)
    img_label.image = image_tk
    print(file_path)

    # 選択された画像をモデルに入力して予測結果を表示する
    image_selected = imread(file_path)
    image_selected = cv2.resize(image_selected, (IMG_SIZE, IMG_SIZE))
    image_selected = np.expand_dims(image_selected, axis=0)
    image_selected = image_selected / 255.0
    prediction = model.predict(image_selected)
    if np.argmax(prediction) == 0:
        result_label.configure(text="This is a cat!")
    else:
        result_label.configure(text="This is a dog!")


# 画像を表示するラベルの作成
img_label = tk.Label(root)
img_label.pack()

# 予測結果を表示するラベルの作成
result_label = tk.Label(root, font=("Helvetica", 18))
result_label.pack()

# ボタンの作成
button = tk.Button(root, text="Choose Image", command=predict)
button.pack()

root.mainloop()

```