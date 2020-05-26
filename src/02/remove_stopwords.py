def remove_stopwords(text, stopwords):
    for sw in stopwords:
        text = text.replace(sw, '')
    return text

stopwords = open('stopwords.txt', 'r').read().split('\n')
text = '結局あそこのラーメンが一番美味しい。'
print(remove_stopwords(text, stopwords))
