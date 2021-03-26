import csv

with open('stage3_test.csv') as csv_in, open("morethan3.csv", 'w', newline='') as out_csv:
    csv_reader = csv.DictReader(csv_in)
    csv_writer = csv.DictWriter(out_csv, fieldnames=['Id', 'Images', 'Title', 'Description', 'Price'])
    csv_writer.writeheader()
    for row in csv_reader:
        if (row['Images'].count(',')) > 2:
            csv_writer.writerow(row)
