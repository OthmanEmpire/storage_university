###



import csv

montypython = [
['Title', 'Release Date'],
['And Now For Something Completely Different', '1971'],
['Monty Python And The Holy Grail', '1975'],
["Monty Python's Life of Brian", '1979'],
['Monty Python Live At The Hollywood Bowl', '1982'],
["Monty Python's The Meaning of Life", '1983']
]

with open('test.csv', 'w') as file:
    writer = csv.writer(file)
    for film in montypython:
        writer.writerow(film)
