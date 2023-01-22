# 2.Если у пароля есть 1 цифра

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