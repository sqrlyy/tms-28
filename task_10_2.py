import csv

filename = 'weather.csv'
weather = [
    {'Date': '06.03', 'City': 'Minsk', 'Degrees': 5, 'Wind': 3},
    {'Date': '07.03', 'City': 'Minsk', 'Degrees': 6, 'Wind': 3},
    {'Date': '08.03', 'City': 'Minsk', 'Degrees': 8, 'Wind': 4},
    {'Date': '09.03', 'City': 'Minsk', 'Degrees': 7, 'Wind': 4},
    {'Date': '10.03', 'City': 'Minsk', 'Degrees': 6, 'Wind': 4},
    {'Date': '11.03', 'City': 'Minsk', 'Degrees': 6, 'Wind': 7},
    {'Date': '12.03', 'City': 'Minsk', 'Degrees': 6, 'Wind': 11}
]
with open(filename, 'w', newline='') as csvfile:
    columns = ['Date', 'City', 'Degrees', 'Wind']
    writer = csv.DictWriter(csvfile, fieldnames=columns)
    writer.writeheader()
    writer.writerows(weather)

with open(filename, 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    average_degree = 0
    average_wind = 0
    for row in reader:
        average_degree += int(row['Degrees'])
        average_wind += int(row['Wind'])

print(f'Average degree: {(average_degree/7)}, average wind: {average_wind/7}')
