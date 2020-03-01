number = ''
while not number.isdigit():
    number = input('Enter a number: ')
summ = 0
multiply = 1
for i in range(len(number)):
    summ += int(number[i])
    multiply *= int(number[i])
print(f'Sum = {summ}, multiply = {multiply}')