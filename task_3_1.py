from decimal import Decimal
number = Decimal(input('Enter number.\n'))
if number % 1000 == 0:
    print('Millenium.')