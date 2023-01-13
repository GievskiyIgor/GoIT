# Урок второй

# 1 задание 
# На технічній співбесіді претенденти на посаду одержують оцінку за тест. 
# У наступний тур співбесіди проходять кандидати, які склали тест на 83 бали включно або вище. 
# Реалізуйте оператор контролю виконання так, щоб він привласнив логічній змінній is_next значення True, якщо кількість набраних балів буде більшою або дорівнює 83. 
# В іншому випадку значення змінної дорівнює False.

is_next = None
num = int(input("Enter the number of points: "))
# if num >= 83:
#     is_next = True
# else:
#     is_next = False        
    
is_next = False if num < 83 else True
print (is_next)    
# ***

# 2 задание
# У нас є три логічні змінні.

# Перша визначає статус користувача is_active, яка дорівнює True або False.
# Друга is_admin визначає, чи є у користувача права адміністратора теж булевого типу.
# Третя is_permission — чи дозволено доступ, теж булевого типу.
# Приведіть змінні is_active, is_admin та is_permission до булевого вигляду.

# Надайте змінній access, значення, яке покаже, чи є доступ у користувача. Використовуйте логічні оператори.
# Адміністратор завжди має доступ, незалежно від значень змінних is_permission та is_active.
# Користувач має доступ, тільки якщо is_permission дорівнює True та is_active також дорівнює True
is_active = input("Is the user active? ")
is_admin = input("Is the user administrator? ")
is_permission = input("Does the user have access? ")

# if is_admin == 'Yes' or is_admin == 'yes' or is_admin == 'Admin' or is_admin == 'admin':
#     access = True
#     print ('User - Administrator')
# else:
#     if (is_active == 'Yes' and is_permission == 'Yes') or (is_active == 'yes' and is_permission == 'yes'):
#         access = True
#         print('User has access')
#     else:
#         access = False
#         print('User has no access')
        
# if is_admin == 'True' or is_admin == 'true':
#     access = True
#     print('User - Administrator')
# else:
#     if is_active == 'True' and is_permission == 'True':
#         access = True
#         print('User has access')
#     else:
#         access = False
#         print('User has no access')

is_admin =True if is_admin == 'True' or is_admin == 'true' else False
is_active = True if is_active == 'True' or is_active == 'true' else False
is_permission = True if is_permission == 'True' or is_permission == 'true' else False

if is_admin:
    access = True
    print('User - Administrator')
else:
    if is_active and is_permission:
        access = True
        print('User has access')
    else:
        access = False
        print('User has no access')
    
print (is_active, is_admin, is_permission)
print(access)
# ***

# 3 задание 
# Як відомо, зазвичай розробників заведено поділяти на три категорії: Джун(Junior) & mdash
# молодший спеціаліст, Мідл(Middle) — основний розробник у компанії та Сеньйор(Senior) — старший розробник. 
# Орієнтовно можна вважати, що до 1 року роботи включно — це Джуніор, понад 5 років — це Сеньйор розробник, а від одного року до 5 включно — мідл.
# Є змінна work_experience, що визначає стаж роботи програміста. Залежно від стажу роботи, присвоїти змінній developer_type значення "Junior", "Middle" або "Senior". 
# Використовуйте, якщо необхідно, булеві оператори or та and під час перевірок.

work_experience = int(input("Enter your full work experience in years: "))
print (work_experience)
print(type(work_experience))
if work_experience > 1 and work_experience <= 5:
    developer_type = "Middle"
elif work_experience <= 1 :
    developer_type = "Junior"
else :
    developer_type = "Senior"
print (developer_type)    
# ***

# 4 задание 
# Перепишіть приклад із теорії, але для додатного числа перевіряйте — парне воно чи ні. Таким чином після перевірок змінна result повинна містити одне з чотирьох значень:

