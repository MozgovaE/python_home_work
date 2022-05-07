my_func = lambda x, y: x **y
x = int(input("Введите положительное число Х"))
y = int(input("Введите целое отрицательное число Y"))

if x < 0 or y > 0:
    print("Введённое число не соответствует заданным параметрам")

else:
    print(my_func(x, y))
