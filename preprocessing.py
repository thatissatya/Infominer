import re
import PyPDF2
import numpy as np
from nltk.corpus import words, stopwords


def get_wordlist():
    lst = list((words.words()))
    lst = np.asarray(lst)
    wrdlst = set()
    for each in lst:
        wrdlst.add(each.lower())
    return wrdlst

def binary_search(word, wrdlst):
    if word in wrdlst:
        return True
    return False


def read_file(wrdlst):
    regex = re.compile('[^a-zA-Z]')
    file = open("book.pdf", 'rb')
    pdffilereader = PyPDF2.PdfFileReader(file)
    totalpages = pdffilereader.numPages
    currentframe = 0
    text = ''
    while currentframe < totalpages:
        data = pdffilereader.getPage(currentframe)
        temptext = data.extractText()
        text = text + " " + regex.sub(' ', temptext.lower())
        currentframe += 1
    ans = ""
    for word in text.split():
        if binary_search(word,wrdlst):
            ans = ans + ' ' + word

    with open("biodata.txt", "w", encoding="utf-8") as file:
        file.write(ans)
        file.close()

def removestopwords():
    with open("biodata.txt", "r", encoding="utf-8") as file:
        data = file.read()
        file.close()
    raw_data = ''
    for each in data.split():
        if len(each) > 3 and each not in stopwords.words('english'):
            raw_data = raw_data + ' ' + each
    return raw_data
