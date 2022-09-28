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



listB = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n=len(listB)-1
for i in range(n):
    x = randint(0,n)
    listB[i],listB[x] = listB[x], listB[i]
print(listB)