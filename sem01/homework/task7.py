# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
x = 0
y = 0
z = 0

for x in range(0,1):
    for y in range(0,1):
        for z in range(0,1):
            if -(x and y and z) == -x or -y or -z:
                print(True) 
            else:
                print(False)