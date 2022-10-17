# 3. Создайте программу для игры в "Крестики-нолики". Поле 3x3. Игрок - игрок, без бота.

# НЕДОДЕЛАННАЯ



l1=[1,2,3]
l2=[4,5,6]
l3=[7,8,9]

player=1

for i in range(9):
    numb = int(input('write '))
    if numb in l1:
        if player:
            l1[numb-1]= 'X'
            player=0
        else:
            l1[numb-1] = 'O'
            player=1
    if numb in l2:
        i=l2.index(numb)
        if player:
            l2[i]= 'X'
            player=0
        else:
            l2[i] = 'O'
            player=1
    if numb in l3:
        i=l3.index(numb)
        if player:
            l3[i]= 'X'
            player=0
        else:
            l3[i] = 'O'
            player=1
    print(f'{l1}\n{l2}\n{l3}')


