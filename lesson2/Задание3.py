m = int(input('Введите номер месяца'))

if m in [12, 1, 2]:
    print('winter')
if m in [3, 4, 5]:
    print('spring')
if m in [6, 7, 8]:
    print('summer')
if m in [9, 10, 11]:
    print('autumn')
elif m > 12 or m < 1:
    print('incorrect number!')
