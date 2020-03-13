import csv


def append_line(filename, new_values=list):
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        value = [f'\n'] + new_values
        writer.writerow(new_values)


with open('people.csv', 'r+', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Last name', 'Age'])

number = int(input('Enter count of people: '))
for i in range(number):
    append_line('people.csv', [input('Name: '), input('Last name: '), input('Age: ')])

with open('report.csv', 'r+') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['1-12', '13-18', '19-25', '26-40', '40+'])

with open('people.csv', 'r') as csv_people:
    reader = csv.reader(csv_people)
    report_list = [0, 0, 0, 0, 0]
    next(reader)
    for row in reader:
        if int(row[2]) < 13:
            report_list[0] += 1
        elif int(row[2]) < 19:
            report_list[1] += 1
        elif int(row[2]) < 26:
            report_list[2] += 1
        elif int(row[2]) < 40:
            report_list[3] += 1
        else:
            report_list[4] += 1
    print(report_list)

append_line('report.csv', report_list)
