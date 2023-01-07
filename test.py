# a = 2
# b = 2
# print (a+b)
# a **= a
# print(a)
# c = b*a
# print(c)

# Python - интерпретируемый Interpreted
# Python - динамический Dinamic
# Python - модульный  Modular
# Python  - Высокий уровеньHigh Level
# Python - Экономически эффективныq Cost effective

# Вычисление площади комнаты и запись ответа
# length = 2.75
# width = 1.75
# area = length * width
# show = f"With width {width} and length {length} of the room, its area is equal to {area}"
# print(show)

# Комплексные числа
# complex = 3.14 + 1j
# print(complex)
# print(complex.real)  # 3.14 действительная часть числа
# print(complex.imag)  # 1.0  мнимую часть чисел

# сложение чисел с мнимой частью
# a= -2 + 3j
# b= 4 +2.1j
# result = a + b
# print (result)

# math - модуль работы с числами
# cmath -  щдуль работы с комплесными числами
# Щоб додати модуль до своєї програми, необхідно виконати імпорт цього модуля за допомогою ключового слова import 
# Наприклад, щоб знайти квадратний корінь із числа, треба використати метод sqrt модуля math
import math

# a = -2
# b = 7
# c = -6

# D = b**2 - 4 * a * c  # Дискриминант этого уравнения
# x1 = (-b + D**0.5)/(2 * a)  # корень уравнения 1
# x2 = (-b - D**0.5)/(2 * a)  # корень уравнения 1
# kku = a * x1**2 + b * x2 + c  # корень квадратного уравнения
# kku_math = math.sqrt(a * x1**2 + b * x2 + c)  # корень квадратного уравнения
# print(D)
# print(x1)
# print(x2)
# print(kku)
# print(kku_math)

# Програмісти часто працюють із геоданими. Попрацюємо і ми з ними. Нам необхідно написати програму, в якій ми розрахуємо відстань між двома точками на поверхні Землі.
# Рахуватимемо відстань між двома містами: Києвом та Лондоном
# Координати Києва в градусах:
# Широта lat1 = 50.45
# Довгота lon1 = 30.523

# Координати Лондона в градусах:
# Широта lat2 = 51.5072
# Довгота lon2 = -0.1275
# Радіус Землі приймемо 6371.01 км. Відстань у кілометрах між містами з урахуванням викривленості планети можна знайти за такою формулою:

# distance = 6371.01 · arccos(sin(lat1) · sin(lat2) + cos(lat1) · cos(lat2) · cos(lon1 - lon2))

# Пам'ятайте, що тригонометричні функції в Python оперують радіанами. Тобто величини із градусів необхідно перекласти у радіани, перш ніж обчислювати відстань між точками. Для цього в модулі math є функція radians

# <радіани > = math.radians( < градуси > )
# Також:

# arccos(x) — це math.acos(x)
# sin(x) — це math.sin(x)
# cos(x) — це math.cos(x)
# Обчисліть distance за вказаною формулою за допомогою запропонованих методів модуля math.
RADIUS = 6371.01

lat1 = math.radians(50.45)
lon1 = math.radians(30.523)

lat2 = math.radians(51.5072)
lon2 = math.radians(-0.1275)

distance = RADIUS * math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2))
print ('Расстояние от Киева до Лондона = ', distance, 'км.')
