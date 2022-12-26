#  Проверка 4:
#  В пароле есть хотя бы одна маленькая буква

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