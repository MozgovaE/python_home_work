import json

person = {
    "name": "John",
    "age": 40,
    "salaries": [200, 100, 160]
}

with open('person.json', 'w') as file_string:
    json.dump(person, file_string)