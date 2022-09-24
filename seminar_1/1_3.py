a = int(input('write number '))
if(a<0):a = -a
b = -a

for i in range(a*2+1):
    print(b,end=' ')
    b+=1
