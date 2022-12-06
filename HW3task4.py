# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# вариант 1 

n = int(input())
a = ""
while n > 0:
    a = str(n%2) + a
    n = n // 2
print(a)

# вариант 2

# n = int(input())
# binary = 0
# k = 1
# while n > 0:
#     div = n % 2
#     binary = binary + div*k
#     n = n // 2
#     k *= 10
# print(binary)