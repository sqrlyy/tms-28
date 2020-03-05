from random import randint
from decimal import Decimal
n = int(input('Enter n: '))
m = int(input('Enter m: '))
matrix = [[randint(0, 30) for j in range(m)] for i in range(n)]
g = Decimal(input('Enter g: '))
for i in matrix:
    print(i)
matrix_g = []
for i in range(n):
    matrix_g.append([])
    for j in range(m):
        matrix_g[i].append(matrix[i][j] * g)
print('Matrix * g: ')
for i in matrix_g:
    print(i)
