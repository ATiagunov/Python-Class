import collections as c
import csv

with open('/home/alexander/PycharmProjects/python_practice/CSV/stage3_test.csv') as csv_in:
    word_cnt = c.Counter()
    csv_reader = csv.DictReader(csv_in)
    for col in csv_reader:
        csv_words = col['Title'].split(" ") + col['Description'].split(" ")
        for i in csv_words:
            word_cnt[i] += 1

    print(f'Двадцать самых частотных слов: {word_cnt.most_common()[:20]}')
    print(f'Двадцать самых редких слов: {word_cnt.most_common()[:-21:-1]}')
