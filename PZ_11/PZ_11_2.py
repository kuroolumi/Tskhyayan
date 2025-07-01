with open('text.txt', 'r', encoding='utf-16') as f:
    content = f.read()
    lines = content.split('\n')

punctuation = "—,!:…"
punctuation_count = sum(1 for char in content if char in punctuation)

print("Содержимое файла:")
print(content)
print(f"\nКоличество знаков препинания: {punctuation_count}")

with open('reversed_poem.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(reversed(lines)))

print("Файл reversed_poem.txt создан с обратным порядком строк.")
