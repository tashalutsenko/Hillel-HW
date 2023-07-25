import json

with open('list.json') as f:
    new_spisochek = json.load(f)


import random


id = list(new_spisochek.keys())
name_age = str({f"{str(value.split()[0])}: {int(value.split()[1])}"
              for value in new_spisochek.values()})
phone = [[random.randint(1, 100000000000) for num in range(1)],
         [random.randint(1, 100000000000) for num in range(1)],
         [random.randint(1, 100000000000) for num in range(1)],
         [random.randint(1, 100000000000) for num in range(1)],
         [random.randint(1, 100000000000) for num in range(1)]]

print(id)
print(name_age)
print(phone)

import csv

with open("task_02.csv", encoding="utf-8", mode="w", newline=None) as file:
    file_csv = csv.writer(file, delimiter=',')
    file_csv.writerow(['ID', 'Name', 'Age', 'Phone'])
    for name, id in enumerate(id):
        data = []
        data.append(id)
        data.append(name_age.split()[0].strip('{'))
        data.append(name_age.split()[1])
        data.append(phone)
        file_csv.writerow(data)
