# 5. ** Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]
import random
from random import randint

listT = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(listT)
print(listT)


listA = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
listA.reverse()
print(listA)


## с использование библиотеки random без метода shuffle
listB = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n=len(listB)-1
for i in range(n):
    x = randint(0,n)
    listB[i],listB[x] = listB[x], listB[i]
print(listB)



## без использования библиотеки random
listC = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n=len(listC)-1
x = 1
for i in range(n):
    if(i>n-2):
        x = 2 
    listC[i],listC[x] = listC[x], listC[i]
    listC.reverse()
    x+=1
print(listC)