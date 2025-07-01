import re

def count_works(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    # Паттерн для поиска произведений (в кавычках или после двоеточия)
    pattern = r'«([^»]+)»|произведения:\s*([^\n]+)'
    works = re.findall(pattern, content)

    # Обработка найденных произведений
    total_works = 0
    for work in works:
        # Объединяем оба варианта (кавычки и двоеточие)
        work_str = work[0] if work[0] else work[1]
        # Разделяем произведения, если их несколько в одной строке
        works_list = [w.strip() for w in re.split(r',| и |\.', work_str) if w.strip()]
        total_works += len(works_list)

    return total_works

# Подсчет произведений
filename = 'writer.txt'
total = count_works(filename)
print(f"Общее количество произведений: {total}")
