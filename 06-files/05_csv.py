import csv

# with open("sample.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Character Limit", "Kate Conger and Ryan Mac"])
#     writer.writerow(["Lord of Emperors", "Guy Gavriel Kay"])
#     writer.writerow(["Before They Were Hanged", "Joe Abercrombie"])
with open("sample.csv") as file:
    reader = csv.DictReader(file)
    # next(reader) - use with default reader to skip the header row
    for row in reader:
        print(row)
