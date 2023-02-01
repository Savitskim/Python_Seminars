# Задача 2: Найдите сумму цифр трехзначного числа.
number = int(input("Введите трехзначное число: "))
result = 0
if number < 0:
    number *= -1
if 99 < number < 1000:
    while number > 0:
        result += number % 10
        number //= 10
    print(result)
else:
    print("Число не является трехзначным!")
