# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

N = int(input('Введите число '))
list = []
list.append(1)
print(list)
for i in range(1,N+1):
    list.append(i)
    list[i] = list[i-1]*i
list.pop(0)
print(list)