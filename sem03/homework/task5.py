# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

a = int(input('Введите число: '))


result = [0,1]

for i in range(2,a+1):
    result.append(result[i-1]+result[i-2])
        

print(result)        
result.reverse()
print(result)        

for i in range (len(result),len(result)+a):
    result.append(result[i-1]+result[i-2])
 
for i in range (len(result)//2,len(result),2):
    result[i] *= -1   
result.reverse()
print(result)