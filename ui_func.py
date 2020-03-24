import classes


def enter_numbers():
    print('Enter numbers.')
    while True:
        wrong_1 = 0
        wrong_2 = 0
        first_number = input('First number: ')
        second_number = input('Second number: ')
        for char in first_number:
            if char.isdigit() or char == '.':
                continue
            else:
                wrong_1 += 1
        for char in second_number:
            if char.isdigit() or char == '.':
                continue
            else:
                wrong_2 += 1

        if wrong_1 < 1 and wrong_2 < 1:
            break
        else:
            continue
    math = classes.Math(float(first_number), float(second_number))
    print(math)
    return math


def sum_numbers(math):
    print(f'Sum: {math.first_number} + {math.second_number} = {math.sum()}')


def sub_numbers(math):
    print(f'Subtraction: {math.first_number} - {math.second_number} = {math.sub()}')


def mul_numbers(math):
    print(f'Subtraction: {math.first_number} * {math.second_number} = {math.mul()}')


def div_numbers(math):
    print(f'Subtraction: {math.first_number} / {math.second_number} = {math.div()}')