# "Positive even number"
# "Positive odd number"
# "Negative number"
# "It is zero"
# Підказка: перевірка на парність виконується порівнянням залишку від поділу на 2 з 0 або 1. Нагадаємо, залишок від ділення можна отримати після операції %
num = int(input("Введіть число: "))

if num > 0:
    num1 = num%2
    if num1 == 0:
        result = "Positive even number"
    else:
        result = "Positive odd number"
elif num < 0:
    result = "Negative number"
else:
    result = "It is zero"

print(result)
# ***

# 5 задание 
# Повернемося до завдання розрахунку коренів квадратного рівняння з попереднього модуля.
# Необхідно обчислити коріння квадратного рівняння.

# a · x2 + b · x + c = 0

# Дискримінант рівняння помістіть у змінну D

# D = b2 - 4 · a · c

# Коріння рівняння помістіть у змінні x1 та x2

# x1 = (-b + D0.5) / (2 · a)
# x2 = (-b - D0.5) / (2 · a)

# Минулого разу ми просто вказали значення коефіцієнтів a, b, c. Тепер, коли ми вже знаємо про розгалуження, ми можемо перевіряти значення дискримінанта і,
# в залежності від того додатне чи від'ємне, провести розрахунок коренів. Виконайте розрахунок коренів для довільних значень коефіцієнтів a, b, c.
# import math

# a = int(input("Enter coefficient a: "))
# b = int(input("Enter coefficient b: "))
# c = int(input("Enter coefficient c: "))

# D = b ** 2 - 4 * a * c
print (D)
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
# else:
#     print ('Дискриминант отрицательный, необходимо првести к положительному числу')
#     D=D * -1
#     x1 = (-b + math.sqrt(D)) / (2 * a)
#     x2 = (-b - math.sqrt(D)) / (2 * a)
    
print (x1, x2)
# ***

# 6 задание 
# Виконайте завдання, щоб визначити парне число чи ні, за допомогою тернарного оператора.
# Програма встановлює значення змінної is_even у True або False, залежно від того, чи є число в змінній num парним або непарним.
# Підказка: перевірка на парність виконується порівнянням залишку від поділу на 2 з 0 або 1. Нагадаємо, залишок від ділення можна отримати після операції %
num = int(input("Enter an integer number: "))

is_even = True if num%2 == 0 else False

print (is_even) 
# ***

# 7 задание 
# Користувач вводить число від 0 до 100. Підрахуйте, використовуючи цикл while, суму всіх чисел від першого до введеного числа включно в num. Результат помістити в змінну sum.

# Тести будуть:
# Поміщати тестові значення для змінної num: 20, 10, 5, 100
# І чекати суми в змінній sum: 210, 55, 15, 5050

num = int(input("Enter the integer (0 to 100): "))
sum = 0

while num >= 0:
    sum = sum + num
    num = num - 1 
print (sum)
# ***

# 8 задание 
# Рядок — це об'єкт, що ітерується, а, значить, ми можемо використовувати його в циклі for . 
# Підрахуйте в заданому рядку message кількість входжень символу зі змінної search. Результат помістіть у змінну result.

message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
search = "r"
result = 0
for r_search in message:
    if search  == r_search:
        result = result + 1
print (result)    
# ***

# 9 задание 
# На співбесідах часто люблять запитувати про алгоритми. Наприклад, розрахуйте найбільший спільний дільник(НД) двох додатних чисел. НСД — це найбільше число,
# яке без залишку діляться на обидва числа.

# Є кілька алгоритмів знаходження НСД, але ми розберемо циклічний алгоритм

# Хай є два початкових числа first та second.
# Виберемо менше з них та привласнимо значення змінній gcd.
# Поки first або second не діляться на gcd без залишку, треба виконувати цикл, в якому зменшуємо змінну gcd на одиницю.
# Коли цикл закінчиться в змінній gcd буде НСД для чисел first та second
# Напишіть програму, яка для двох додатних цілих чисел знаходить НСД.

