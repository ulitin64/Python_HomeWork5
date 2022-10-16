# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

def sweet_game(player_move):
    user = False
    count = 1
    while player_move > 0:
        user_request = int(input(f'Игрок {int(user)+1} введите количество конфет (от 1 до 28): '))
        while user_request > 28:
            print(f'Игрок {int(user)+1} повторите ввод!')
            user_request = int(
                input(f'Игрок {int(user)+1} введите количество конфет (от 1 до 28): '))
        player_move -= user_request
        print(player_move)
        count += 1
        user = not(user)
        if player_move == 0:
            print(f'Игрок {int(user)+1} победил!')


def sweet_bot(player_move):
    return (player_move % 29) - 1

sweet_game(100)




