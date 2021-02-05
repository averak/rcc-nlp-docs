# テキスト生成

マルコフ連鎖をつかって，rits_rcc ボットを作ります。

自身のツイッターデータを使えば，あなたボットを作ることも可能です。

## 実行環境

- Python 3.0
- OS: Ubuntu

## 使い方

### 1. ツイートデータを準備

[@rit_rcc データ](https://drive.google.com/file/d/1tFV8aejl9cZyMd2ueLLHOmXU-WNddg-v/view?usp=sharing)をダウンロードし，このディレクトリに配置してください。

### 2. ライブラリをインストール

```sh
$ pip install markovify
```

### 3. 前処理

ツイートデータからツイートテキストのみを抽出します。

```sh
$ python preprocessing.py
```

### 4. 学習

```sh
$ python train.py
```

### 5. テキスト生成！

```sh
$ python generator.py
```
