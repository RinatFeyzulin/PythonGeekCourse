# 3. Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7

import random
 
def random_list(n):
    if n < 0:
        print('Negative or 0 value of the number of numbers!')
        return []
    l=[]
    for i in range(n):
        l.append(random.randrange(1, 10))
    print(l)
    return l
    

def unicum_number(op):
    if len(op) == 0:
        return []
    l=op
    new_l=[]
    for i in l:
        count=0
        for q in l:
            if q==i: count+=1
        if count==1:
            new_l.append(i)
    print(new_l)
    return new_l
    
unicum_number(random_list(-7))
