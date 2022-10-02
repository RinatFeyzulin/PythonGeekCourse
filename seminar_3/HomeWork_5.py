# 5. ** Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи

# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21
def negaFibonachi(number):
    f = 0
    f1 = 1
    i=0
    list_n = []

    while i<number+1:
        list_n.append(f)
        if f!=0:
            if i%2==0:
                list_n.insert(0,-f)
            else:list_n.insert(0,f)
        (f,f1)=(f1,f1+f)
        i+=1
    result = ' '.join(map(str,list_n))
    return result

print(negaFibonachi(8))