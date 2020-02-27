list_1 = []
length = int(input('Write length of list: '))
print('Fill list: ')
k = 0
for i in range(length):
    list_1.append(input())
    if int(list_1[i]) % 2 == 0:
        k += 1

print(k)
