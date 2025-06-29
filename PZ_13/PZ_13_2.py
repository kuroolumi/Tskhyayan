# Вариант 3
# 2. Сформировать массив из положительных четных элементов, найти их сумму и среднее арифметическое

matrix = [
    [1, -2, 3],
    [4, 5, -6],
    [7, 8, 9]
]


positive_even_elements = [num for row in matrix for num in row if num > 0 and num % 2 == 0]
sum_elements = sum(positive_even_elements)
average = sum_elements / len(positive_even_elements) if positive_even_elements else 0

print("\nПоложительные четные элементы:", positive_even_elements)
print("Сумма:", sum_elements)
print("Среднее арифметическое:", average)