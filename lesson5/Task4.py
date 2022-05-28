numbers = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4}
new_file = []
with open('Numbers.txt', 'r') as file_obj:
    for x in file_obj:
        x = x.split()
        new_file.append(numbers[x[0]] + ' - ' + x[1])
    print(new_file)

with open('Numbers_new.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)