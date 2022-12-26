# Проверка 5:
# В пароле есть хотя бы один спец символ (+, -, /, _, % и т.д. P.S. их на самом деле больше)

password = 'adMin123\t'
has_digit = False

for s in password:
    print('Good')
    if s.isspace():
        has_digit = True
        break

if s.isspace():
    print('Skore:5 ')
else:
    print('-')