# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list = input("please enter elemets use split\n").split()
list2 = []
i = 0
while (i < len(list)//2 + len(list)%2):
    numb = len(list) - i - 1
    list2.append(int(list[i]) * int(list[numb]))
    i+=1
print(list2)

