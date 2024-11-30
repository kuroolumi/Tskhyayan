"""
Описать функцию DigitCountSum(K, C, S), находящую количество C цифр целого
положительного числа K, а также их сумму S (K — входной, C и S — выходные
параметры целого типа). С помощью этой функции найти количество и сумму цифр
для каждого из пяти данных целых чисел.
"""


def DigitCountSum(K):
    Miau = str(K)

    C = len(Miau)

    S = sum(int(digit) for digit in Miau)

    return C, S


aboba = [99, 1930, 430, 11037, 1058, 4]

for number in aboba:
    count, digit_sum = DigitCountSum(number)
    print(f"Число: {number}, Количество цифр: {count}, Сумма цифр: {digit_sum}")
