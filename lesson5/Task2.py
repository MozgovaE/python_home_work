my_list = ['Март\n', 'Апрель\n', 'Май\n']
with open("Spring.txt", 'w+') as file_obj:
    file_obj.writelines(my_list)
with open("Spring.txt") as file_obj:
    lines = 0
    letters = 0
    for line in file_obj:
        lines += line.count("\n")
        letters = len(line)-1
        print(f"{letters} - количество букв")
    print(f"Количество строк: {lines}")