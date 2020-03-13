import csv
from datetime import datetime

start = datetime.now()

def find_min(list_of_dates):
    min_year = 2020
    min_month = 12
    min_day = 31
    for row in list_of_dates:
        if int(row[2]) < min_year:
            min_year = int(row[2])
    for row in list_of_dates:
        if int(row[2]) == min_year and int(row[1]) < min_month:
            min_month = int(row[1])
    for row in list_of_dates:
        if int(row[2]) == min_year and int(row[1]) == min_month and int(row[0]) < min_day:
            min_day = int(row[0])

    print(f'Earliest date: {min_day},{min_month},{min_year}')


filename = 'dates.csv'

dates = [
    {'day': 1, 'month': 1, 'year': 2020},
    {'day': 21, 'month': 7, 'year': 2019},
    {'day': 3, 'month': 9, 'year': 2018},
    {'day': 15, 'month': 2, 'year': 2020},
    {'day': 24, 'month': 6, 'year': 2016},
    {'day': 31, 'month': 12, 'year': 2016},
    {'day': 7, 'month': 6, 'year': 2016},
    {'day': 13, 'month': 6, 'year': 2016}
]

with open(filename, 'w', newline='') as csvfile:
    columns = ['day', 'month', 'year']
    writer = csv.DictWriter(csvfile, fieldnames=columns)
    writer.writeheader()
    writer.writerows(dates)

rows = []
with open(filename, 'r+', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        rows.append(row)

find_min(rows)
