# 1) Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 120 конфета. Играют два игрока делая ход друг после друга.
# Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
# Победитель - тот, кто оставил на столе 0 конфет.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# 2021 21 ---> 2000 бот4 -> 1996 .... бот --->29 --> 27 >> 2конф
# a) Добавьте игру против бота
# Доп b) Подумайте как наделить бота ""интеллектом"" (Теория игр)

from random import randint as ri
total = 120
taken = 0
player_take = 0
bot_take = 0

def start():
    print('На столе лежит 120 конфета. Играют два игрока делая ход друг после друга.\n За один ход можно забрать не более чем 28 конфет.\n Победитель - тот, кто оставил на столе 0 конфет.')
    player_turn()

# def who_is_first():
#     random_number = ri(1, 2)
#     if random_number == 1:
#         player_turn()
#     else:
#         bot_turn()

def player_turn():
    global total
    global taken
    global player_take
    print (f'Your turn, on the table {total} sweets')
    taken = int(input('Write, please, how many sweets you will take?:'))
    while taken > 28 or taken < 0 or taken > total:
        taken = int(input('неверное количество, try again'))
        
    total -= taken
    player_take += taken
    if total > 0:
        bot_turn()
    else:
        print('You are win!')

def bot_turn():
    global total
    global taken
    global bot_take
    taken = total % 29 if total % 29 !=0 else ri (1, 28)
    total -= taken
    bot_take += taken
    print(f'Bot has taken {taken} sweets. Right now on the table {total} sweets')
    if total > 0:
        player_turn()
    else:
        print('Bot win!')