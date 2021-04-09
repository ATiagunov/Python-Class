import csv

with open('stage3_test.csv', newline='') as csv_in, open("10000<price<=50000.csv", 'w', newline='') as out_csv:
    spamreader = csv.reader(csv_in, delimiter=',', quotechar='"')
    writer = csv.writer(out_csv, delimiter=',')
    count = 0
    for row in spamreader:
        if count == 0:
            writer.writerow(row)
            count += 1
        elif 10000 < float((row[4])) <= 50000:
            writer.writerow(row)
