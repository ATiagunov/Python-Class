import csv

with open('stage3_test.csv') as csv_in, open("no_images&descriptions.csv", 'w', newline='') as out_csv:
    csv_reader = csv.DictReader(csv_in)
    csv_writer = csv.DictWriter(out_csv, fieldnames=['Id', 'Title', 'Price'])
    csv_writer.writeheader()
    for row in csv_reader:
        del row['Images'], row['Description']
        csv_writer.writerow(row)
