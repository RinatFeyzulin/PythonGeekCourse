# 4.* Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

import random
def product_double(double_list):
    new_list = []
    for i in double_list:
        new_list.append(round(i-int(i),3))
    new_list.sort()
    result = round(new_list[-1] - new_list[0],3)
    print('Min:',new_list[0],'  Max:',new_list[-1],'  Difference: ', result)

def random_list(count):
    new_list = []
    for i in range(count):
        new_list.append(round(random.uniform(10.5, 25.5),3))
    return new_list

my_list = random_list(5)
print(my_list)
product_double(my_list)
