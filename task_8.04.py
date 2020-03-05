from math import sqrt


def quadratic_equation(a, b, c):
    d = b**2 - 4 * a * c
    if d > 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        return f'x1 = {x1}, x2 = {x2}'
    else:
        return 'D < 0'


x = int(input('Enter x^2: '))
y = int(input('Enter x: '))
number = int(input('Enter other number: '))
print(quadratic_equation(x, y, number))
