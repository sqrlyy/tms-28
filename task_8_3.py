from math import fabs
from math import pow
from datetime import datetime


def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def sin1(x, e):
    result = 0
    term = x
    n = 1
    while fabs(term) > e:
        result += term
        term = pow(-1, n) * pow(x, 2 * n + 1) / fact(2 * n + 1)
        n += 1
    return result


number = float(input('Enter x: '))
exp = float(input('Enter e: '))

print(sin1(number, exp))
