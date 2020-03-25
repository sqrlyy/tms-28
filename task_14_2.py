import argparse
from datetime import datetime
from datetime import timedelta
from time import sleep


def timer(time_to_go):
    zero_time = timedelta(hours=0, minutes=0, seconds=0)
    one_second = timedelta(seconds=1)
    while time_to_go != zero_time:
        time_to_go = time_to_go - one_second
        sleep(0.999)
        yield time_to_go


def Pomodoro(focus_time, break_time, cycles):
    while cycles != 0:
        if cycles != args.cycles:
            print('New cycle is started.')
        cycles -= 1
        print('Focus!')
        for i in timer(timedelta(seconds=focus_time * 60)):
            print(i)
        print('Chill out...')
        for i in timer(timedelta(seconds=break_time * 60)):
            print(i)
        yield 'Cycle finished!'


parser = argparse.ArgumentParser('Pomodoro')
parser.add_argument('first_name', type=str)
parser.add_argument('last_name', type=str)
parser.add_argument('name', type=str)
parser.add_argument('-ft', '--focus-time', type=int, default=25)
parser.add_argument('-bt', '--break-time', type=int, default=5)
parser.add_argument('-cls', '--cycles', type=int, default=4)
args = parser.parse_args()

with open('task_14_2.txt', 'a') as file:
    file.writelines(f'Opener: {args.first_name} {args.last_name}, time: {datetime.now()} \n')

pomodoro_generator = Pomodoro(args.focus_time, args.break_time, args.cycles)

for i in pomodoro_generator:
    print(i)
