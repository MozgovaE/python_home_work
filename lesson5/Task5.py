import json

summa = {'numbers': [1, 2, 3]}
with open('Summa.json', 'w') as file_string:
    json.dump(summa, file_string)

with open('Summa.json') as file_stream:
    summa = json.load(file_stream)
    print(sum(summa['numbers']))
