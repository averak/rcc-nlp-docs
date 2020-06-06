# -*- coding: utf-8 -*-
from janome.tokenizer import Tokenizer

t = Tokenizer()

# 極性辞書をパース
polarity_text = open('polarity.txt', 'r').read()
rows = polarity_text.split('\n')

dic = []
for row in rows:
    word = row.split(':')
    word[3] = float(word[3])
    dic.append(word)


def calc_feeling_analysis(text):
    score = 0.0
    for token in t.tokenize(text):
        match_word = [w for w in dic if w[0] == token.base_form]
        if match_word == []:
            continue
        score += match_word[0][3]

    return score


score = calc_feeling_analysis('人生に疲れた。死にたいです。')
print(score)
