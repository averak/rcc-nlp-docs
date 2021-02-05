import os
import re
import glob
import tqdm


def cleaning(text):
    result = re.sub(r"\\[a-zA-Z*#]+", "", text)
    result = re.sub(r"\{.*\}", "", result)
    result = re.sub(r"\(.*\)", "", result)
    result = re.sub(r"（.*）", "", result)
    result = re.sub(r"[ 　]", "", result)
    result = re.sub(r"\n", "", result)

    return result


docs = {"kaikei": [], "system": [], "syogai": [], "kensui": [], "soumu": []}
files = glob.glob("data/*/src/*/*/*.tex")

# read
print("データ読み込み...")
for file_name in tqdm.tqdm(files):
    for kyoku in docs.keys():
        if kyoku not in file_name:
            continue

        with open(file_name, "r") as f:
            text = cleaning(f.read())
            docs[kyoku].append(text)

# dump
print("データ書き込み...")
os.system("rm -rf text")
for kyoku in tqdm.tqdm(docs.keys()):
    os.makedirs("text/%s" % kyoku, exist_ok=True)

    for text in docs[kyoku]:
        file_name = "text/%s/%s.txt" % (kyoku, id(text))

        with open(file_name, "w") as f:
            f.write(text)
