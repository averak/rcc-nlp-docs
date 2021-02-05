import re


def cleaning(text):
    result = text[15:]
    result = result[:-2]
    result = re.sub(r"http.+", "", result)
    result = re.sub(r"@[a-zA-Z0-9_]+", "", result)
    result = re.sub(r"#.+", "", result)
    result = re.sub(r"[\n\t\r]", "", result)
    result = re.sub(r"\\n", "", result)
    result = re.sub(r"[.．]", "。", result)
    result = re.sub(r"[,，]", "、", result)
    result = re.sub(r"[!！]", "。", result)
    result = re.sub(r"[ 　]", "\n", result)

    return result


tweets = []

# 全ツイートを読み込む
with open("tweet.js", "r") as f:
    file_text = f.read()

    for noisy_text in re.findall(r"\"full_text\".+", file_text):
        tweets.append(cleaning(noisy_text))

with open("dump.txt", "w") as f:
    text = re.sub("\n{2,}", "", "\n".join(tweets))
    f.write(text)
