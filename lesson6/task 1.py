#Программа запрашивает у пользователя пароль и записывает в переменную password.
#Необходимо посчитать сложность пароля, где за каждую пройденную проверку пароль получает +1 балл к итоговой оценке, максимальное количество баллов - 5
#Проверки:
#Длина пароля больше или равно 8 символам
#В пароле есть хотя бы одна цифра
#В пароле есть хотя бы одна большая буква
#В пароле есть хотя бы одна маленькая буква
#В пароле есть хотя бы один спец символ (+, -, /, _, % и т.д. P.S. их на самом деле больше)



#Проверка №1:

password = '123'
if len(password) <= 8:
   print('Skore:2 ')
   print('Recomendation: ')
   print('Use special characters')
   print('The minimum password length is 8')
   print('Use capital letters')
else:
    print('-')
      
#Проверка №2:

password = 'admin123'
has_digit = False

for char in password:
    print(char)
    if char.isdigit():
        has_digit = True
        break


if has_digit:
    print('Skore:3 ')
    print('Recomendation: ')
    print('Use capital letters')
    print('Use special characters')
else:
    print('-')
      
# Проверка 3 :

password = 'adMin123'
has_digit = False

for s in password:
    print('Good')
    if s.isupper():
        has_digit = True
        break

if s.isupper:
    print('Skore:4 ')
    print('Recomendation: ')
    print('Use special characters')
else:
    print('-')

#  Проверка 4:

password = 'adMin123'
has_digit = False

for s in password:
    print('Good')
    if s.islower():
        has_digit = True
        break

if s.islower():
    print('Skore:4 ')
    print('Recomendation: ')
    print('Use special characters')
else:
    print('-')      

# Проверка 5:

password = 'adMin123@#'
has_digit = False

for s in password:
    print('Good')
    if s.punctuation():
        has_digit = True
        break

if s.punctuation():
    print('Skore:5 ')
else:
    print('-')




