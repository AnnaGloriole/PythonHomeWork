# 4)Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.

n = int(input('Введите число N: '))
sum = 0
for i in range(n+1):
    if i % 2 == 0:
        sum += i
print(f'сумма четных чисел, распаложенных между числами 1 и {n} включительно \n {sum}')