# Примітка: Для умови циклу в пункті 3 необхідно пам'ятати, що цикл while виконується за умови True, а наш цикл повинен закінчитися, тільки якщо gcd поділив обидва числа без залишку.

first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))

if first >= second:
    gcd = second
    print(gcd)
else:
    gcd = first  
    print(gcd)
    
while True:
    # if gcd > 0:
        if (first % gcd) == 0 and (second % gcd) == 0:
            print (gcd)
            break
        elif gcd == 0:
            break
        else:
            gcd -= 1
# ***

# 10 задание 
# Напишіть два цикли, вкладені один в один. У першому циклі while ми постійно запитуємо ціле число, а у другому з допомогою циклу for складаємо суму чисел 
# від 0 до введеного числа включно і додаємо до змінної sum. Змінна sum накопичує суми, що утворюються при кожному введенні числа. Вихід з першого циклу здійснюємо, 
# якщо ми ввели число 0.

# Тести використовують дві тестові послідовності чисел:
# 10, 13, 73, 0 і чекають на суму 2847
# 1, 2, 3, 4, 0 і чекають на суму 20

num = int(input("Enter integer (0 for output): "))
sum = 0
while num != 0:
    
    for ci in range(1,num + 1):
        sum += ci 
        # num -= 1
    print(sum)
    num = int(input("Enter integer (0 for output): "))
# ***

# 11 задание 
num = int(input("Enter integer (0 for output): "))
sum = 0
while True:
    if num ==0:
        break
    for ci in range(1, num + 1):
        sum += ci
        # num -= 1
    print(sum)
    num = int(input("Enter integer (0 for output): "))
# ***

# 12 задание 
sum = 0
while True:
    num = int(input("Enter integer (0 for output): "))
    if num == 0:
        break
    for i in range(num + 1):
        if i%2 == 1:
            continue
        sum = sum + i
    print (sum)
# ***

# 13 задание 
#  КОД ЦЕЗАРЯ

# Досить часто програмісти стикаються із завданнями кодування інформації. Закодувати повідомлення в чаті між двома користувачами. 
# Зашифрувати пароль та ім'я користувача при автентифікації користувача через мережу і т.і.

# Напишіть програму, що реалізує код Цезаря. Він названий на честь великого римського імператора Юлія Цезаря.

# Ідея шифрування полягає у циклічному зміщенні букв на задану кількість. Наприклад, якщо зміщення на три позиції, то літера A стає літерою D, B – E тощо. 
# Останні три літери алфавіту зациклюються та переносяться на початок. Літера X стає A, Y – B, а Z – C. Цифри, пробіли та інші символи не шифруються.

# У програмі користувач вводить фразу та число для зсуву, після чого треба вирахувати нове закодоване повідомлення.

# Програма шифруватиме як малі(a-z), так і великі літери(A-Z).

# Для розв'язку цього завдання знадобиться знання двох нових функцій. Перша функція ord. Вона перетворює символ на число, яке є позицією в таблиці ASCII.

# ord("a")  # 97
# Можна вважати, що отриманий результат '97' — це числове представлення символу a для комп'ютера.

# Зворотна функція chr повертає рядковий символ у таблиці ASCII за позицією, переданою як аргумент.

# chr(118)  # 'v'
# Детальніший принцип шифрування.

# Розглянемо для прикладу як зашифрувати символ v. Щоб отримати позицію символу v щодо початкового символу a, необхідно виконати вираз

# pos = ord('v') - ord('a')  # 21
# Але, згідно з алгоритмом, нам необхідно враховувати зсув, який може бути довільним, наприклад, 33. 
# І пам'ятати, що алфавіт англійської мови заснований на латинському алфавіті та складається з 26 літер. 
# Тому кінцева позиція символу v щодо символу a для шифрування з урахуванням цього — дорівнює 2.

# pos = ord('v') - ord('a')  # 21
# pos = (pos + 33) % 26  # 2
# Залишився останній крок, отримати новий символ:

