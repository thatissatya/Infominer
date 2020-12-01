import nltk


class owl:
    def __init__(self,n,f):
        self.oname = n
        self.header = '''<?xml version="1.0" encoding="UTF-8"?>\n <Ontology xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"    xsi:schemaLocation="http://www.w3.org/2002/07/owl# http://www.w3.org/2009/09/owl2-xml.xsd" xmlns="http://www.w3.org/2002/07/owl#" xml:base="http://example.com/'''+self.oname+'''" ontologyIRI="http://example.com/'''+self.oname+'''" > <Prefix name="CF" IRI="'''+self.oname+'''#"/> <Import>http://example.com/'''+self.oname+'''</Import>\n\n'''
        self.content = []
        self.footer = '\n</Ontology>'
        self.file = f

    def cont(self):
        t=''
        for i in self.content:
            t += i+'\n'
        return t

    def subclass(self, sub, sup):
        c='<SubClassOf><Class IRI="#'+sub+'"/> <Class IRI="#'+sup+'"/></SubClassOf>\n'
        self.content.append(c)

    def properti(self, sub, prop, sup):
        c='<SubClassOf>   <Class IRI="#'+sub+'"/> <ObjectAllValuesFrom>  <ObjectProperty IRI="#'+prop+'"/><Class IRI="#'+sup+'"/> </ObjectAllValuesFrom>    </SubClassOf>'
        self.content.append(c)

    def write(self):
        f=open(self.file,'w')
        f.write(self.header)
        f.write(self.cont())
        f.write(self.footer)
        f.close()


def generate_owl_file(bigram):
    lst = set()
    with open('wordlist.txt', 'r', encoding='utf-8') as file:
        wordlist = file.read()
    l = ['epidemiology', 'biological', 'epidemiological', 'disease', 'medical', 'transformation', 'instrument',
         'anthropology', 'cardiovascular', 'psychologically', 'odontology', 'electron', 'microscopy', 'bromide']
    for each in list(bigram):
        if each[0] == each[1]:
            continue
        else:
            if (each[0] in l or each[1] in l) and (each[0] not in wordlist.split() and each[1] not in wordlist.split()):
                trex = nltk.pos_tag(each)
                if trex[0][1].startswith('N') and trex[1][1].startswith('N'):
                    # or (trex[0][1]=='JJ' and trex[1][1]=='JJ') or ((trex[0][1].startswith('N') and trex[1][1]=='JJ')) or ((trex[0][1]=='JJ' and trex[1][1].startswith('N')))):
                    lst.add(each)
    lst = list(lst)
    o = owl('BioMedical', 'test.owl')
    for tup in lst:
        if tup[0] in l:
            o.subclass(tup[1], tup[0])
        else:
            o.subclass(tup[0], tup[1])
    o.write()



