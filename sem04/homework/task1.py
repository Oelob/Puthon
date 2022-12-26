# ычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math



def AccuracyOfPi(a):
    
    count = 0
    if a >= 10**(-10) and a <= 10**(-1):
        while a < 1:
            a = a*10
            count += 1
        print(round(math.pi,count)) 
    else:
        a = float(input('Необходимая точность находится вне допустимого диапазона. Попробуйте еще раз: '))
        AccuracyOfPi(a)
   
d = float(input('Введите необходимую точность в формате 0.00..1: '))
AccuracyOfPi(d)

    