# pos = ord('v') - ord('a')  # 21
# pos = (pos + 33) % 26  # 2
# new_char = chr(pos + ord("a"))  # 'c'
# Символ v зі зміщенням 33 шифрується символом c.

# Тести перевіряють та кодують наступні рядки:

# "Hello my little friends!", offset = 37,
# "Hello world!", offset = 7

# 1 вариант 
message = input("Введите сообщение: ")
offset = int(input("Введите сдвиг: ")) 
encoded_message = ""

pos_alfavit_r = ord('A')
pos_alfavit_n = ord('a')

for ch in message:
    
    registr_str = str.isupper(ch)
    pos_ch = ord(ch)
    
    if (pos_ch >= 65 and pos_ch <= 90) or (pos_ch >= 97 and pos_ch <= 122):
        
        if registr_str == True:
        
            pos = pos_ch - pos_alfavit_r
            pos = (pos + offset) % 26
            pos_promegytok = pos + pos_alfavit_r
            
            if pos_promegytok > 90:
                new_char = chr(ord('A') + (pos_promegytok-90)-1)
            else:
                new_char = chr(pos + pos_alfavit_r)
            
            if pos_alfavit_r <= 90:
                pos_alfavit_r += 1
            else:
                pos_alfavit_r = ord('A')
                
        else:
            pos = pos_ch - pos_alfavit_n
            pos = (pos + offset) % 26
            pos_promegytok =  pos + pos_alfavit_n
            
            if pos_promegytok > 122:
                new_char = chr(ord('a') + (pos_promegytok-122)-1) 
            else:
                new_char = chr(pos + pos_alfavit_n)    
            
            if pos_alfavit_n <= 122:
                pos_alfavit_n += 1
            else:
                pos_alfavit_n = ord('a')
            
    else:
        new_char = ch  
        
    encoded_message += new_char
    
print (encoded_message)

# 2 вариант
message = input("Введите сообщение: ")
offset = int(input("Введите сдвиг: "))
encoded_message = ""

pos_alfavit_r = ord('A')
pos_alfavit_n = ord('a')

for ch in message:

    registr_str = str.isupper(ch)
    pos_ch = ord(ch)

    if ch.istitle() or ch.islower():

        if registr_str:  # проверка на верхний регистр
            pos = pos_ch - pos_alfavit_r
            pos_alfavit = pos_alfavit_r
            pos_alfavit_r += 1 if pos_alfavit_r <= 90 else ord('A')
        else:  # нижний регистр
            pos = pos_ch - pos_alfavit_n
            pos_alfavit = pos_alfavit_n
            pos_alfavit_n += 1 if pos_alfavit_n <= 122 else ord('a')

        pos = (pos + offset) % 26
        pos_promegytok = pos + pos_alfavit

        if pos_promegytok > 90 and pos_promegytok < 97:  # закончились заглавные буквы, начались символы,'А'
            new_char = chr(ord('A') + (pos_promegytok-90)-1)
        elif pos_promegytok > 122: # закончились прописные буквы, начались символы, 'а'
            new_char = chr(ord('a') + (pos_promegytok-122)-1)
        else:
            new_char = chr(pos + pos_alfavit)
    else:
        new_char = ch

    encoded_message += new_char

print(encoded_message)

# ***

# 14 задание
# Ситуація проста, вам необхідно вирахувати кількість SMS, які треба надсилати в одному пакеті розсилки потенційним покупцям. 
# Всього на день виділяється 1000 платних SMS для кампанії маркетингу pool = 1000. Співробітник відділу маркетингу вводить кількість розсилок quantity, 
# і ви обчислюєте розмір пакета chunk = pool // quantity. Опрацюйте помилку поділу на нуль.
pool = 1000
quantity = int(input("Enter the number of mailings: "))
try:
    chunk = pool // quantity
