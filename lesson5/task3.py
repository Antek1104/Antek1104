# Вывести треугольник #3 с шириной N с помощью цикла while

N = 5
d = '*'
k = ''
a = 0
print(N*d)
while N != 1:
        N -= 1
        a += 1
        print((k * a)+(N * d))
