# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random


k = int(input('Введите степень: '))

coeffitient = []
list_x = []
result = ''
indexes = {"0": "\u2070",
           "1": "\u00B9",
           "2": "\u00B2",
           "3": "\u00B3",
           "4": "\u2074",
           "5": "\u2075",
           "6": "\u2076",
           "7": "\u2077",
           "8": "\u2078",
           "9": "\u2079"
        }

def degree(a: int):
    degrees = ""
    temp = str(a)
    for char in temp:
        degrees += indexes[char] or ""
    return degrees   

for i in range(k+1):
    coeffitient.append(random.randint(0,100))
print(coeffitient)

for i in range(k,0,-1):
    if i == 1:
        list_x.append('x')
    else:
        list_x.append(f'x{degree(i)}')
print(list_x)

for i in range(k):
    result = result + (f'{coeffitient[i]}*{list_x[i]} + ')
result = result + (f'{coeffitient[-1]} = 0')
    
print(result)

f = open(r'sem04\homework\result_task4.txt','w',encoding='utf-8')
f.write(result)