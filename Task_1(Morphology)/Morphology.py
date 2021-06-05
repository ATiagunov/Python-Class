import xml.etree.ElementTree as etree
import re


class Corpus:

    def __init__(self):
        self.sentences = []

    def load(self, path_to_corpus):
        tree = etree.parse(path_to_corpus)
        root = tree.getroot()
        for text in root.iter('source'):
            self.sentences.append(text.text + "\n")

    def print_i_sentence(self, i):
        print(self.sentences[i])


class Sentence:
    def __init__(self):
        self._wordforms = []
        self._sentences = []
        self.bag_of_words = []

    def iterate_corpus(self, corpus):
        for sentence in corpus.sentences:
            self._sentences.append(sentence)
            words = []
            res = re.findall(r'\w+', sentence)
            for word in res:
                self.bag_of_words.append(word)
                words.append(word)
            self._wordforms.append(words)

    def retrieve_words_of_i_sentence(self, i):
        print(self._sentences[i])
        print(self._wordforms[i])

    def retrieve_j_word_of_i_sentence(self, i, j):
        print('\n' + self._wordforms[i][j])

    def retrieve_i_word_from_all(self, i):
        print('\n' + self.bag_of_words[i])


class Wordform:

    def __init__(self, obj, i):
        self._grammems = []
        self._wordform = obj.bag_of_words[i]

    def iterate_grammems(self):
        tree = etree.parse('/home/alexander/PycharmProjects/python_practice/XML/annot.opcorpora.no_ambig.xml')
        root = tree.getroot()
        for token in root.iter('token'):
            text = token.get('text')
            if self._wordform == text:
                vs = token.findall('tfr')
                for v in vs:
                    ls = v.find('v')
                    for l in ls:
                        gs = l.findall('g')
                        for g in gs:
                            self._grammems.append(g.attrib['v'])
                    return

    def retrieve_grammems_of_the_word(self):
        print(f'\n {self._wordform}: {self._grammems}')

    def retrieve_i_grammem(self, i):
        print('\n' + self._grammems[i])



c = Corpus()
c.load('/home/alexander/PycharmProjects/python_practice/XML/annot.opcorpora.no_ambig.xml')
c.print_i_sentence(3)

s3 = Sentence()
s3.iterate_corpus(c)
s3.retrieve_words_of_i_sentence(3)
s3.retrieve_j_word_of_i_sentence(3, 2)
s3.retrieve_i_word_from_all(0)

w3 = Wordform(s3, 3)
w3.iterate_grammems()
w3.retrieve_grammems_of_the_word()
w3.retrieve_i_grammem(0)

#Исправил, исключил из списка слов пунктуацию. Только не совсем понимаю, что писать в тестах.
#Например, для нахождения граммем i-го слова у меня получится тот же самый код, что и в классе.