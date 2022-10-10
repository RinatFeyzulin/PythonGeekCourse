# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001

from decimal import Decimal 
number = Decimal(input('Enter a real number:'))
number = number.quantize(Decimal(input('Enter the required accuracy 0.0001: ')))
print(number)