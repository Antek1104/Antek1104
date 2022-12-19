#Пользователь вводит с клавиатуры три числа в переменные a, b, c.
#Найдите наибольшее число из них и запишите в переменную max.


a, b, c = int(input()), int(input()), int(input())
mx = a
if b > mx:
    mx = b
if c > mx:
    mx = c
print(mx)

