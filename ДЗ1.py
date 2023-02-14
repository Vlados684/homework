from math import sqrt


print ('Вариант 21 \n  a) 17/19 = 0.895, sqrt(52) = 7,21 \n  б) 7,52 и 0,12% \n  в) 0,5748')
print(' ')

num_1 = 0.895
num_2 = 7.21


num_11 = round(17/19, 8)
num_22 = round(sqrt(52), 8)


limit_1 = num_11 - num_1
limit_2 = num_22 - num_2


percentage_1: float = round((limit_1 / num_1) * 100, 6)
percentage_2: float = round((limit_2 / num_2) * 100, 6)

print(
    f'Сравниваем погрешности {percentage_1} и {percentage_2}.'
)

if percentage_1 > percentage_2:
    print(
        f'a) Ответ: {num_1} точнее.'
    )
else:
    print(
        f'a) Ответ: {num_2} точнее.'
    )


num_a = 7.521
num_b = 0.0012
num_b_b = round((num_a * num_b), 5)

print(
    f'Так как {num_b} < 0,005, то в числе {num_a} '
    f'верными в узком смысле являются цифры 7,5,2'
)

num_b1 = num_b + 0.001

print(
    f'Полученная погрешность меньше 0,005, '
    f'то оставшиеся цифры верны в узком смысле. '
)

print(
    f'б) Ответ: {round((num_a), 2)}'
)


num_c: float = 0.5748
num_c1: float = 0.00005
num_c2: float = num_c1 / num_c

print(
    'в) Абсолютная погрешность:', 0.0005
)
print(
    'Относительная погрешность:', round((num_c2), 4)
)
