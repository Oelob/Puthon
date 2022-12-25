# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

a = int(input('Введите число: '))
result = ''
while a != 0:
    temp = str(f'{a%2}')
    result = result + temp
    
    a = a//2
# result = result[::-1]
result = ''.join(reversed(result))
result = int(result)


print(result)
