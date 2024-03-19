import csv

with open("python1.csv" , 'w') as f:
    pen = csv.writer(f)
    header = ['Name','Cell Phone', 'City']
    pen.writerow(header)
    entry1 = ['huguette','512 555 5555','austin']
    pen.writerow(entry1)
f.close

