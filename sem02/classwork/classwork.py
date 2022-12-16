# 11. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
    
#     *Пример:*
    
#     - Для N = 5: 1, -3, 9, -27, 81
n = int(input())
num = 1
print(num, end = " ")
for i in range(1,n):
    num*=-3
    print(num, end = " ")

# 12. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
    
#     *Пример:*
    
#     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input())
a = {}
for i in range(1,n+1):
    a[i] = i*3+1
print(a)

# 13. Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.

one = input()
two = input()
# count = 0
# for i in range(len(one)-len(two)+1):
#     if one[i:i+len(two)] == two:
#         count += 1
# print(count)
print(one.count(two))


# 1)Создайте список из случайных чисел. Найдите максимальное количество его одинаковых элементов.
import random

number = int(input())
maxRandom = int(input('input max random number'))
maxAmount = 0

list = []
count = [0] * (maxRandom+1)

for i in range(0, number):
    list.append(random.randint(0, maxRandom))

for i in list:
    count[int(i)] += 1

for i in count:
    if i > maxAmount:
        i = maxAmount

print(list)
print(max(count))
print('МАскимально количество раз появилась ' + str(count[maxAmount]) + ', ' + str(maxAmount+1) + ' раз')



# 2)Данная программа должна вывести n рядов, заполненных знаком ‘*’ определенным образом. А именно: в первом ряду должно быть n «звездочек», в втором n-1, и так далее. А в последнем ряду таким образом будет одна «звездочка». Причем убывать эти «звездочки» должны слева направо. Число n вводится пользователем.
# Введите количество рядов: 5
# *****
# ****
# ***
# **
# *



