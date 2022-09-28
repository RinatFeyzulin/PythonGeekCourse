# 2. Создать список, длины n, значения формируются по формуле 3k + 1,
# где k принимает значения от 1 до n включительно.

numbers = []
a = int(input("write number"))

for i in range(1, a+1):
    numbers.append(3*i+1)

print(numbers)