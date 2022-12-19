# Реализуйте алгоритм перемешивания списка.

list = [21,454,1,23,4,865,222]
import random

new_list = []

for i in range(0, len(list)):
    list_el = random.randint(0,len(list)-1)
    new_list.append(i)
    new_list[i]=list[list_el]
    list.pop(list_el)
    

print(new_list)