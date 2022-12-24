# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import sys
sys.path.append(r'C:\Users\1\Desktop\иван\задания по разработчику\python')
from funcs.functions import*

a = int(input('Введите количество элементов списка: '))
b = int(input('Введите предел диапазона произвольных чисел: '))
array = RandomFloatList(a, b)

for i in range(len(array)):
    array[i]=array[i]%1

print(array)
result = max(array)-min(array)
print(round(result,2))

