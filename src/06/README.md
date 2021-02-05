# BoW 表現

BoW 表現を用いて，RCC 総会文書の類似度算出及び分類をします。

## 実行環境

- Python 3.0
- OS: Ubuntu

## 使い方

### 1. 総会文書をダウンロード

```sh
$ ./fetch_data.sh
```

### 2. ライブラリをインストール

```sh
$ pip install -U pip
$ pip install sklearn
```

### 3. 前処理

tex 形式を txt に変換する前処理を行い，処理後のテキストを`text`ディレクトリに作成します。

```sh
$ python preprocessing.py
```

### 4. 総会文書のコピペチェック

局ごとの総会文書コピペチェックをします。`similarity.py`の`TARGET`でチェック対象の局を指定できます。

```sh
$ python similarity.py
```
