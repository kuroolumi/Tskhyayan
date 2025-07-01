import tkinter as tk
from tkinter import ttk

def register():
    # Здесь можно добавить логику обработки данных формы
    print("Регистрация завершена!")

# Создание основного окна
root = tk.Tk()
root.title("EVENT REGISTRATION FORM")
root.geometry("400x500")

# Стиль для меток
label_style = {'font': ('Arial', 10), 'anchor': 'w', 'pady': 5}

# Поля для имени
tk.Label(root, text="Name", **label_style).grid(row=0, column=0, sticky='w')
tk.Label(root, text="First Name", **label_style).grid(row=1, column=0, sticky='w')
first_name_entry = tk.Entry(root)
first_name_entry.grid(row=1, column=1, sticky='ew', padx=5, pady=2)

tk.Label(root, text="Last Name", **label_style).grid(row=2, column=0, sticky='w')
last_name_entry = tk.Entry(root)
last_name_entry.grid(row=2, column=1, sticky='ew', padx=5, pady=2)

# Поле для компании
tk.Label(root, text="Company", **label_style).grid(row=3, column=0, sticky='w')
company_entry = tk.Entry(root)
company_entry.grid(row=3, column=1, sticky='ew', padx=5, pady=2)

# Поле для email
tk.Label(root, text="Email", **label_style).grid(row=4, column=0, sticky='w')
email_entry = tk.Entry(root)
email_entry.grid(row=4, column=1, sticky='ew', padx=5, pady=2)

# Поля для телефона
tk.Label(root, text="Phone", **label_style).grid(row=5, column=0, sticky='w')
tk.Label(root, text="Area Code", **label_style).grid(row=6, column=0, sticky='w')
area_code_entry = tk.Entry(root, width=10)
area_code_entry.grid(row=6, column=1, sticky='w', padx=5, pady=2)

tk.Label(root, text="Phone Number", **label_style).grid(row=7, column=0, sticky='w')
phone_number_entry = tk.Entry(root)
phone_number_entry.grid(row=7, column=1, sticky='ew', padx=5, pady=2)

# Выбор темы
tk.Label(root, text="Subject", **label_style).grid(row=8, column=0, sticky='w')
subject_var = tk.StringVar()
subject_combobox = ttk.Combobox(root, textvariable=subject_var, state='readonly')
subject_combobox['values'] = ('Choose option', 'Option 1', 'Option 2', 'Option 3')
subject_combobox.current(0)
subject_combobox.grid(row=8, column=1, sticky='ew', padx=5, pady=2)

# Радиокнопки для существующего клиента
tk.Label(root, text="Are you an existing customer?", **label_style).grid(row=9, column=0, sticky='w')
customer_var = tk.StringVar(value='No')
tk.Radiobutton(root, text="Yes", variable=customer_var, value="Yes").grid(row=9, column=1, sticky='w')
tk.Radiobutton(root, text="No", variable=customer_var, value="No").grid(row=10, column=1, sticky='w')

# Кнопка регистрации
register_button = tk.Button(root, text="REGISTER", command=register, bg='blue', fg='white')
register_button.grid(row=11, column=0, columnspan=2, pady=20, sticky='ew', padx=50)

# Настройка сетки
root.columnconfigure(1, weight=1)

root.mainloop()