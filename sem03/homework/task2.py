# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import sys
sys.path.append(r'C:\Users\1\Desktop\иван\задания по разработчику\python')
from funcs.functions import*

a = int(input('Введите количество элементов списка: '))
b = int(input('Введите предел диапазона произвольных чисел: '))
array = RandomList(a, b)

result = []
print(array)
i = 0
if len(array)%2 == 0:
    while i != len(array)/2:
        result.append(array[i]*(array[-1-i]))
        i += 1 
else:
    while i != len(array)//2:
        result.append(array[i]*(array[-1-i]))
        i += 1 
    result.append(array[len(array)//2]**2)

print(result)

