# 3. Задайте два числа. Напишите программу, которая найдёт
# НОК (наименьшее общее кратное) этих двух чисел.

from math import gcd
a=int(input())
b=int(input())
print(a*b//gcd(a,b))
print(gcd(a,b))
