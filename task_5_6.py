from random import randint
n = int(input('Enter length of list: '))
main_list = []
for i in range(n):
    main_list.append(randint(1, 50))
print(main_list)
counter = 0
number = main_list[0]
for i, mx_number in enumerate(main_list):
    if number < mx_number:
        number = mx_number
    else:
        number = mx_number
        if number < main_list[i+1] and (i + 1) < n:
            counter += 1
print(counter)
