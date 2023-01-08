# Урок второй

# 1 задание 
# На технічній співбесіді претенденти на посаду одержують оцінку за тест. 
# У наступний тур співбесіди проходять кандидати, які склали тест на 83 бали включно або вище. 
# Реалізуйте оператор контролю виконання так, щоб він привласнив логічній змінній is_next значення True, якщо кількість набраних балів буде більшою або дорівнює 83. 
# В іншому випадку значення змінної дорівнює False.

# is_next = None
# num = int(input("Enter the number of points: "))
# if num >= 83:
#     is_next = True
# else:
#     is_next = False        
    
# # is_next = False if num < 83 else True
# print (is_next)    
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

if is_admin == 'Yes' or is_admin == 'yes' or is_admin == 'Admin' or is_admin == 'admin':
    access = True
    print ('User - Administrator')
else:
    if (is_active == 'Yes' and is_permission == 'Yes') or (is_active == 'yes' and is_permission == 'yes'):
        access = True
        print('User has access')
    else:
        access = False
        print('User has no access')
      
# print (is_active, is_admin, is_permission)
# print(access)
# ***
# 3 задание 
# ***
# 4 задание 
# ***
# 5 задание 
# ***
# 6 задание 
# ***
# 7 задание 
# ***
# 8 задание 
# ***
# 9 задание 
# ***
# 10 задание 
# ***
# 11 задание 
# ***
# 12 задание 
# ***
# 13 задание 
# ***
# 14 задание
# ***
# 15 задание 
# ***
# 16 задание 
# ***