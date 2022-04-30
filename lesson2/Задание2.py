# не сообразила, как заполнить список через input

new_list = [1, 2, 3, 4, 5, "ghj"]

print(len(new_list))

l = 0

if len(new_list) % 2 == 0:
    new_list[l], new_list[1] = new_list[1], new_list[l]
    new_list[2], new_list[3] = new_list[3], new_list[2]
else:
    new_list[l], new_list[1] = new_list[1], new_list[l]

print(new_list)
