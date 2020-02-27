list_1 = []
length = int(input('Write length of list: '))
print('Fill list: ')
for i in range(length):
    list_1.append(input())

list_2 = []
for i in range(length):
    list_2.append(int(list_1[i]) * -2)
print(list_2)