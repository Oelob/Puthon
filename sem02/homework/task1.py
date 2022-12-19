# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

print('Введите число ')
a = list(input())
sum = 0
for i in range(0, len(a)):
    try:
        a[i] = int(a[i])
        sum += a[i]
    except:
        continue

print(sum)


