# Вариант 25
# С начала суток прошло N секунд (N — целое). Найти количество полных часов, прошедших с начала суток.

try:
    N = int(input('Введите количество секунд, прошедших с начала суток: ')) # сюда вписывается число
    if N < 0:
        print('Ошибка! Количество секунд не может быть отрицательным!')
    else:
        print('wait a few seconds')
        M = int(N // 3600)  # переводит секунды в часы
        print("Целых часов прошло с начала суток:", M)  # выводит результат

except ValueError:
    print('Ошибка! Введено не число')

