import math as m
from decimal import Decimal

x=Decimal(input())
y=Decimal(input())

result=(m.fabs(x)-m.fabs(y))/(1+m.fabs(x*y))

print('Ответ:',result)