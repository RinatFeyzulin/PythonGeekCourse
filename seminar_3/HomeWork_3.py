# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000

from operator import index


def number_byte(number):
    byte_list = []
    while number:
        byte_list.append(int(number%2))
        number = int(number)/2
    byte_list.reverse()
    byte_list.remove(index(byte_list[0]))
    byte_string = ''.join(map(str,byte_list))
    return byte_string
print(number_byte(88))
