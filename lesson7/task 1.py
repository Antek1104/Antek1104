# задание 1.
# Запросить у пользователя 5 чисел и записать их в список:

my_list = []
for num in range(5):
    x = int(input('Введите число: '))
    my_list.append(x)
print(my_list)

#Задание№2 :
#Дан список A = [1, 2, 3, 4, 5]
#Удалить последнее число из списка:

my_list = [1,2,3,4,5]
my_list.remove(5)
print(my_list)

#Задание 3:
#Запросить у пользователя 10 чисел и записать их в список A
#Запросить у пользователя число N
#Вывести пользователю сколько в списке A повторяется число N

my_list = []
for num in range(10):
    x = int(input('Введите число: '))
    my_list.append(x)
print(my_list)

n = int(input('Введите число: '))
numbers = [1,2,3,1,4,5,1]
print(numbers.count(1))

#Задание 4:
#Запросить у пользователя число N
#Запросить у пользователя N чисел и записать их в список A
#Вывести список в обратной последовательности

my_list = []
for num in range(5):
    x = int(input('Введите число: '))
    my_list.append(x)
    x = [1, 2, 3, 4, 5]
    my_list = x[::-1]

print(x)
print(my_list)

#Задание 5:
#Запросить у пользователя 5 чисел и записать их в список A
#Записать все числа из списка A которые больше 5 в список C

my_list = []
for num in range(7):
    x = int(input('Введите число: '))
    my_list.append(x)
def greater  (x):
    return x > 5

my_list = [1, 2, 3, 4, 5, 6, 7]
filteredList = list(filter(greater, my_list))
print(filteredList)

#Задание 6:
#Запросить у пользователя число N
#Запросить у пользователя N целых чисел и записать их в список A
#Найти в нем минимальное и максимальное число с помощью цикла
#(запрещено использовать функцию min, max, sorted, sort). Вывести эти числа.

my_list = []
for num in range(5):
    x = int(input('Введите число: '))
    my_list.append(x)

list = [1,2,3,4,5]

mins = list[0]
for i, x in enumerate(list, 1):
    if x < mins:
        mins = x

print(my_list)
print(mins)

#Задание 7:
#Пользователь вводит текст нужно вывести количество цифр в этом тексте

a = input('Введите строку: ')
print(a)
print('Форматированый текст: ',a.upper())
num = [int(i) for i in a if i.isdigit()]
print('Количество цифр в тексте:', len(num))
new = a.split()
for i in new:
    if i.isdigit():
        new.remove(i[-1])
for i in new:
    print(i, end=' ')
