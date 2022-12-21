# 19. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

# import datetime
# a=int(input())
# a = str(a)
# b=len(a)
# nums = datetime.datetime.now().microsecond%10**b
# print(nums)

a = ['qwe', '3213']
flag = False
for i in a:
    if i.isdigit():
        flag = True
        break

print(flag)
        
a = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
b = 'qwe'
j = 0
for i in range(len(a)):
    if a[i] == b:
        j+=1
        if j == 2:
            print(i)
            break
if j !=2:
    print("нет второго вхождения")

        