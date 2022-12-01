# 3) Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, 
# который вы сами заполняете.
# Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]
# Ввод: 4
# [-4, -3, -2, -1, 0, 1, 2, 3,4]

n = int(input('Введите число N: '))
list1 = [i for i in range(-n, n+1)]
print(list1)
# list2 = [3, 0, 5, 4, 7]
from random import randint
list2 = []
for i in range(5):
    list2.append(randint(0, 10))
print(list2)
proiz = 1
for index in list2:
    proiz *= list1[index]
    print(list1[index])
print(proiz)