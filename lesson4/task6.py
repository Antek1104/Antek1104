#Пользователь вводит с клавиатуры три числа в переменные a, b, c.
#Найдите наибольшее число из них и запишите в переменную max.


a, b, c = int(input('Enter first number: ')), int(input('Enter second number: ')), int(input('Enter third number: '))
max = a
if b > max:
    max = b
if c > max:
    max = c
print(max)