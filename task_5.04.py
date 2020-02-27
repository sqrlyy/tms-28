from random import randint
from decimal import Decimal
n = int(input('Write n:'))
m = int(input('Write m:'))
mx = []
summ = 0
result = 0
for i in range(n):
    mx.append([])
    for j in range(m):
        mx[i].append(randint(1, 20))
        summ += mx[i][j]
average = summ/(n*m)
for i in range(n):
    if i % 2 == 0:
        for j in range(0, m, 2):
            if mx[i][j] > average:
                result += mx[i][j]
    else:
        for j in range(1, m, 2):
            if mx[i][j] > average:
                result += mx[i][j]

print(mx)
print(f'Сумма = {summ}, сред.арифм. = {average}, результат = {result}')