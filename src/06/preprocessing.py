import os
import re
import glob


def cleaning(text):
    result = re.sub(r"\\[a-zA-Z*#]+", '', text)
    result = re.sub(r"\{.*\}", '', result)
    result = re.sub(r"\(.*\)", '', result)
    result = re.sub(r"（.*）", '', result)
    result = re.sub(r"[ 　]", '', result)
    result = re.sub(r"\n", '', result)

    return result


docs = {"kaikei": [], "system": [], "syogai": [], "kensui": [], "soumu": []}
files = glob.glob(r"data/*/src/*/*/*.tex")

# read
for file_name in files:
    for kyoku in docs.keys():
        if kyoku not in file_name:
            continue

        with open(file_name, 'r') as f:
            text = cleaning(f.read())
            docs[kyoku].append(text)

# dump
os.system("rm -rf text")
for kyoku in docs.keys():
    os.makedirs('text/%s' % kyoku, exist_ok=True)

    for text in docs[kyoku]:
        file_name = 'text/%s/%s.txt' % (kyoku, id(text))

        with open(file_name, 'w') as f:
            f.write(text)
