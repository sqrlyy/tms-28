from random import randint
n = int(input('Size of matrix: '))
matrix = [[randint(1, 30) for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        if j < i:
            matrix[i][j] = 0

for i in matrix:
    print(i)