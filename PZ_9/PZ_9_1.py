#ВАРИАНТ 23

my_dict = {
    'цвет': 'красный',
    'размер': 'большой',
    'вкус': 'сладкий',
    
}

print("словарь:", my_dict)


key_to_find = 'фрукт'
if key_to_find not in my_dict:
    print('ключ не был найден, добавляем')
    # Добавляем ключ, если его нет
    my_dict[key_to_find] = 'яблоко'


print("словарь:", my_dict)