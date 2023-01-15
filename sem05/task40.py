# 40. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
# Также должно работать и для букв:
# Входные данные:
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные:
# 6A1F2D7C1A17E
# (5 - количество единиц, далее сама единица, 4 - количество двоек, далее сама двойка и т.д)
# Модуль восстановления работет в обратную сторону - из строки выходных данных, получить строку входных данных.

data = open(r'sem05\input_data(task40).txt','r')
new_str = data.read()
print(new_str)
result = ''
temp = ''

# модуль сжатия
for element in new_str:
    if element != temp:
        temp = element
        result += element
        result += str(new_str.count(element))
print(result)
output_data = open(r'sem05\output_data(task40).txt','w')
output_data.write(result)
output_data.close()

# модуль восстановления
new_result = ''
for element in range(1,len(result),2):
    new_result += result[element - 1 ]*int(result[element])
print(new_result)
    
output_data = open(r'sem05\output_data(task40).txt','a')
output_data.write(f'\n{new_result}')
output_data.close()   
    
    



