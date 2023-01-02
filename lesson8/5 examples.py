#Выписать 5 типов ошибок, описания и примеров их воспроизведения.

# Example 1:

#TypeError - Возникает, когда функция или операция применяется к объекту неправильного типа,
#Example :

names_set = set()
names_set.add("Anthony")
names_set.add("Iryna")
names_set2 = {"Anna","Oliviia"}
names_set3 = names_set + names_set2
for name in names_set:
    print(name)

#Example 2:

#ZeroDivisionError - Возникает, когда второй операнд деления или операции по модулю равен нулю.
#Example :

a = 2
b = 0
print(a / b)

#Example 3:

#ValueError - Возникает, когда функция получает аргумент правильного типа, но неправильное значение.
#Example:

chr(-97)

#Example 4:

#KeyError - Возникает, когда ключ не найден в словаре.
#Example:

countries_and_capitals = {'Poland': 'Warsaw', 'Chechia': 'Prague', 'Germany': 'Berlin'}
print(countries_and_capitals['USA'])

#example 5:

#NameError Возникает, когда переменная не найдена в локальной или глобальной области.
#Example:

my_list[1,2,3,4,5]
print(my_list)


