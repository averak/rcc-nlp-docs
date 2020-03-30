# -*- coding: utf-8 -*-
from janome.tokenizer import Tokenizer

t = Tokenizer()

text = input('input text : ')

for token in t.tokenize(text):
    print(token)
