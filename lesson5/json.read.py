import json

with open('person.json') as file_string:
    person = json.load(file_string)

    print(sum(person['salaries']))

#print(json.loads('{"name": "John", "age": 40, "salaries": [100, 200, 160]}'))