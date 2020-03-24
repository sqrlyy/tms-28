import ui_func
import exceptions
choice = [1, 2, 3, 4, 5, 6]
while True:
    print('1) Enter numbers. 2)Sum. 3)Subtraction. 4)Multiply. 5)Division. 6)Exit.')
    user_choice = None
    while user_choice not in choice:
        user_choice = input('Enter your choice: ')
        if not user_choice.isdigit():
            raise exceptions.ChoiceException('enter only 1-6')
        else:
            user_choice = int(user_choice)
    if user_choice == 1:
        numbers = ui_func.enter_numbers()
    elif user_choice == 2:
        try:
            ui_func.sum_numbers(numbers)
        except NameError:
            print('Enter numbers!')
    elif user_choice == 3:
        try:
            ui_func.sub_numbers(numbers)
        except NameError:
            print('Enter numbers!')
    elif user_choice == 4:
        try:
            ui_func.mul_numbers(numbers)
        except NameError:
            print('Enter numbers!')
    elif user_choice == 5:
        try:
            ui_func.div_numbers(numbers)
        except NameError:
            print('Enter numbers!')
            # raise exceptions.MyException('as')
        except ZeroDivisionError:
            print('Division by zero!')
    else:
        print('Goodbye!')
        break
    print('\n')
