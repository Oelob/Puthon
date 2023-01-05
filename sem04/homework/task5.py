list_examples = []
data = open(r'sem04\homework\result_task5.txt','r')
for i in data:
    list_examples.append(i)
data.close()
exm1 = list_examples[0]
exm2 = list_examples[1]

# Прописываем функцию для красивого отображения степени
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

# Создаем функцию, в которой получим из строки словарь, где ключом будет степень Х, а значением будет аргумент при Х.
def GetDict(str):
    # редактируем полученную строку, избавляемся от лишних знаков
    # str_new = str[:-2]   
    str_new = ''
    for i in range(len(str)):
        if str[i] != '=':
            str_new = str_new + str[i]
        else:
            break             
    str_new = str_new.replace('^','')
    str_new = str_new.replace('*','')
    
    # Если первый аргумент отрицательный, приходится искуственно обрезать строку, чтобы сохранить "-" для дальнейших вычислений
    if str_new[0] == '-':
        temp = str_new[0]
        str_new = str_new[1:len(str_new)]
        str_new = str_new.replace('-','+-')
        str_new = temp + str_new
    else:
        str_new = str_new.replace('-','+-')
    
    # создаем список отдельных элементов, убираем "х". Готовим список для создания словаря
    list_str = str_new.split('+') 
    list2_str = []
    for i in list_str:
        list2_str.append(i.split('x'))
    for i in range(len(list2_str)):
        for j in range(len(list2_str[i])):
            if list2_str[i][j] == '':
                list2_str[i][j] = '1'
    
    # Переводим аргумент перед Х в числовой тип,чтобы производить арифметические действия 
    for i in range(len(list2_str)):
        for j in range(len(list2_str[i])):
            list2_str[i][j] = int(list2_str[i][j])
        
    
    # создаем словарь на основе списка для дальнейшего сложения многочленов
    dict_str = {}
    if str_new[-1] == 'x' or str_new[-2] == 'x':
        for i in range(len(list2_str)):
            dict_str.setdefault(list2_str[i][1],list2_str[i][0])
        # dict_str.setdefault(0,list2_str[-1][0])
    else:
        for i in range(len(list2_str)-1):
            dict_str.setdefault(list2_str[i][1],list2_str[i][0])
        dict_str.setdefault(0,list2_str[-1][0])
      
    return dict_str

dict1 = GetDict(exm1)
print(dict1)

dict2 = GetDict(exm2)
print(dict2)

# Создаем общий словарь для формирования результирующего многочлена
dict3 = {}

# формируем список ключей для единого словаря
list_keys = [key for key in dict1.keys()]
list_keys = list_keys + [key for key in dict2.keys()]
set_keys = set(list_keys)
list_keys = list(set_keys)
list_keys.reverse()
print(list_keys)

# создаем общий словарь
for i in range(len(list_keys)):
    if list_keys[i] in dict1.keys() and list_keys[i] in dict2.keys():
        dict3.setdefault(list_keys[i],dict1[list_keys[i]]+dict2[list_keys[i]])
    elif list_keys[i] in dict1.keys():
        dict3.setdefault(list_keys[i],dict1[list_keys[i]])
    elif list_keys[i] in dict2.keys():
        dict3.setdefault(list_keys[i],dict2[list_keys[i]])
print(dict3)

# Формируем результирующий многочлен
result = ''

for key,value in dict3.items():
    if key == 1:
        if value < 0:
            result = result[:-1] + f'{value}x'
        elif value > 0:
            result = result + f'{value}x+'
        elif value == 0:
            continue
        elif value == 1:
            result = result + f'x+'
        continue 
    if key == 0:
        if value < 0:
            result = result[:-1] + f'{value}'
        elif value > 0:
            result = result + f'{value}+'
        elif value == 0:
            continue
        elif value == 1:
            result = result + f'x+' 
    else:
        if value < 0:
            result = result[:-1] + f'{value}x{degree(key)}+'
        elif value > 0:
            result = result + f'{value}x{degree(key)}+'
        elif value == 0:
            continue
        elif value == 1:
            result = result + f'x{degree(key)}+' 
if result[-1] == '+':
    result = result[:-1]
result = result + '=0'
        
print(result)

data_new = open(r'sem04\homework\result_task5.txt','a',encoding='utf-8')
data_new.write(f'\n{result}')


