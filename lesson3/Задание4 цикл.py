
my_func = lambda x, y: x **y
x = int(input("Введите положительное число Х"))
y = int(input("Введите целое отрицательное число Y"))
i = 1 # текущая степень
result = 1

if x < 0 or y > 0:
    print("Введённое число не соответствует условию")
else:
    while i <= y:
        result *= x
        i += 1

    print(my_func(x, y))


