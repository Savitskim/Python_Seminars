# Задача 26
# Напишите программу, которая на вход принимает два числа A и B, и
# возводит число А в целую степень B с помощью рекурсии.

# Пример:

# A = 3; B = 5 -> 243 (3**5)
# A = 2; B = 3 -> 8


def power(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    if b != 1:
        return a * power(a, b - 1)


a = int(input('А = '))
b = int(input('B = '))
print(power(a, b))
