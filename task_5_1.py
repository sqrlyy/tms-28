from decimal import Decimal
signs = ['+', '-', '/', '*', '0']
sign = ''
number_1 = Decimal(input('Please enter first number: '))
number_2 = Decimal(input('Please enter second number: '))
while True:
    sign = input('Enter sign: ')
    while sign not in signs:
        sign = input('Enter sign: ')
        print(sign)

    if sign == '+':
        print('Result:', (number_1 + number_2))
    elif sign == '-':
        print('Result:', (number_1-number_2))
    elif sign == '/':
        while number_2 == 0:
            number_2 = Decimal(input('Enter second number, not 0: '))
        print('Result:', (number_1/number_2))
    elif sign == '*':
        print('Result:', (number_1*number_2))
    else:
        break

print('End.')
