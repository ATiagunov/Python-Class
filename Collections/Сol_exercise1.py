import collections as c
import csv

with open('stage3_test.csv') as csv_in:
    words = list()
    csv_reader = csv.DictReader(csv_in)
    for col in csv_reader:
        csv_words = col['Title'].split(" ") + col['Description'].split(" ")
        for i in csv_words:
            words.append(i)
    letter_cnt = c.Counter(words)
    print(f'Двадцать самых частых слов: {letter_cnt.most_common()[:20]}')
    print(f'Двадцать самых редких слов: {letter_cnt.most_common()[:-21:-1]}')
