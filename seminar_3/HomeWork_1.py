# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

def list_sum(myList):
    sum = 0
    for index in range(len(myList)):
        if index%2==1: continue
        sum+=myList[index]
    print(sum)
my_list = [1,2,3,4,5,6,1,2]
list_sum(my_list)
    
