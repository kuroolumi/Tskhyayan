import random
import math

# Генерация последовательности чисел
numbers = [random.randint(-100, 100) for _ in range(20)]
while all(n >= 0 for n in numbers):  # Убедимся, что есть отрицательные числа
    numbers = [random.randint(-100, 100) for _ in range(20)]

# Запись исходных данных в файл
with open('source.txt', 'w', encoding='utf-8') as f:
    f.write(' '.join(map(str, numbers)))

# Обработка данных
count = len(numbers)
max_num = max(numbers)
first_half = numbers[:len(numbers)//2]
product = math.prod([n for n in first_half if n < 0])

# Запись результатов в новый файл
with open('result.txt', 'w', encoding='utf-8') as f:
    f.write(f"""Исходные данные: {' '.join(map(str, numbers))}
Количество элементов: {count}
Максимальный элемент: {max_num}
Произведение элементов меньших 0 в первой половине: {product}""")

print("Файлы source.txt и result.txt созданы успешно.")
