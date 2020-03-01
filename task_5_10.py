from datetime import datetime
from datetime import timedelta

table = []

while True:
    print('What you want to do? 1)Add new train 2)Check table 3)Time in trip more 7:20 4)Exit')
    choice = int(input())
    if choice == 1:
        info = {'Number': input('Enter number: '), 'Arrival point': input('Arrival point: '),
                'Arrival time': datetime.strptime(input('Arrival time (m/d/y h:m): '), '%m/%d/%Y %H:%M'),
                'Destination': input('Destination: '),
                'Departure time': datetime.strptime(input('Departure time: (m/d/y h:m): '), '%m/%d/%Y %H:%M')}
        info.update({'Time in trip': info['Departure time'] - info['Arrival time']})
        table.append(info)
    elif choice == 2:
        for i in table:
            print(i)
    elif choice == 3:
        for train in table:
            if train['Time in trip'] >= timedelta(0, 26400):
                print(train)
    elif choice == 4:
        break
    print('\n')
