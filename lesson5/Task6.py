import json
subj = {"Информатика": [100, 50, 20], "Физика": [30, 10, 0], "Физкультура": [30, 0, 0]}

with open('Subjects.txt', 'w') as file_string:
    json.dump(subj, file_string)

with open('Subjects.txt', 'r') as file_string:
        subj = json.load(file_string)

        a = (sum(subj['Информатика']))
        b = (sum(subj['Физика']))
        c = (sum(subj['Физкультура']))

        print("Общее количество часов по информатике:", a)
        print("Общее количество часов по физике:", b)
        print("Общее количество часов по физкультуре:", c)


