"""
Даны два списка A и B одинакового размера N. Сформировать новый список C того
же размера, каждый элемент которого равен максимальному из элементов списков
A и B.
"""


import random

# списки a и b, которые генерируют 5 рандомных чисел от 1 до 100
A = [random.randint(1, 100) for i in range(5)]
B = [random.randint(1, 100) for il in range(5)]

# список для наших чисел
Yuumi = []

# для нахождения чисел с макс значением
for max_num in range(len(A)):
    max_value = max(A[max_num], B[max_num])
    Yuumi.append(max_value)

# результат!!
print(Yuumi)
