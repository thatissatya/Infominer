import preprocessing
import n_gram
import another_method
import OWLWriter


if __name__ == "__main__":
    wrdlst = preprocessing.get_wordlist()
    preprocessing.read_file(wrdlst)
    raw_data = preprocessing.removestopwords()
    unigram = n_gram.uni_gram(raw_data)
    bigram = n_gram.bi_gram(raw_data)
    OWLWriter.generate_owl_file(bigram)
    another_method.manual(bigram)

