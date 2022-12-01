# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input('Введите число N: '))
if number < 0: number = number * -1

list = []
f = 1
for i in range(1, number + 1):
    list.append(i*f)
    f *= i
print(list)