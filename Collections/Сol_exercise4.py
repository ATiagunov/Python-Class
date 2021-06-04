import collections as c
import csv
from functools import cmp_to_key
from contextlib import redirect_stdout


def compare_adverts(a, b):
    return float(a[len(a) - 1]) - float(b[len(b) - 1])

with open('/home/alexander/PycharmProjects/python_practice/CSV/stage3_test.csv') as csv_in, open("result.txt", 'w', newline='') as f:
    csv_reader = csv.reader(csv_in)
    next(csv_reader)
    list = []
    for row in csv_reader:
        k, v = row[2], row[len(row) - 1]
        list.append([k, v])

    min_max = sorted(list, key=cmp_to_key(compare_adverts))
    max_min = sorted(list, key=cmp_to_key(compare_adverts), reverse=True)
    min_max_dict = c.OrderedDict({})
    max_min_dict = c.OrderedDict({})
    for row in min_max:
        min_max_dict[row[0]] = row[len(row) - 1]

    for row in max_min:
        max_min_dict[row[0]] = row[len(row) - 1]

    with redirect_stdout(f):

        print("Цены по возрастанию")
        for row in min_max_dict.items():
            print("Заголовок: ", row[0], "Стоимость: ",  row[1])


        print("Цены по убыванию")
        for row in max_min_dict.items():
            print("Заголовок: ", row[0], "Стоимость: ", row[1])














