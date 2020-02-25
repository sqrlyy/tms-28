from decimal import Decimal
import math

a = Decimal(input())
b = Decimal (input())

print(a)
hypotenuse = math.sqrt(a**2+b**2)

square = a*b/2

print('Гипотенуза:',hypotenuse)
print('Площадь:',square)