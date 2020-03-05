from random import randint
n = int(input('Enter n: '))
m = int(input('Enter m: '))
matrix_a = [[randint(0, 30) for j in range(m)] for i in range(n)]
matrix_b = [[randint(0, 30) for j in range(m)] for i in range(n)]

diff_matrix = []
sum_matrix = []
for i in range(n):
    diff_matrix.append([])
    sum_matrix.append([])
    for j in range(m):
        diff_matrix[i].append(matrix_a[i][j]-matrix_b[i][j])
        sum_matrix[i].append(matrix_a[i][j]+matrix_b[i][j])


print('Matrix a: ')
for i in matrix_a:
    print(i)
print('Matrix b: ')
for i in matrix_b:
    print(i)
print('Difference: ')
for i in diff_matrix:
    print(i)
print('Sum matrix: ')
for i in sum_matrix:
    print(i)
