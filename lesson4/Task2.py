"""Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента."""

my_list = [1, 2, 5, 1, 0]
new_list = []

for i in range(len(my_list)-1):
    if my_list[i] < my_list[i+1]:
        new_list.append(my_list[i+1])

print(new_list)