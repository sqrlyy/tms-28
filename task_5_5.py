from random import randint

main_list = []
for i in range(19):
    main_list.append(randint(1, 50))
print(main_list)
max_number = main_list[0]
for number in main_list:
    if max_number < number:
        max_number = number

print(f'Result: {max_number}')