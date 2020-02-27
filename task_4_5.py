x_1 = 0
x_2 = 1
n = 15


def fib(x1, x2, n):
    if n == 1:
        return x2
    else:
        x2 += x1
        x1 = x2 - x1
        print(f'{x1}')
        return fib(x1, x2, n-1)


print(fib(x_1, x_2, n))



