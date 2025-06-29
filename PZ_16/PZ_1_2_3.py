import pickle

#ВАРИАНТ 7

class Matrix:
    """Класс для работы с матрицами (сложение, вычитание, умножение)."""
    
    def __init__(self, rows, cols, data=None):
        """Инициализация матрицы с указанным количеством строк и столбцов."""
        self.rows = rows
        self.cols = cols
        self.data = data or [[0 for _ in range(cols)] for _ in range(rows)]
    
    def __add__(self, other):
        """Сложение двух матриц."""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны быть одного размера")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result
    
    def __sub__(self, other):
        """Вычитание двух матриц."""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны быть одного размера")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] - other.data[i][j]
        return result
    
    def __mul__(self, other):
        """Умножение матриц или матрицы на число."""
        if isinstance(other, (int, float)):
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result.data[i][j] = self.data[i][j] * other
            return result
        elif isinstance(other, Matrix):
            if self.cols != other.rows:
                raise ValueError("Количество столбцов первой матрицы должно равняться количеству строк второй")
            result = Matrix(self.rows, other.cols)
            for i in range(self.rows):
                for k in range(other.cols):
                    for j in range(self.cols):
                        result.data[i][k] += self.data[i][j] * other.data[j][k]
            return result
        else:
            raise TypeError("Неподдерживаемый тип операнда")
    
    def __str__(self):
        """Строковое представление матрицы."""
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

# Тестирование
m1 = Matrix(2, 2, [[1, 2], [3, 4]])
m2 = Matrix(2, 2, [[5, 6], [7, 8]])

print("Матрица 1:")
print(m1)
print("\nМатрица 2:")
print(m2)
print("\nСложение:")
print(m1 + m2)
print("\nВычитание:")
print(m1 - m2)
print("\nУмножение матриц:")
print(m1 * m2)
print("\nУмножение на число:")
print(m1 * 2)

# ВАРИАНТ 3

class Automobile:
    """Базовый класс для автомобилей."""
    
    def __init__(self, brand, model, year):
        """Инициализация автомобиля с маркой, моделью и годом выпуска."""
        self.brand = brand
        self.model = model
        self.year = year
    
    def __str__(self):
        """Строковое представление автомобиля."""
        return f"{self.brand} {self.model} ({self.year})"

class Truck(Automobile):
    """Класс грузовика, наследуется от Automobile."""
    
    def __init__(self, brand, model, year, load_capacity):
        """Инициализация грузовика с грузоподъемностью."""
        super().__init__(brand, model, year)
        self.load_capacity = load_capacity
    
    def __str__(self):
        """Строковое представление грузовика."""
        return f"{super().__str__()}, Грузоподъемность: {self.load_capacity} кг"

class PassengerCar(Automobile):
    """Класс легкового автомобиля, наследуется от Automobile."""
    
    def __init__(self, brand, model, year, passenger_count):
        """Инициализация легкового автомобиля с количеством пассажиров."""
        super().__init__(brand, model, year)
        self.passenger_count = passenger_count
    
    def __str__(self):
        """Строковое представление легкового автомобиля."""
        return f"{super().__str__()}, Пассажиров: {self.passenger_count}"

# Тестирование
car1 = Automobile("Toyota", "Camry", 2020)
truck1 = Truck("Volvo", "FH16", 2019, 20000)
passenger_car1 = PassengerCar("Honda", "Civic", 2021, 5)

print(car1)
print(truck1)
print(passenger_car1)