except ZeroDivisionError:
    print('Divide by zero completed!')
# ***

# 15 задание 
# Напишіть програму, яка буде виконувати найпростіші математичні операції з числами послідовно, приймаючи від користувача операнди(числа) та оператор.

# Умови для цієї задачі

# Додаток працює з цілими та дійсними числами.
# Додаток вміє виконувати такі математичні операції:
# ДОДАВАННЯ(+)
# ВІДНІМАННЯ(-)
# МНОЖЕННЯ(*)
# ДІЛЕННЯ(/)
# Програма приймає один операнд або один оператор за один цикл запит-відповідь.
# Всі операції програма виконує в порядку надходження — одну за одною.
# Програма виводить результат обчислень, коли отримує від користувача символ = .
# Додаток закінчує роботу після того, як виведе результат обчислення.
# Користувач по черзі вводить числа та оператори.
# Якщо користувач вводить оператор двічі поспіль, він отримує повідомлення про помилку і може ввести повторно.
# Якщо користувач вводить число двічі поспіль, він отримує повідомлення про помилку і може ввести повторно.
# Додаток коректно опрацьовує ситуацію некоректного введення(exception).
# Початкові змінні:

# result = None
# operand = None
# operator = None
# wait_for_number = True
# result — сюди поміщаємо підсумковий результат operand — завжди зберігає поточне число operator — рядковий параметр, може містити чотири значення,
# "+", "-", "*", "/" wait_for_number — прапорець, який вказує, що очікують на вводі оператор(operator) або операнд(operand)

# Приклад виконання програми:

# >> > 3
# >> > +
# >> > 3
# >> > 2
# 2 is not '+' or '-' or '/' or '*'. Try again
# >> > -
# >> > -
# '-' is not a number. Try again.
# >> > 5
# >> > *
# >> > 3
# >> > =
# Result: 3.0
# Тестові послідовності:

# Перша: ["10", "+", "5", "6", "/", "3", "-", "a", "2", "*", "6", "= "], результат 18.0
# Друга: ["2", "3", "-", "1", "+", "10", "*", "2", "="], результат 22.0
result = None # підсумковий результат
operand = None # поточне число
operator = None # рядковий параметр, може містити чотири значення, "+", "-", "*", "/"
wait_for_number = True #  флаг 

while True:
    # if operand == '=' or operator == '=':
    #     print(result)
    #     break
    # else:
        if wait_for_number == True:
            
            try:
                operand = input('Input operand - ')
                if not operand == '=':
                    operator_next = int(operand)
                    # wait_for_number = False
                else:
                   print(result)
                   break     
            except ValueError:
                print(f'Input {operand} is not a number. Try again')
                # wait_for_number = False       
                operand = input('Input operand - ')
                operator_next = int(operand)
            
            #  Вычисление Уравнения
            if not operator == None:
                if ord(operator) == 42:  # * - умножение
                    result = operand_tek * operator_next
                elif ord(operator) == 43:  # + сложение
                    result = operand_tek + operator_next
                elif ord(operator) == 45:  # - - вычитание
                    result = operand_tek - operator_next
                elif ord(operator) == 47:  # / - Деление
                    try:
                        result = operand_tek / operator_next
                    except ZeroDivisionError:
                        print(f'Input {operand}, you cannot divide by zero. Input number!!! Try again')
                        operand = input('Input operand - ')
                        result = operand_tek / int(operand)
            
            wait_for_number = False
        else:
            operator = input('Input operator - ')
            if not operator == '=':
                if ord(operator) == 42 or ord(operator) == 43 or ord(operator) == 45 or ord(operator) == 47:
                    wait_for_number = True
                else:
                    print(f'Input {operator} is not ''+'' or ''-'' or ''/'' or ''*''. Try again')
                    wait_for_number = False
            else:
                print(result)
                break
                
        if result == None:
            operand_tek = operator_next
        else:
            operand_tek = result    
# ***
