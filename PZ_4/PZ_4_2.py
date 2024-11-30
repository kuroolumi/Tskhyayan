"""
Вариант 25.
Дано целое число N (>0). Если оно является степенью числа 3, то вывести TRUE,
если не является — вывести FALSE.
"""

while True:
    try:
        N = int(input("Введите целое число N (>0): "))

        if N <= 0:
            print("Ошибка! N должно быть больше 0.")
            continue

        is_aboba_of_3 = False
        aboba = 1

        while aboba < N:
            aboba *= 3

        if aboba == N:
            is_aboba_of_3 = True

        print("TRUE" if is_aboba_of_3 else "FALSE")
        break

    except ValueError:
        print("Ошибка! Введено не целое числовое значение.")
