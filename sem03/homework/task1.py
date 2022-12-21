# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

list = []*9
for i in range (9):
    list.append(random.randint(0,9))
    
print(list)

sum = 0
for i in range (1, len(list), 2):
    sum += list[i]
    
print(sum)