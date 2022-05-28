import os

if os.path.exists('имяфайла.txt'):
    os.remove('имяфайла.txt')
    #если есть файл с таким именем, то удалить его

files = os.listdir() #список файлов в папке
print(files)