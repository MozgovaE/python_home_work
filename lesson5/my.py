my_file = open(r'data.txt', mode="w")

# for line in my_file.readlines():
#     print(line.replace('\n',''))

# for data in my_file.read(1024):
#     print(data)

if my_file.writable():
    my_file.write("Update\n")

    strings = ["John\n", "Kate\n"]
    my_file.writelines(strings)
else:
    print("Can not write")
my_file.close()

#или вот так, где клоус писать не обязательно (менеджер контекста):
# try:
# with open('data.txt') as my_file
#     print(my_file.read())
# print(type(my_file))
# except IOError:
      # print("Some error")

with open('data.txt', 'w') as printable:
    strings = ["John", "Kate"]

    for x in strings:
        print(x, file=printable)