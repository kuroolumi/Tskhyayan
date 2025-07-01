import tkinter as tk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()
        
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2 if num2 != 0 else "Error: Division by zero"
        
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Invalid input")

# Создание окна
root = tk.Tk()
root.title("Simple Calculator")

# Поля ввода
tk.Label(root, text="Number 1:").grid(row=0, column=0)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1)

tk.Label(root, text="Number 2:").grid(row=1, column=0)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1)

# Выбор операции
tk.Label(root, text="Operation:").grid(row=2, column=0)
operation_var = tk.StringVar(value="+")
operations = ["+", "-", "*", "/"]
for i, op in enumerate(operations):
    tk.Radiobutton(root, text=op, variable=operation_var, value=op).grid(row=2, column=i+1)

# Кнопка и результат
tk.Button(root, text="Calculate", command=calculate).grid(row=3, columnspan=5)
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, columnspan=5)

root.mainloop()