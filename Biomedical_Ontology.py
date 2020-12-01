
import PyPDF2, re, json, nltk
import numpy as np
from nltk.corpus import stopwords
from nltk.corpus import words
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from collections import Counter
# # Playing with Original Dictionary
# lst = list((words.words()))
# l = np.asarray(lst)
# st = set()
# for each in l:
#     st.add(each.lower())


# In[5]:


# Testing whether extracted word exist in real world dictionary or not
# def binary_search(word):
#     if word in st:
#         return True
#     return False


# In[7]:


# regex = re.compile('[^a-zA-Z]')
# file = open("book.pdf", 'rb')
# pdfFileReader = PyPDF2.PdfFileReader(file)
# totalpages = pdfFileReader.numPages
# currentpage = 0
# text = ''
# while (currentpage < totalpages ):
#     data = pdfFileReader.getPage(currentpage)
#     temptext=data.extractText()
#     text = text + " " + regex.sub(' ',temptext.lower())
#     currentpage += 1
# ans  = ""
# for word in text.split():
#     if binary_search(word):
#         ans = ans + ' ' + word
#
# with open("biodata.txt", "w", encoding="utf-8") as file:
#     file.write(ans)
#

# In[8]:


# Getting ride of stopwords
# with open("biodata.txt", "r", encoding="utf-8") as file:
#     data = file.read()
# text = ''
# for each in data.split():
#     if len(each) > 3 and each not in stopwords.words('English'):
#         text = text + ' ' + each


# In[9]:


# Unigram generation and counting their frequencies

# token = word_tokenize(text)
# wordcount  = {}
# for word in token:
#     if word not in wordcount.keys():
#         wordcount[word]=1
#     else :
#         wordcount[word]+=1
# with open('Unigram.txt','w',encoding='utf-8') as f:
#     f.write(json.dumps(wordcount))


# In[10]:


# Bigram generation and counting their frequenccies

# bigram =  list(ngrams(token,2))
# bgram = {}
# for each in bigram:
#     if each[0] == each[1]:
#         continue
#     word = each[0] + ' ' + each[1]
#     if word not in bgram.keys():
#         bgram[word] = 1
#     else :
#         bgram[word]+=1
# with open('Bigram.txt','w',encoding='utf-8') as file:
#     file.write(json.dumps(bgram))


# In[11]:


# class owl:
#     def __init__(self,n,f):
#         self.oname=n
#         self.header='''<?xml version="1.0" encoding="UTF-8"?>\n <Ontology xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"    xsi:schemaLocation="http://www.w3.org/2002/07/owl# http://www.w3.org/2009/09/owl2-xml.xsd" xmlns="http://www.w3.org/2002/07/owl#" xml:base="http://example.com/'''+self.oname+'''" ontologyIRI="http://example.com/'''+self.oname+'''" > <Prefix name="CF" IRI="'''+self.oname+'''#"/> <Import>http://example.com/'''+self.oname+'''</Import>\n\n'''
#         self.content=[]
#         self.footer='\n</Ontology>'
#         self.file=f
#
#     def cont(self):
#         t=''
#         for i in self.content:
#             t+=i+'\n'
#         return t
#     def subclass(self,sub,sup):
#         c='<SubClassOf><Class IRI="#'+sub+'"/> <Class IRI="#'+sup+'"/></SubClassOf>\n'
#         self.content.append(c)
#
#     def properti(self,sub,prop,sup):
#         c='<SubClassOf>   <Class IRI="#'+sub+'"/> <ObjectAllValuesFrom>  <ObjectProperty IRI="#'+prop+'"/><Class IRI="#'+sup+'"/> </ObjectAllValuesFrom>    </SubClassOf>'
#         self.content.append(c)
#
#     def write(self):
#         f=open(self.file,'w')
#         f.write(self.header)
#         f.write(self.cont())
#         f.write(self.footer)
#         f.close()
#

# In[12]:


# Generating Owl File
# lst = set()
# with open('wordlist.txt','r',encoding = 'utf-8') as file:
#     wordlist = file.read()
# l = ['epidemiology','biological','epidemiological','disease','medical','transformation','instrument','anthropology','cardiovascular','psychologically','odontology','electron','microscopy','bromide']
# for each in list(bigram):
#     if each[0] == each[1]:
#         continue
#     else:
#         if (each[0] in l or each[1] in l) and (each[0] not in wordlist.split() and each[1] not in wordlist.split()):
#             trex=nltk.pos_tag(each)
#             if trex[0][1].startswith('N') and trex[1][1].startswith('N'):
#                 # or (trex[0][1]=='JJ' and trex[1][1]=='JJ') or ((trex[0][1].startswith('N') and trex[1][1]=='JJ')) or ((trex[0][1]=='JJ' and trex[1][1].startswith('N')))):
#                 lst.add(each)
# lst = list(lst)
# o=owl('BioMedical','test.owl')
# for tup in lst:
#     if tup[0] in l:
#         o.subclass(tup[1],tup[0])
#     else:
#         o.subclass(tup[0],tup[1])
# o.write()
#


# In[13]:


#New Method

# fo = open("biodata.txt",encoding="utf-8")
# fo1 = fo.readlines()
# y=0
# mk=""
# for line in fo1:
#        bigm = list(nltk.bigrams(line.split()))
#        bigmC = Counter(bigm)
#        for key, value in sorted(bigmC.items(), key=lambda t:t[-1], reverse=True):
#            mk=mk+ str(key)+ ' ' + str(value) + '\n'
#
# mname="newbram.txt"
# with open(mname, "w+", encoding="utf-8") as f:
#     f.write(mk)
#
#
# # In[14]:
#
#
#
# d1 = re.findall(r"(\w+) in the", data)
# d2 = re.findall(r"in the (\w+)", data)
# d3 = re.findall(r"(\w+) is a", data)
# d4 = re.findall(r"is a (\w+)", data)
#
#
# # In[15]:
#
#
# print(len(d3),len(d4))
#
#
# # In[16]:
#
#
# e = 0
# newlst = set()
# while e < len(d1):
#     each = (d1[e],d2[e])
#     if d1[e] == d2[e]:
#         e  = e + 1
#         continue
#     else:
#         if len(each[0])>3  and len(each[1]):
#             trex=nltk.pos_tag(each)
#             if trex[0][1].startswith('N') and trex[1][1].startswith('N'):
#                 newlst.add(each)
#     e  = e + 1
# e = 0
# while e < len(d4):
#     each = (d3[e],d4[e])
#     if d3[e] == d4[e]:
#         e  = e + 1
#         continue
#     else:
#         if len(each[0])>3  and len(each[1]):
#             trex=nltk.pos_tag(each)
#             if trex[0][1].startswith('N') and trex[1][1].startswith('N'):
#                 newlst.add(each)
#     e  = e + 1
# lst = list(newlst)
# o=owl('BioMedical','trex.owl')
# for tup in lst:
#     if tup[0] in l:
#         o.subclass(tup[1],tup[0])
#     else:
#         o.subclass(tup[0],tup[1])
# o.write()
#
#

# In[ ]:




