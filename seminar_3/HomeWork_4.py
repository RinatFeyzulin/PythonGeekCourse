# 4.* Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

def product_double(double_list):
    new_list = []
    for i in double_list:
        new_list.append(round(i-int(i),3))
    new_list.sort()
    result = new_list[-1] - new_list[0]
    print('Min:',new_list[0],'  Max:',new_list[-1],'  Difference: ', result)

product_double([5.16, 8.62, 6.57, 7.92, 9.22])