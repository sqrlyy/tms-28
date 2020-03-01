print('Enter a range: ')
m = int(input())
n = int(input())


for number in range(m, n+1):
    result = []
    i = 2
    divider = 0
    while i < number:
        if number % i == 0:
            divider = number / i
            result.append(divider)
            i += 1
        else:
            i += 1
    print(result)
