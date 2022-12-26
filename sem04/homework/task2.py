# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

a = int(input('Введите число, простые множители которого необходимо получть: '))

list = []
while a != 1:
    if a%2 == 0:
        a = a/2
        list.append(2)
    elif a%3 == 0:
        a = a/3
        list.append(3)
    elif a%5 == 0:
        a = a/5
        list.append(5)
    elif a%7 == 0:
        a = a/7
        list.append(7)
    
print(list)