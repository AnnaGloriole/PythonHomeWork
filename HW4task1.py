# Вычислить число Pi c заданной точностью d, не используя ф. round()
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from math import pi
number = int(input())
stroka = str(pi)
print(stroka[0:number+2])