def fact2(n):
    result = 1
    if n % 2 == 0:
        for i in range(2, n+1, 2):
            result *= i
    else:
        for i in range(1, n+1, 2):
            result *= i
    return result


number = int(input('Please enter number > 0: '))
while number < 0:
    number = int(input())

print(fact2(number))
