# задача 2. Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

N = int(input('Введите натуральное число: '))

def simple_multiplier(num):
    list = []
    for i in range(1, num+1):
        if num%i == 0:
            list.append(i)
            num //= i
    return list

print(f'простые множители: {simple_multiplier(N)}')