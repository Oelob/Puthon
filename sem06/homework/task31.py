# Задача 31: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]

import random

original_list = [random.randint(-20,20) for i in range(20)]
print(original_list)

user_range_min = int(input('Введите нижнюю границу диапазона: ')) 
user_range_max = int(input('Введите верхнюю границу диапазона: '))

result = []
for indx, val in enumerate(original_list):
    if user_range_min<=val<=user_range_max:
         result.append(indx)
print(result) 
