"""
Дан целочисленный список размера N. Проверить, чередуются ли в нем четные и нечетные числа.
Если чередуются, то вывести 0, если нет, то вывести порядковый номер первого элемента,
нарушающего закономерность.
"""

import random

def check(aboba_num):
    for i in range(1, len(aboba_num)):
        # проверка четности текущего и предыдущего чисел
        if (aboba_num[i] % 2) == (aboba_num[i - 1] % 2):
            # вывод индекса при одинаковой четности чисел
            return i + 1
    return 0  # если чередование соблюдено

# список из 5 рандомных чисел от 1 до 100
numbers = [random.randint(1, 100) for i in range(5)]

# список наших чисел
print("РАНДОМ:", numbers)

# проверка чередования чисел в списке
result = check(numbers)
print(f"номер числа, ломающее закономерность: {result}")
