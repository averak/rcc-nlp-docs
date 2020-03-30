import re

def clean_hashtag(text):
    cleaned_text = re.sub(r'#[a-zA-Z]+', '', text)
    return cleaned_text

text = "Pythonでテキストをクリーニングする。 #Python"
print(clean_hashtag(text))
