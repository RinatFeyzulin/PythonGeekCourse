# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#    Напишите программу, которая определит, присутствует ли в заданном списке число,
#    полученное от пользователя.

from random import sample

def num_in_list(count, number):
    if count<0:
        return "error"
    myList = sample(range(1,count * 2), count )
    print(myList)
    if number in myList:
        return 'yes'
    return 'no'

print(num_in_list(int(input()), int(input())))