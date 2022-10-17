# 1. В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие
# A[i] - 1 = A[i-1]. Найдите это число.
from random import choice

def list_p(list):
    for i in range(1,len(list)):
        if list[i]-1!=list[i-1]:
            print(list[i]-1)
            return list[i]-1
    return -1

def new_list(count):
    my_list = [x for x in range(count+1)]
    print(my_list)
    my_list.remove(choice(my_list))
    print(my_list)
    return my_list

l=new_list(5)

print(list_p(l))