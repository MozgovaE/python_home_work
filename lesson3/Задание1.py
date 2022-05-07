def delenie(number_1, number_2):
    try:
        return number_1 / number_2
    except ZeroDivisionError:
        return


number_1 = int(input("Введите делимое:"))
number_2 = int(input("Введите делитель:"))

print("Результат деления = ", delenie(number_1, number_2))

