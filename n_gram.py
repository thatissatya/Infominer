import json

from nltk import word_tokenize, ngrams


def uni_gram(raw_data):
    token = word_tokenize(raw_data)
    wordcount = {}
    for word in token:
        if word not in wordcount.keys():
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    with open('unigram.txt', 'w', encoding='utf-8') as f:
        f.write(json.dumps(wordcount))
        f.close()
    return wordcount


def bi_gram(raw_data):
    token = word_tokenize(raw_data)
    bigram = list(ngrams(token, 2))
    bgram = {}
    for each in bigram:
        if each[0] == each[1]:
            continue
        word = each[0] + ' ' + each[1]
        if word not in bgram.keys():
            bgram[word] = 1
        else:
            bgram[word] += 1
    with open('bigram.txt', 'w', encoding='utf-8') as file:
        file.write(json.dumps(bgram))
        file.close()
    return bgram
