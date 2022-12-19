# задание 1
a=int(input())
b=int(input())
c=int(input())
if a > 10 and b > 10 and c > 10:
    print("Yes")
else:
    print("No")

#задание 2
a, b, c = int(input()), int(input()), int(input())
mx = a
if b > mx:
    mx = b
if c > mx:
    mx = c
print(mx)



