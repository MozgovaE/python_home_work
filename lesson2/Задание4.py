new_str = str(input('Введите строку из нескольких слов через пробел'))
my_list = new_str.split()

if len(new_str.split()) > 10:
    for ind, el in enumerate(my_list):
        print(el.replace(el, el[0:9]))
else:
    for ind, el in enumerate(my_list):
        print(ind, el)

#не пойму, как сократить слово в списке до 10 символов