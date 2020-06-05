# 環境構築

本プロジェクトでは，Pythonを使用します。
自然言語処理といえばPythonかRだと思いますが，

* R -> 研究やデータ分析オンリーで使われがち
* Python -> アプリケーションへ組み込みやすい

といった特徴があるので，今回はPythonを利用します。


## Pythonをインストール
まずは，Pythonのバージョン管理ツールをインストールしましょう。

ターミナルで以下のコマンドを実行します。行頭の$はシェルでの実行を示す単なるマークであり，入力する必要はありません。

```sh
$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv

$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
```

続いてPython 3.8をインストールします。~~（現時点で3.8はTensorFlow非対応です）~~

```sh
$ pyenv install 3.7.6
$ pyenv global 3.7.6
```

以上でPythonのセットアップは完了です。

ターミナルで`python -V`と入力して`Python 3.7.6`と表示されれば成功です。
