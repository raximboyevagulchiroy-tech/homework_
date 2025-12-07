# 1
import json

data = {
    "model": "malibu",
    "rang": "qora",
    "yil": 2020,
    "narx": 40000
}
json_data = json.dumps(data)
print(json_data)

# 2
talaba_json = {
    "ism": "Hasan",
    "familiya": "Husanov",
    "tyil": 2000
}

print(talaba_json["ism"], talaba_json["familiya"])

# 3
data = {
    "model": "malibu",
    "rang": "qora",
    "yil": 2020,
    "narx": 40000
}

talaba_json = {
    "ism": "Hasan",
    "familiya": "Husanov",
    "tyil": 2000
}

with open('data.json', 'w') as f:
    json.dump(data, f)

with open('talaba_json.json', 'w') as f:
    json.dump(talaba_json, f)

# 4
talaba = {"student": [{"id": "01", "name": "Tom", "lastname": "Price", "year": 4, "faculty": "Engineering"}, {"id": "02", "name": "Nick", "lastname": "Thameson", "year": 3, "faculty": "Computer Science"}, {"id": "03", "name": "John", "lastname": "Doe", "year": 2, "faculty": "ICT"}]}
for student in talaba["student"]:
    print("Ism: " , student["name"])
    print("Familiya: " , student["lastname"])
    print("Fakultet: " , student["faculty"])
