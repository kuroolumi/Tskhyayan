# ВАРИАНТ 19 

# Задание 2
def upper_chars(s):
    yield from (c.upper() for c in s)

text = "Hello World"
print(f"Преобразованный текст: {''.join(upper_chars(text))}")