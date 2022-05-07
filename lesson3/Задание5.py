counter = 1

numbers_list = [int(x) for x in input("Введите несколько чисел через пробел").split()]
print(sum(numbers_list))

while counter == 1:
    new_list = [int(x) for x in input("Введите новые числа").split()]
    result = sum(numbers_list) + sum(new_list)
    print(result)
# for i in numbers_list:
#     i = str('&')
#     break
#     print("Программа завершена")
#не разобралась, как ввести спецсимвол, если список в числовом формате
