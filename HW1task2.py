# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

x = float(input('Введите координату Х '))
y = float(input('Введите координату Y '))

if x > 0 and y > 0: print('Точка в 1 четверти плоскости')
elif x < 0 and y > 0: print('Точка во 2 четверти плоскости')
elif x < 0 and y < 0: print('Точка в 3 четверти плоскости')
elif x > 0 and y < 0: print('Точка в 4 четверти плоскости')
elif x == 0 and y == 0: print('zero')
else: print('Точка на оси координат')
