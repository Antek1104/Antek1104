# Проверка 5:
# В пароле есть хотя бы один спец символ (+, -, /, _, % и т.д. P.S. их на самом деле больше)

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