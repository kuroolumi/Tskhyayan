import sqlite3
from datetime import datetime

# Создание и подключение к базе данных
conn = sqlite3.connect('applicants_PZ_15.db')
cursor = conn.cursor()

# Создание таблицы Анкета
cursor.execute('''
CREATE TABLE IF NOT EXISTS Анкета (
    Регистрационный_номер INTEGER PRIMARY KEY,
    Фамилия TEXT NOT NULL,
    Имя TEXT NOT NULL,
    Отчество TEXT,
    Дата_Рождения TEXT NOT NULL,
    Награды TEXT NOT NULL,
    Адрес TEXT NOT NULL,
    Специальность TEXT NOT NULL
)
''')
conn.commit()

# Функция для ввода данных
def add_applicant():
    try:
        reg_num = int(input("Регистрационный номер: "))
        surname = input("Фамилия: ")
        name = input("Имя: ")
        patronymic = input("Отчество: ")
        birth_date = input("Дата рождения (ГГГГ-ММ-ДД): ")
        awards = input("Награды (да/нет): ")
        address = input("Адрес: ")
        specialty = input("Специальность: ")
        
        cursor.execute('''
        INSERT INTO Анкета VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (reg_num, surname, name, patronymic, birth_date, awards, address, specialty))
        conn.commit()
        print("Данные добавлены успешно!")
    except Exception as e:
        print(f"Ошибка: {e}")

# Функция для поиска данных
def search_applicant():
    try:
        print("\nВарианты поиска:")
        print("1. По фамилии")
        print("2. По специальности")
        print("3. По наличию наград")
        choice = int(input("Выберите вариант поиска: "))
        
        if choice == 1:
            surname = input("Введите фамилию: ")
            cursor.execute("SELECT * FROM Анкета WHERE Фамилия=?", (surname,))
        elif choice == 2:
            specialty = input("Введите специальность: ")
            cursor.execute("SELECT * FROM Анкета WHERE Специальность=?", (specialty,))
        elif choice == 3:
            awards = input("Введите наличие наград (да/нет): ")
            cursor.execute("SELECT * FROM Анкета WHERE Награды=?", (awards,))
        else:
            print("Неверный выбор.")
            return
        
        results = cursor.fetchall()
        if results:
            for row in results:
                print(row)
        else:
            print("Данные не найдены.")
    except Exception as e:
        print(f"Ошибка: {e}")

# Функция для удаления данных
def delete_applicant():
    try:
        print("\nВарианты удаления:")
        print("1. По регистрационному номеру")
        print("2. По фамилии")
        print("3. По специальности")
        choice = int(input("Выберите вариант удаления: "))
        
        if choice == 1:
            reg_num = int(input("Введите регистрационный номер: "))
            cursor.execute("DELETE FROM Анкета WHERE Регистрационный_номер=?", (reg_num,))
        elif choice == 2:
            surname = input("Введите фамилию: ")
            cursor.execute("DELETE FROM Анкета WHERE Фамилия=?", (surname,))
        elif choice == 3:
            specialty = input("Введите специальность: ")
            cursor.execute("DELETE FROM Анкета WHERE Специальность=?", (specialty,))
        else:
            print("Неверный выбор.")
            return
        
        conn.commit()
        print("Данные удалены успешно!")
    except Exception as e:
        print(f"Ошибка: {e}")

# Функция для редактирования данных
def edit_applicant():
    try:
        reg_num = int(input("Введите регистрационный номер для редактирования: "))
        
        print("\nЧто вы хотите изменить?")
        print("1. Фамилию")
        print("2. Адрес")
        print("3. Специальность")
        choice = int(input("Выберите поле для редактирования: "))
        
        if choice == 1:
            new_surname = input("Введите новую фамилию: ")
            cursor.execute("UPDATE Анкета SET Фамилия=? WHERE Регистрационный_номер=?", (new_surname, reg_num))
        elif choice == 2:
            new_address = input("Введите новый адрес: ")
            cursor.execute("UPDATE Анкета SET Адрес=? WHERE Регистрационный_номер=?", (new_address, reg_num))
        elif choice == 3:
            new_specialty = input("Введите новую специальность: ")
            cursor.execute("UPDATE Анкета SET Специальность=? WHERE Регистрационный_номер=?", (new_specialty, reg_num))
        else:
            print("Неверный выбор.")
            return
        
        conn.commit()
        print("Данные обновлены успешно!")
    except Exception as e:
        print(f"Ошибка: {e}")

# Основное меню
def main():
    while True:
        print("\nМеню:")
        print("1. Добавить абитуриента")
        print("2. Поиск абитуриента")
        print("3. Удалить абитуриента")
        print("4. Редактировать абитуриента")
        print("5. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            add_applicant()
        elif choice == '2':
            search_applicant()
        elif choice == '3':
            delete_applicant()
        elif choice == '4':
            edit_applicant()
        elif choice == '5':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
    conn.close()