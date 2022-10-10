# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0,
# с помощью дополнительных библиотек python. Запросите значения А, В, С 3 раза.
# Уравнения и корни запишите в файл.

from math import sqrt

def sqr_r(a,b,c):
    d = b**2-4*a*c
    if a==0:
        return 'error'
    with open('4.2_text.txt','a', encoding='utf-8') as data:
        data.write(f'{a}x² + {b}x + {c} = 0\n')
        if d > 0:
            data.write(f'{(-b+sqrt(d))/(2*a)}\n')
            data.write(f'{(-b-sqrt(d))/(2*a)}\n')
        elif d==0:
            data.write(f'{-b/(2*a)}\n')
        else:
            data.write('no koren')
for i in range(3):
    sqr_r(int(input('a ')),int(input('b ')),int(input('c ')))