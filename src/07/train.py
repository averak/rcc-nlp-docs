import re
from janome.tokenizer import Tokenizer
import markovify


def split_for_markovify(text):
    """split text to sentences by newline, and split sentence to words by space.
    """
    # separate words using janome
    tagger = Tokenizer()
    splitted_text = ""

    # these chars might break markovify
    # https://github.com/jsvine/markovify/issues/84
    breaking_chars = [
        "(",
        ")",
        "[",
        "]",
        """,
        """,
    ]

    # split whole text to sentences by newline, and split sentence to words by space.
    for line in text.split():
        for token in tagger.tokenize(line):
            try:
                if token.surface not in breaking_chars:
                    splitted_text += token.surface    # skip if node is markovify breaking char
                if token.surface != "。" and token.surface != "、":
                    splitted_text += " "    # split words by space
                if token.surface == "。":
                    splitted_text += "\n"    # reresent sentence by newline
            except UnicodeDecodeError as e:
                # sometimes error occurs
                print(line)

    return splitted_text


def main():
    # load text
    with open("dump.txt", "r") as f:
        text = f.read()

    # split text to learnable form
    splitted_text = split_for_markovify(text)

    # learn model from text.
    text_model = markovify.NewlineText(splitted_text, state_size=3)

    # ... and generate from model.
    sentence = text_model.make_sentence()
    # need to concatenate space-splitted text
    print("".join(sentence.split()))

    # save learned data
    with open("model.json", "w") as f:
        f.write(text_model.to_json())


if __name__ == "__main__":
    main()
