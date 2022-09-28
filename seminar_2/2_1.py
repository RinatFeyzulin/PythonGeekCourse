# 1. Напишите программу, которая принимает на вход число N
#  и выдаёт последовательность из N членов.

# a = int(input('write number'))
# n = 1

# for i in range(a):
#     print(n, end=' ')
#     n*=-3

a = int(input('write number'))

for i in range(a):
    print((-3)**i, end=' ')
   