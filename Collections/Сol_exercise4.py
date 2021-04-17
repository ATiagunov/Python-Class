import collections as c
import csv

with open('stage3_test.csv') as csv_in, open("result.csv", 'w', newline='') as out_csv:
    csv_reader = csv.DictReader(csv_in)
    csv_writer = csv.DictWriter(out_csv, fieldnames=csv_reader.fieldnames)
    csv_writer.writeheader()
    d = c.defaultdict(list)
    for row in csv_reader:
        for k, v in row.items():
            d[k].append(v)
    for row in d:
        od = c.OrderedDict(d.items())
    od = c.OrderedDict(sorted(list(od.items()), key=lambda t: t[4][1]))
    print(list(od))
    #В некоторых примерах OrderedDict принимает на вход csv.reader,
    #я собираю все в один через default, из которого получаю ordered.
    #Значения price определенно лежат в [4][1], но почему не работает sorted не понимаю.








