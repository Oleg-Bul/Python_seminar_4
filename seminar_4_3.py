# Задайте два числа. Напишите программу,
# которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

a = 5
b = 20
c = 0
for i in range(1, (a*b+1), 1):
    if (i % a == 0) and (i % b == 0):
        c = i
        break

print('НОК = ', c)
