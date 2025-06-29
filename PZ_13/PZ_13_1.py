# Вариант 3
# 1. Увеличить элементы на главной диагонали матрицы в 2 раза


matrix = [
    [1, -2, 3],
    [4, 5, -6],
    [7, 8, 9]
]

print("Исходная матрица:")
for row in matrix:
    print(row)

matrix = [[matrix[i][j] * 2 if i == j else matrix[i][j] for j in range(len(matrix[i]))] for i in range(len(matrix))]

print("\nМатрица после увеличения элементов на главной диагонали:")
for row in matrix:
    print(row)