import collections as c
import csv

with open('/home/alexander/PycharmProjects/python_practice/CSV/stage3_test.csv') as csv_in, open("result.csv", 'w', newline='') as out_csv:
    csv_reader = csv.DictReader(csv_in)
    d = {}
    for row in csv_reader:
       k, v = row['Title'], row['Price']
       d[k] = v


    min_to_max = c.OrderedDict(sorted(d.items(), key=lambda t: t[1]))
    max_to_min = c.OrderedDict(sorted(d.items(), key=lambda t: t[1], reverse=True))

    writer = csv.writer(out_csv)
    for key, value in max_to_min.items():
        writer.writerow([key, value])








