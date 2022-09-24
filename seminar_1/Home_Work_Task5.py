# AB = √(xb - xa)2 + (yb - ya)2

# 5.Напишите программу, которая принимает на вход координаты 
# двух точек и находит расстояние между ними в 2D пространстве.

x1 = float(input('write A "x"\n'))
y1 = float(input('write A "y"\n'))

x2 = float(input('write B "x"\n'))
y2 = float(input('write B "y"\n'))

print(((x1-x2)**2 + (y1-y2)**2)**0.5)

