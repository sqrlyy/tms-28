import argparse
from datetime import datetime
from datetime import timedelta
from time import sleep


def timer(time_to_go):
    zero_time = timedelta(hours=0, minutes=0, seconds=0)
    one_second = timedelta(seconds=1)
    while time_to_go != zero_time:
        print(time_to_go)
        time_to_go = time_to_go - one_second
        sleep(0.999)


def Pomodoro(focus_time, break_time, cycles, name):
    print(f'{name} is started.')
    while cycles != 0:
        if cycles != args.cycles:
            print('New cycle is started.')
        cycles -= 1
        print('Focus!')
        sleep(focus_time * 60 - 30)
        print('Focus ends in:')
        timer(timedelta(seconds=focus_time * 60 - 30))
        print('Chill out...')
        sleep(break_time * 60 - 30)
        print('Break ends in:')
        timer(timedelta(seconds=break_time * 60 - 30))
    return f'Process {name} is ends.'


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

print(Pomodoro(args.focus_time, args.break_time, args.cycles, args.name))
