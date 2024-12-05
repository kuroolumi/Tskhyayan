"""
Даны множества A и B, состоящие соответственно из N1 и N2 точек (точки заданы
своими координатами x, у). Найти минимальное расстояние между точками этих
множеств и сами точки, расположенные на этом расстоянии (вначале выводится
точка из множества A, затем точка из множества B).
Расстояние R между точками с координатами (x1, y1) и (x2, у2) вычисляется по формуле:
R = √(x2 – x1)2 + (у2 – y1)2.
Для хранения данных о каждом наборе точек следует использовать по два списка: первый
список для хранения абсцисс, второй — для хранения ординат.
"""

import random

# функция будет вычислять расстояник между двумя точками
def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


# координаты xy для множества A
A_x = [random.randint(1, 100) for i in range(3)]  # Абсциссы точек A
A_y = [random.randint(1, 100) for il in range(3)]  # Ординаты точек A

# координаты xy для множества B
B_x = [random.randint(1, 100) for ilu in range(3)]  # Абсциссы точек B
B_y = [random.randint(1, 100) for lumi in range(3)]  # Ординаты точек B

# переменные для данных
min_distance = float('inf')
closest_point_A = None
closest_point_B = None


for k in range(len(A_x)):
    for j in range(len(B_x)):
        distance = calculate_distance(A_x[k], A_y[k], B_x[j], B_y[j])  # расстояние между точками A и B

        # если расстояние меньше минимального, минимальное значение и точки обновляются
        if distance < min_distance:
            min_distance = distance
            closest_point_A = (A_x[k], A_y[k])  # Сохраняем точку из A
            closest_point_B = (B_x[j], B_y[j])  # Сохраняем точку из B

# вывод результатов вычислений
print(f"Минимальное расстояние: {min_distance}")
print(f"Точка из A: {closest_point_A}")
print(f"Точка из B: {closest_point_B}")
