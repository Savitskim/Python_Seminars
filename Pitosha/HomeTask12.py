# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3
x = int(input('Введите сумму чисел: '))
y = int(input('Введите произведение чисел: '))
d = x*x-4*y
if d == 0:
    print(round(x/2), round(x/2))
if d > 0:
    print(round((x-d)/2), round((x+d)/2))
if d < 0:
    print('Таких чисел нету')
