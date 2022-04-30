my_dict = {"m1": "Зима", "m2": "Весна", "m3": "Лето", "m4": "Осень"}

number = int(input('Введите номер месяца'))

if number in [1 ,2 , 12]:
    print(my_dict.get("m1"))
if number in [3, 4, 5]:
    print(my_dict.get("m2"))
if number in [6, 7, 8]:
    print(my_dict.get("m3"))
if number in [9, 10, 11]:
    print(my_dict.get("m4"))
else:
    print('Error: incorrect number!')
