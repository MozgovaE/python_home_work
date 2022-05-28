firm = {'Иванов': 11370, 'Петров': 21500, 'Зайцев': 19340, 'Волков': 21450}
try:
    file_obj = open("Salaries.txt", 'w')
    for last_name, salary in firm.items():
        file_obj.write(last_name + ':' + str(salary) + "\n")
except IOError:
    print("Некорректные данные")
finally:
    file_obj.close()

with open("Salaries.txt", "r") as file_obj:
    for line in file_obj:
        a = 0
        x = line.split(':')
        if int(x[1]) <= 20000:
            print(x)
        else: a = a + 1

