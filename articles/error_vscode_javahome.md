---
title: "The supplied javaHome seems to be invalid 解決方法"
emoji: "😸" # アイキャッチとして使われる絵文字（1文字だけ）
type: "tech" # tech: 技術記事 / idea: アイデア記事
topics: [] # タグ。["markdown", "rust", "aws"]のように指定する
published: true # 公開設定（falseにすると下書き）
---

# エラー:VSCodeにてFlutter開発中にThe supplied javaHome seems to be invalidに遭遇

## Error内容
```
###Errorの内容###
Could not run phased build action using connection to Gradle distribution 'https://services.gradle.org/distributions/gradle-7.4.2-bin.zip'.
The supplied javaHome seems to be invalid. I cannot find the java executable. Tried location: C:\Program Files\Microsoft\jdk-11.0.16.101-hotspot\bin\java.exe

###Errorの発生箇所###
buildscript

###Errorが発生している箇所のコード全文###
buildscript {
    ext.kotlin_version = '1.3.50'
    repositories {
        google()
        mavenCentral()
    }

    dependencies {
        classpath 'com.android.tools.build:gradle:7.4.1'
        classpath "org.jetbrains.kotlin:kotlin-gradle-plugin:$kotlin_version"
    }
}

allprojects {
    repositories {
        google()
        mavenCentral()
    }
}

rootProject.buildDir = '../build'
subprojects {
    project.buildDir = "${rootProject.buildDir}/${project.name}"
    project.evaluationDependsOn(':app')
}

task clean(type: Delete) {
    delete rootProject.buildDir
}
```

## 原因
VSCodeのExtensionである”Extension Pack for Java”がJAVA_HOMEの環境変数をOverrideしていた模様。

Terminalでecho $JAVA_HOMEと打っても正しいパスが表示されるので、解決にすごく時間がかりました。

## 解決方法
”Extension Pack for Java”をVSCodeで削除

