# 4.* Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена, 
# записать в файл полученный многочлен не менее 3-х раз.
# in
# 9
# 5
# 3

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0

import random
def mnogochlen(n):
    list_mnogochlen = []
    for y in range(n):
        n=int(input('write number\n'))
        res=''
        for i in range(n,0,-1):
            r1=str(random.choice('0123456789'))
            r2=str(random.choice('+-'))
            if r1=='0':continue
            else: res +=r1+'*x^'+str(i)+' '+r2+' '
        r3=str(random.choice('0123456789'))
        res+=r3+' = 0'
        list_mnogochlen.append(res)
        print(res)
    print(f'{list_mnogochlen}\n')
    return list_mnogochlen

def record_in_file_poly(lisT):
    with open('poly.txt','a') as data:
        for i in range(len(lisT)):
            data.write(f'{lisT[i]}\n')

def record_in_file_poly2(lisT):
    with open('poly_2.txt','a') as data:
        for i in range(len(lisT)):
            data.write(f'{lisT[i]}\n')


record_in_file_poly(mnogochlen(3))
record_in_file_poly2(mnogochlen(3))
