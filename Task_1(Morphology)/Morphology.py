import xml.etree.ElementTree as etree


class Corpus:

    def __init__(self):
        self._sentences = []

    def load(self, path_to_corpus):
        global root
        tree = etree.parse(path_to_corpus)
        root = tree.getroot()
        for text in root.iter('source'):
            self._sentences.append(text.text + "\n")

    def print_i_sentence(self, i):
        print(self._sentences[i])


class Sentence:

    def __init__(self):
        self._strings = []
        self._words = []

    def pick_sentence(self, num):
        for sentence in root.iter('sentence'):
            if int(sentence.attrib['id']) == num:
                text = sentence.find('source')
                self._strings.append(text.text)
                tokens = sentence.find('tokens')
                for token in tokens:
                    word = token.attrib['text']
                    self._words.append(word)

    def retrieve_sentence(self):
        if not self._strings or not self._words:
            print("Предложение под этим номером не существует")
        else:
            print(self._strings)
            print(self._words)

    def print_i_word(self, i):
        if not self._words:
            print("Предложение под этим номером не существует")
        else:
            print(self._words[i])


class Wordform:

    def __init__(self):
        self._grammems = []
        self._word_strings = []

    def pick_word(self, num):
        for token in root.iter('token'):
            if int(token.attrib['id']) == num:
                text = token.attrib['text']
                self._word_strings.append(text)
                vs = token.findall('tfr')
                for v in vs:
                    ls = v.find('v')
                    for l in ls:
                        gs = l.findall('g')
                        for g in gs:
                            self._grammems.append(g.attrib['v'])

    def retrieve_word(self):
        if not self._grammems or not self._word_strings:
            print("Слово под этим номером не существует")
        else:
            print(self._word_strings)
            print(self._grammems)

    def print_i_grammem(self, i):
        if not self._grammems:
            print("Граммем для этого слова не существует")
        else:
            print(self._grammems[i])


c = Corpus()
c.load('/home/alexander/PycharmProjects/python_practice/XML/annot.opcorpora.no_ambig.xml')
c.print_i_sentence(2)

s3 = Sentence()
s3.pick_sentence(3)
s3.retrieve_sentence()

s5 = Sentence()
s5.pick_sentence(5)
s5.retrieve_sentence()

w3 = Wordform()
w3.pick_word(3)
w3.retrieve_word()

w2 = Wordform()
w2.pick_word(2)
w2.retrieve_word()
w2.print_i_grammem(0)

