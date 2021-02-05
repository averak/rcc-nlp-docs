import markovify
from janome.tokenizer import Tokenizer

tokenizer = Tokenizer()
model = markovify.Text.from_json(open("model.json").read())

while True:
    word = input("単語を入力：")

    try:
        print(model.make_sentence_with_start(beginning=word).replace(" ", ""))
    except:
        print("\"%s\"から始まるテキストはありませんでした" % word)

    print()
