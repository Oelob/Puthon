# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

N = int(input('Введите число '))

list = []
num_position = []
j = 0
for i in range(-N,N+1):
    list.append(None)
    list[j] = i
    j = j + 1
print(list)

text = open(r'sem02\homework\file.txt','r')
print(text)
sum = 0
for i in text.read():
    try:
        i = int(i)
        sum += list[i]
    except:
        continue
print(sum)