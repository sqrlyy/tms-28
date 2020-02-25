first_str = input('Enter str.\n')
average = int(len(first_str)/2)
print(first_str[average])
if first_str[average] == first_str[0]:
    print(first_str[1:average])
