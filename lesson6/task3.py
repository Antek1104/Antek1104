# Проверка 3 :
# В пароле есть хотя бы одна большая

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

