# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.


# a = int(input('Введите натуральное число: '))


# def Find_Fibonachi(x):
#     list = [0, 1, 1]
#     index = 2
#     while x > list[index]:
#         list.append(list[index]+list[index-1])
#         index += 1
#     if x == list[index]:
#         return index+1
#     else:
#         return -1


# print(f'Оно является {Find_Fibonachi(a)} числом по счету')
num_input = int(input('Введите число: '))
n1, n2 = 0, 1
n_num = 2
while n2 < num_input:
    n1, n2 = n2, n2+n1
    n_num += 1
if num_input == n1:
    print(f'{num_input} является 1 по счету числом Фибоначчи')
else:
    if num_input == n2:
        print(f'{num_input} является {n_num} по счету числом Фибоначчи')
    else:
        print(-1)
