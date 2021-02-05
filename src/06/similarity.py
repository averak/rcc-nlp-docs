import glob
import tqdm
from janome.tokenizer import Tokenizer
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np


def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


tokenizer = Tokenizer()
vectorizer = CountVectorizer(binary=False)

# コピペチェック対象の局
TARGET = "soumu"  # kaikei / system / syogai / kensui / soumu
docs = []

print("形態素解析...")
files = glob.glob("text/%s/*.txt" % TARGET)
for file_name in tqdm.tqdm(files):
    with open(file_name, "r") as f:
        # 単語に分割
        docs.append("")
        for text in f.readlines():
            docs[-1] += " ".join(tokenizer.tokenize(text,
                                                    wakati=True)) + " "

# BoWを求める
bow = vectorizer.fit_transform(docs).toarray()
for i in range(len(bow)):
    for j in range(len(bow)):
        if i == j:
            continue

        if cos_sim(bow[i], bow[j]) > 0.8:
            print("---コピペが発覚---")
            print(docs[i].replace(" ", ""))
            print("------")
            print(docs[j].replace(" ", ""))
            print()
