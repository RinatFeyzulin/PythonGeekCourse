# Дан список чисел. Создайте список в который попадают
# числа, описывающие возрастающую последовательность.
# in 8

# [10,0,5,11,6,1,15,10]

# out [[10,11,15],[0,5,11,15], [5,11,15],[11,15],[6,15],[1,15]]

from random import randint

def list_random_number(count):
    lst = [randint(0, 20) for i in range(count)]
    print(lst)
    return lst
    

def list_k(lst):
    new_list=[]
    for i in range(len(lst)):
        p_list=[lst[i]]
        lst_i=lst[i]
        for k in range(i+1,len(lst)):
            if lst_i<lst[k]:
                p_list.append(lst[k])
                lst_i=lst[k]
        if len(p_list)>1:new_list.append(p_list)
    print(new_list)


list_k(list_random_number(8))