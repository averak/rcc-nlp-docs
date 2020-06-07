# 基礎技術

このチャプターでは，自然言語処理の基礎技術について解説していきます。

基礎技術には，一般に以下の４つが挙げられます。

* 形態素解析
* 意味解析
* 構文解析
* 文脈解析

それぞれについて見ていきましょう。


## 形態素解析
前のチャプターで紹介した通り，janomeやMeCabなどといった形態素解析器を使用します。

理論についての詳しい解説は行いません。

```python
from janome.tokenizer import Tokenizer

t = Tokenizer()

for token in t.tokenize('対象テキスト'):
    # 表層形：token.surface
    # 品詞：token.part_of_speech
    # 活用型：token.infl_type
    # 活用形：token.infl_form
    # 基本形：token.base_form
    # 読み：token.reading
    # 発音：token.phonetic
```


## 意味解析


## 構文解析


## 文脈解析

