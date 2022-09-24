# 4. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

a = int(input('write number 1 to 4\n'))

if(a==1):print('x>0 and y>0')
elif(a==2):print('Ix<0 and y>0')
elif(a==3):print('x<0 and y<0')
elif(a==4):print('x>0 and y<0')
else:print('try again')

