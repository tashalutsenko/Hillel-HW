import json

spisochok = {100001: 'Zuzia, 4',
             100002: 'Kyzia, 4',
             100003: 'Venya, 6',
             100004: 'Puh, 6',
             100005: 'Liolia, 8',
             }

spisochok1 = {key: f"Name: {str(value.split()[0])} age: {int(value.split()[1])}"
              for key, value in spisochok.items()}

with open('list.json', 'w') as f:
    json.dump(spisochok1, f)

print(spisochok)
print(spisochok1)