# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# Пример:

# - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}

N = int(input('Введите число '))
import math 
list = []

for i in range(1, N+1):
    list.append(i)
    list[i-1] = math.pow((1 + 1/i), i)
    
print(list)
print(round(sum(list),2))
 
