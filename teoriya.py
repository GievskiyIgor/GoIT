# # a = 2
# # b = 2
# # print (a+b)
# # a **= a
# # print(a)
# # c = b*a
# # print(c)

# # Python - интерпретируемый Interpreted
# # Python - динамический Dinamic
# # Python - модульный  Modular
# # Python  - Высокий уровеньHigh Level
# # Python - Экономически эффективныq Cost effective

# # Вычисление площади комнаты и запись ответа
# # length = 2.75
# # width = 1.75
# # area = length * width
# # show = f"With width {width} and length {length} of the room, its area is equal to {area}"
# # print(show)

# # Комплексные числа
# # complex = 3.14 + 1j
# # print(complex)
# # print(complex.real)  # 3.14 действительная часть числа
# # print(complex.imag)  # 1.0  мнимую часть чисел

# # сложение чисел с мнимой частью
# # a= -2 + 3j
# # b= 4 +2.1j
# # result = a + b
# # print (result)

# # math - модуль работы с числами
# # cmath -  щдуль работы с комплесными числами
# # Щоб додати модуль до своєї програми, необхідно виконати імпорт цього модуля за допомогою ключового слова import
# # Наприклад, щоб знайти квадратний корінь із числа, треба використати метод sqrt модуля math
# import math

# # a = -2
# # b = 7
# # c = -6

# # D = b**2 - 4 * a * c  # Дискриминант этого уравнения
# # x1 = (-b + D**0.5)/(2 * a)  # корень уравнения 1
# # x2 = (-b - D**0.5)/(2 * a)  # корень уравнения 1
# # kku = a * x1**2 + b * x2 + c  # корень квадратного уравнения
# # kku_math = math.sqrt(a * x1**2 + b * x2 + c)  # корень квадратного уравнения
# # print(D)
# # print(x1)
# # print(x2)
# # print(kku)
# # print(kku_math)

# # Програмісти часто працюють із геоданими. Попрацюємо і ми з ними. Нам необхідно написати програму, в якій ми розрахуємо відстань між двома точками на поверхні Землі.
# # Рахуватимемо відстань між двома містами: Києвом та Лондоном
# # Координати Києва в градусах:
# # Широта lat1 = 50.45
# # Довгота lon1 = 30.523

# # Координати Лондона в градусах:
# # Широта lat2 = 51.5072
# # Довгота lon2 = -0.1275
# # Радіус Землі приймемо 6371.01 км. Відстань у кілометрах між містами з урахуванням викривленості планети можна знайти за такою формулою:

# # distance = 6371.01 · arccos(sin(lat1) · sin(lat2) + cos(lat1) · cos(lat2) · cos(lon1 - lon2))

# # Пам'ятайте, що тригонометричні функції в Python оперують радіанами. Тобто величини із градусів необхідно перекласти у радіани, перш ніж обчислювати відстань між точками. Для цього в модулі math є функція radians

# # <радіани > = math.radians( < градуси > )
# # Також:

# # arccos(x) — це math.acos(x)
# # sin(x) — це math.sin(x)
# # cos(x) — це math.cos(x)
# # Обчисліть distance за вказаною формулою за допомогою запропонованих методів модуля math.
# RADIUS = 6371.01

# lat1 = math.radians(50.45)
# lon1 = math.radians(30.523)

# lat2 = math.radians(51.5072)
# lon2 = math.radians(-0.1275)

# distance = RADIUS * math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2))
# print ('Расстояние от Киева до Лондона = ', distance, 'км.')

# a = input('Введите число')
# a = int(a)
# if a > 0: # выполняетьс все это условие
#     print('Число положительное')
# elif a == 1:
#     print('Число равно 1')
# else:
#     print("a <= 0")

# 08.01.2023
# break - завершение итерации
# continue - попуск итерации если выполнелось условие
# Операторы continue и break работают только внутри одного цикла. В ситуации вложенных циклов нет способа выйти из всех циклов сразу.

# a= 0
# while True:
#     print (a)
#     if a >= 15:
#         break # break - завершение итерации так как выполнелось условие в бесконечном цикле
#     a = a + 1
# ***

# echo скрипт, который выводит в консоль то, что вы введете, пока вы не введете exit:

# while True:
#     uesr_input = input('Vvedite chiclo ')
#     if uesr_input == 'exit':
#         break
#     print (uesr_input)
# ***

# Бесконечный цикл, при условии, что введенно exit или пользователь ввел в поле цифру 0
# while True:
#     user_namber = input ('Vvedite chislo ')
#     if user_namber == 'exit':
#         break
#     user_number = int(user_namber)
#     if user_number == 0:
#         break
#     else:
#         while True:
#             print(user_number)
#             if user_number <= 0:
#                 break
#             user_number = user_number - 1
#  ***

# Механизм обработки исключений
#  тело для анписания
# 1 - try, начало блока
# 2 - except, условие выполнение при возникновении ошибки
# 3 - esle, не обязательный блок. Выполняеться если условие ошибки не подтвердилось
# 4- finally, не обязательный блок, Выполнится в любом случае, вне зависимости от того, были ошибки или нет.

# aa = input ('Введите число ')
# try:
#    aa = int(aa)
# except ValueError:
#     print ('Число aa введенно не коректно')
# else:
#     print(aa > 1)
# finally:
#     print("This will be printed anyway")
#  ***

# Основные типы исключений в Python
# SyntaxError — синтаксическая ошибка.
# IndentationError — ошибка, которая возникает, если в выделении блоков инструкций пробелами допущена ошибка.
# TabError возникает, если в одном файле использовать пробелы и табуляции для выделения блоков инструкций.

# TypeError возникает, когда операция с переменной этого типа невозможна.
# 2 / 'a'

# ValueError возникает, когда тип операнда подходящий, но значение таковое, что операцию невозможно выполнить.
# int("a")

# ZeroDivisionError — деление на ноль.

#  Что выдает код

# for i in range(9):
#     if i == True:
#         print (i)
#  Результат выдает 1. Так как при сравнении машина True = 1, 1 == 1 -  условие выполнелось
# ***

# a = set('hello')
# print(a)    # {'e', 'h', 'l', 'o'}

# def summ (n):

#     n += 5 + n*2
#     print(n)

# n = 2
# summ(n)


# def even_or_odd(number):

#     if number % 2 == 0:
#         print('Even')
#     else:
#         print('Odd')

# number1 = int(input('Введите число от 0 до 100: '))
# even_or_odd(number1)

# import re

