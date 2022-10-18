# 3. Создайте программу для игры в "Крестики-нолики". Поле 3x3. Игрок - игрок, без бота.

l4=([i for i in range(1,10)])
player='X'

def board():
    print(f'\n{"-"*20}')
    for q in range(3):
        for k in range(3):
            print(f'{l4[k+q*3]:^5}', end=' ')
        print(f'\n{"-"*20}')

def win():
    global player
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in win_coord:
        if l4[i[0]]==l4[i[1]]==l4[i[2]]:
             player=l4[i[0]]
             return True
        else: return False
 
def game_play():
    global player
    board()
    while True:
        pos=input(f'Player turn {player} ')
        if pos.isdigit():
            if int(pos)>9:
                print('Position out of bounds')
                continue
            if l4[int(pos)-1]=='X' or l4[int(pos)-1]=='O':
                print('Position occupied')
                continue
            l4[int(pos)-1]=player
            if player=='X':
                 player='O'
            else: player='X'
            board()
        else:
            print('no position')
            continue
        if win():
            print(f'WIN player - {player}')
            break

game_play()


