### This program reads from a CSV file ###


import csv
with open("novels.csv") as f:
    read_data = csv.reader(f)

    for row in read_data:
        print(row)
        
