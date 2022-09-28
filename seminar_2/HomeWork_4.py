# * 4. Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов, 
# заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15

numb = int(input('write numb '))
number = []

for i in range(-numb,numb+1):
    number.append(i)
print(number)

pos_one = int(input('write Position one '))
pos_two = int(input('write Position two '))

print(number[pos_one-1] * number[pos_two-1])

