# задача 3. Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


spisok = [int (i) for i in input('input digits use split').split()]
result = []
for i in spisok:
    if spisok.count(i) == 1:
        result.append(i)
print('the number occurs only once')

# list1 = [1, 4, 6, 10, 45, 1, 4, 52, 6, 7, 74, 10, 1, 354, 52, 10, 74]
# list2 = list(range(17))
# print(list1)

# def sort_one_time(inp_list):
#     for i in range(len(inp_list)-2, -1, -1):
#         if inp_list[i] in inp_list[i+1:]: inp_list.pop(i)
#     print(inp_list)

# sort_one_time(list1)
# sort_one_time(list2)