import nltk

from Infominer.OWLWriter import owl


def manual(bigram):
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



