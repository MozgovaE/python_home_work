my_func = lambda x, y: x + y

a = int(input("первое число:"))
b = int(input("второе число:"))
c = int(input("третье число:"))

if a > b and b > c:
    x = a
    y = b
if a > b and c > b:
    x = a
    y = c
if b > a and c > a:
    x = b
    y = c
if a == b or a == c or b == c:
    print("Error: similar numbers")

print(my_func(x, y))
