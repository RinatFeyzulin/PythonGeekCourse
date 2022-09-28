# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

numb = input('write number\n')
numbLen = len(numb)-1
numb = float(numb) * (10**numbLen)
sum = 0

while numb!=0:
    sum +=int(numb%10)
    numb /=10
print(sum)