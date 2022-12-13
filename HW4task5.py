# Дополнительное Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов
# Файл1: 2*x^2 + 4*x + 5
# Файл2: 41*x^3 + 6*x² + 2*x + 98
# Вывод Файл3: 41*x^3 + 8*x^2 + 6*x + 103

def p1(x):
    return 2*x**2 + 4*x + 5

data = open('file1.txt', 'a')
data.writelines(p1)
data.close()

def p2(x):
    return 41*x**3 + 6*x**2 + 2*x + 98

data = open('file2.txt', 'a')
data.writelines(p2)
data.close()

path = 'file1.txt', 'file2.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()
exit()

data = open('file3.txt', 'a')
data.writelines(p2+p1)
data.close()
