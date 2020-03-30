# -*- coding: utf-8 -*-
from janome.tokenizer import Tokenizer

t = Tokenizer()

text = input('input text : ')

for token in t.tokenize(text):
    print(token)

    '''
    表層形：token.surface
    品詞：token.part_of_speech
    活用型：token.infl_type
    活用形：token.infl_form
    基本形：token.base_form
    読み：token.reading
    発音：token.phonetic
    '''

# 分かち書きのみ
t = Tokenizer(wakati=True)
print(t.tokenize(text))

