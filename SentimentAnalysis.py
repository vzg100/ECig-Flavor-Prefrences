from pathlib import Path
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import glob
import csv
import string
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import nltk
from nltk.corpus import movie_reviews
from nltk.stem import WordNetLemmatizer
sentences = []
sw = stopwords.words("english")
#Please excuse this cluster fuck of code 
def clean_text(t):
    # This text remoes 
    t= nltk.word_tokenize(t, language='english')
    c_t = []
    # Clears text of any special characters, right now this work is based on english speakers
    for i in t:
        if i in "qwertyuiopasdfghjklzxcvbnm ":
            c_t.append(i)
    t = []
    # Lemmatizer is used to try and bring different usages and possibly spellings of flavors to a single 
    lemmatizer = WordNetLemmatizer()
    for i in c_t:
        # TODO: add stop word filtering
        t.append(lemmatizer.lemmatize(i))
    c_t = " ".join(t) 
    return c_t

# Pulled from sentdex tutorial to save some lines code 
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

print("loaded training documents")
#shuffles data before it is translated
random.shuffle(documents)
x_train = []
y_train = []
# Translated training data labels to 1 and 0
for i in range(len(documents)):
    if documents[i][1] == "neg":
        y_train.append(0)
        text = " ".join(documents[i][0])
        text = nltk.word_tokenize(text, language='english')
        x_train.append(clean_text(" ".join(documents[i][0])))
    else:
        y_train.append(1)
        x_train.append(clean_text(" ".join(documents[i][0])))
        
print("prepped docs")

#vectorizes training data and trains the classifier
vectorizer = CountVectorizer(analyzer = "word", max_features = 5000, tokenizer = None, stop_words = None, preprocessor = None) 
x_train = vectorizer.fit_transform(x_train)
x_train = x_train.toarray()
classy = MultinomialNB()
classy.fit(x_train, y_train)

print("trained")
reddit = []
# clean2.txt has a portion of the total scraped reddit comments, cleans them again as a precaution 
f = open("clean2.txt")
for line in f:
    line = line.lower()
    line = clean_text(line)
    reddit.append(line)
print("loaded reddit docs")
# t_reddit is just a copy of the reddit text used to analyze flavor later
t_reddit = reddit
reddit = vectorizer.fit_transform(reddit)
reddit = reddit.toarray()
result = classy.predict(reddit)
print("Predicted reddit docs")

flavors = open("")
#keeps count of results
flavor_list = []
for i in flavors:
    i = clean_text(i)
    flavor_list.append(i)
flavor_results = {}
# Compares scraped flavors to reddit text
for i in range(len(t_reddit)):
    for j in flavor_list:
        if j in t_reddit[i]:
            if j in flavor_results.keys():
                if result[i] == 0:
                    flavor_results[j] = [flavor_results[j][0], flavor_results[j][1]+1]
                else:
                    flavor_results[j] = [flavor_results[j][0]+1, flavor_results[j][1]]
            else:
                if result[i] == 0:
                    flavor_results[j] = [0, 1]
                else:
                    flavor_results[j] = [1, 0]
print(flavor_results)

