from random import randint
print('Choose range.\n')
x = int(input())
y = int(input())
print('Okay, now number of attempts\n')
amount_of_attempts = int(input())
winner_number = randint(x, y)

for i in range(amount_of_attempts):
    print('Write a number: ')
    choice_number = int(input())
    if choice_number == winner_number:
        print('You are the winner! \n')
        break
    elif amount_of_attempts - i == 1:
        print('Your are the loser!')
        break
    elif winner_number > choice_number:
        print('Take more.\n')
    elif winner_number < choice_number:
        print('Take less.\n')

