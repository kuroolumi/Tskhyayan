"""
Вариант 25.
Даны два целых числа A и B (A < B). Вывести в порядке возрастания все целые
числа, расположенные между A и B (включая сами числа A и B), а также количество
N этих чисел.
"""

while True:
    try:
        A = int(input("Введите число A: "))
        B = int(input("Введите число B: "))

        if A < B:
            print("Числа между A и B (включительно):")
            count = 0  # Счетчик для количества чисел
            for number in range(A, B + 1):
                print(number)
                count += 1

            # Выводим количество чисел
            print("Количество чисел:", count)
            break
        else:
            print("Ошибка! A должно быть меньше, чем B.")
    except ValueError:
        print("Ошибка! Введено не целое числовое значение.")
