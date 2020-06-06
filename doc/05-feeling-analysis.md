# 感情分析

このチャプターでは，日本語の感情分析について解説します。

分析対象テキストのポジティブ・ネガティブレベルをスコア化することが目的です。


## 極性辞書
感情極性辞書とは，
[単語感情極性対応表](http://www.lr.pi.titech.ac.jp/~takamura/pndic_ja.html)より，日本語の極性辞書をコピーしてください。

ファイル名を`polarity.txt`として保存します。

このままでは極性辞書として読み込めないためパースしてあげましょう。

```python
>>> from janome.tokenizer import Tokenizer
>>> t = Tokenizer()
>>>
>>> # 極性辞書をパース
>>> polarity_text = open('polarity.txt', 'r').read()
>>> rows = polarity_text.split('\n')
>>>
>>> dic = []
>>> for row in rows:
...     word = row.split(':')
...     word[3] = float(word[3])
...     dic.append(word)
...
>>>
>>> def calc_feeling_analysis(text):
... score = 0.0
...     for token in t.tokenize(text):
...         match_word = [w for w in dic if w[0] == token.base_form]
...         if match_word == []:
...             continue
...         score += match_word[0][3]
...
...   return score
...
>>> calc_feeling_analysis('人生に疲れた。死にたいです。')
-2.136564
```

この辞書では，各単語にWordNetを用いて自動生成された離散的なスコアをそのまま使用しているので，精度は低めですが，軽い開発程度であれば十分でしょう。

他にも[oseti](https://github.com/ikegami-yukino/oseti/)といった日本語のネガポジ分析器などもあります。
ただしosetiの利用にはMeCabがインストールされていることが前提ですので，注意が必要です。

