# 環境構築

本プロジェクトでは，Pythonを使用します。
自然言語処理といえばPythonかRだと思いますが，

* R -> 研究やデータ分析オンリーで使われがち
* Python -> アプリケーションへ組み込みやすい

といった特徴があるので，今回はPythonを利用します。

ここではPython 3.8を使用しますが，フラッグシップが嫌いな方は別のバージョンでも構いません。


## Pythonをインストール
### Windowsへインストール
[参考記事](https://qiita.com/New_enpitsu_15/items/ee95bde0858e9f77acf0)に従ってPython 3.8をインストールしてください。

### macOS/Linuxへインストール
まずは，Pythonのバージョン管理ツールをインストールしましょう。

ターミナルで以下のコマンドを実行します。行頭の$はシェルでの実行を示す単なるマークであり，入力する必要はありません。

```sh
$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv

$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
# zshの場合は，.bash_profile -> .zshrcとしてください
```

続いてPython 3.8をインストールします。~~（現時点で3.8はTensorFlow非対応です）~~

```sh
$ pyenv install 3.8.2
$ pyenv global 3.8.2
```

以上でPythonのセットアップは完了です。

ターミナルで`python -V`と入力して`Python 3.8.2`と表示されれば成功です。

