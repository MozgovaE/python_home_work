my_list = [7, 5, 3, 3, 2]
n = int(input("Введите новый элемент рейтинга - целое число"))
e = 0

if n < my_list[-1]:
    my_list.append(n)
    print('Обновлённый рейтинг:', my_list)
elif n > my_list[0]:
    my_list.insert(0, n)
    print('Обновлённый рейтинг:', my_list)

while n != my_list[e]:
    e = e + 1
    my_list.insert(e, n)
    print('Обновлённый рейтинг:', my_list)
