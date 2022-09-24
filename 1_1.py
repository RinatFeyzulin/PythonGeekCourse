# 1. Напишите программу, которая принимает на вход два числа
# и проверяет, является ли одно число квадратом другого.

a = int(input('write number first\n'))
b = int(input('write number second\n'))

if(a == b**2 or a**2 == b): print('yes')
else:print('no')

