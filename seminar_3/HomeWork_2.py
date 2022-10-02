# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.


def list_product(myList):
    new_list = []
    pos=0
    neg=-1
    lenList = len(myList)
    
    while pos<lenList/2:
        new_list.append(myList[pos]*myList[neg])
        pos+=1
        neg-=1

    print(new_list)

list_product([5,2,1,5,10])
