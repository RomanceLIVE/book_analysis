# Jupyter-lab code


# Loading the book

try_encodings = ['utf-8', 'latin-1', 'cp1252']

for encoding in try_encodings:
    try:
        with open("miracle_in_the_andes.txt", "r", encoding=encoding) as file:
            book = file.read()
        break  # Stop if successful
    except UnicodeDecodeError:
        continue  # Try the next encoding if this one fails


# The most used words (non-articles)

import re
pattern = re.compile("[a-zA-Z]+")
findings = re.findall(pattern, book.lower())
findings[:5]


d = {}
for word in findings:
    if word in d.keys():
        d[word] = d[word] + 1
    else:
        d[word] = 1


d_list = [(value, key) for (key, value) in d.items()]
d_list = sorted(d_list, reverse=True)
d_list[:5]


import nltk

nltk.download('stopwords')


import nltk

from nltk.corpus import stopwords
english_stopwords = stopwords.words("english")


filtered_words = []
for count, word in d_list:
    if word not in english_stopwords:
        filtered_words.append((word, count))


filtered_words[:10]


# Sentiment Analysis: What is the most positive and most negative chapter ?


from nltk.sentiment import SentimentIntensityAnalyzer

import nltk

nltk.download('vader_lexicon')

analyzer = SentimentIntensityAnalyzer()

scores = analyzer.polarity_scores("I hate you and myself!")

if scores["pos"] > scores["neg"]:
    print("Text is positive!")
else:
    print("Text is negative!")

analyzer.polarity_scores(book)

### Chapter sentiment analysis

import re

pattern = re.compile("Chapter [0-9]+")
chapters = re.split(pattern, book)


chapters[1:]


for chapter in chapters:
    scores = analyzer.polarity_scores(chapter)
    print(scores)


