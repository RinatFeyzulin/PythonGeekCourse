# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Простые делители числа

# in
# 54
# out
# [2, 3, 3, 3]

def factor_numb(n):
    p=2
    l=[]
    while p<=n:
        if n%p==0:
            n/=p
            l.append(p)
        else:
            p+=1
    print(l)
    return l
factor_numb(9990)