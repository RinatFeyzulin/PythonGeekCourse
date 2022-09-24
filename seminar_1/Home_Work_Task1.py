#1. Напишите программу, которая принимает на вход цифру,
#обозначающую день недели, и проверяет, является ли этот день выходным.

a = int(input("write number day\n"))
if(a<=0 or a>=8): print('there is no such day')
elif(a>5):print('day off')
else:print('working day')