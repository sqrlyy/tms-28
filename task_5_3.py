sum_result = []
for number in range(200, 301):
    result = []
    divider = 0
    i = 2
    while i <= number:
        if number % i == 0:
            divider = number / i
            result.append(int(divider))
            i += 1
        else:
            i += 1
    print(result)
    if result:
        sum_result.append(int(sum(result)))
    else:
        sum_result.append(0)
print('\n')
print(sum_result)
print('\n')
for i in range(0, 101):
    for j in range(0, 101):
        if sum_result[i] == 200 + j and sum_result[j] == 200 + i:
            print(200 + i, 200 + j)
