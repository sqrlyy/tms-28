from decimal import Decimal
import math

a = Decimal(input())
b = Decimal(input())

average_arifm = (a+b)/2
average_geom = math.sqrt(a*b)

print('Среднее арифметическое:',average_arifm)
print('Среднее геометрическое',average_geom)