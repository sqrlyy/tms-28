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
        yield time_to_go


parser = argparse.ArgumentParser('Timer')
parser.add_argument('-fn', '--first-name', required=True)
parser.add_argument('-ln', '--last-name', required=True)
parser.add_argument('-hs', '--hours', required=True)
parser.add_argument('-min', '--minutes', required=True)
parser.add_argument('sec', '--seconds', required=True)
args = parser.parse_args()

user_time = timedelta(hours=int(args.hours), minutes=int(args.minutes), seconds=int(args.seconds))

with open('log_14_1.txt', 'a') as file:
    file.writelines(f'Opener: {args.first_name} {args.last_name}, time: {datetime.now()} \n')

timer_generator = timer(user_time)

for i in timer_generator:
    print(i)

print('ALARM!')