"""
Найти сумму чисел ряда 1,2,3,4,... от числа n до числа m. Суммирование оформить
функцией с параметрами. Значения n и m программа должна запрашивать.
"""


def sum_range(n, m):
    if n > m:
        return 0
    return sum(range(n,m + 1))

n = int(input('Введите n'))
m = int(input('Введите m'))

aboba = sum_range(n ,m)
print(f'сумма чисел равна: {aboba}')
