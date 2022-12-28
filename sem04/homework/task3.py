# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import sys
sys.path.append(r'C:\Users\1\Desktop\иван\задания по разработчику\python')
from funcs.functions import*

num_list = RandomList(8, 10)
print(num_list)

result = [None]
for el in num_list:
    for i in range(len(result)):
        if el != result[i]:
            
            if result[i] == None:
                result[i] = el
                result.append(None)
            else:
                continue
        else:
            break
result.pop(-1)    
print(result) 
 