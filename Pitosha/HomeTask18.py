# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5
from random import randint


def ok(x, list_x):
    find_ok = float("inf")
    for i in list_x:
        if abs(x-i) <= find_ok:
            find_ok = abs(x-i)
            ok = i
    return ok


size = int(input('Введите размер массива: '))
list_1 = []
i = 0
count = 0
while i < size:
    list_1.append(randint(0, 10))
    i += 1
print(list_1)
find = int(
    input('Введите число, чтобы узнать наиболее приближенное: '))
print(ok(find, list_1))
