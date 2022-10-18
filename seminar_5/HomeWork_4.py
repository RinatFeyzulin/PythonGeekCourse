# 4. ** Создайте программу для игры с конфетами человек против человека.

#    Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
#    Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
#    Все конфеты оппонента достаются сделавшему последний ход.
#    Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

#    1. Добавьте игру против бота
#    2. Подумайте как наделить бота "интеллектом"

from random import shuffle,randint

CONFITI=2021
CONFITI_LIMIT=28

player = ['Player','bot' if int(input('write if bot "1" or if player "0" ')) else 'Person']
shuffle(player)

player_current=player[0]

def count_CONFITI(count):
    global CONFITI, CONFITI_LIMIT,player_current
    if count>CONFITI_LIMIT or count>CONFITI:
        print('Take a number no greater than the specified limit')
        print(f'Осталось {CONFITI} конфети')
        return
    CONFITI-=count
    if CONFITI==0:
        print(f"\n------WIN player {player_current}-------")
        return 
    if player_current==player[1]:
        player_current=player[0]
    else:player_current=player[1]

def bot_run(candies: int) -> int:
    result = candies % 29
    if not result:
        result = randint(1, 28)
    return result

def game_play():
    while CONFITI:
        print(f'Ход за  {player_current}')
        if player_current=='bot':
            a=bot_run(CONFITI)
            count_CONFITI(a)
            print(f'{a}')
        else:
            a=int(input('введите количество конфет '))
            count_CONFITI(a)
        
        print(f'\nОсталось {CONFITI} конфети')
    
game_play()

