from random import randint
n = int(input('Enter size of matrix: '))
matrix = []
for i in range(n):
    matrix.append([])
    for j in range(n):
        matrix[i].append(randint(1, 30))
print(matrix)
for i in range(n):
    max_number = matrix[i][0]
    temp_j = 0
    for j in range(n):
        if max_number < int(matrix[i][j]):
            max_number = int(matrix[i][j])
            temp_j = j
    matrix[i][i], matrix[i][temp_j] = matrix[i][temp_j], matrix[i][i]
    print(max_number)
print(matrix)
