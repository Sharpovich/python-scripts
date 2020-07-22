import csv
import json

# format CSV
with open("example.csv") as f:
    reader=csv.reader(f)
    for row in reader:
        print(row)

with open("example2.tsv") as f:
    reader=csv.reader(f, delimiter="\t")
    for row in reader:
        print(row)

students=[
    ["Sharpov","Tim", 70,80,90],
    ["Adis","Noa", 90,100,15]
]
with open("example.csv", "a") as f:
    writer=csv.writer(f)
    writer.writerows(students)

# format JSON
student1={
    'firts_name':'Greg',
    'last_name': 'Dean',
    'scores': [70,80,90],
    'description': "Good job, Greg",
    'certificate': True
}

student2={
    'firts_name': "Tim",
    'last_name': "Sharpov",
    'scores': [80,80.2,80],
    'description': "Nicely Done",
    'certificate': True
}

data=[student1,student2]
# чтение происходит через dumps
print(json.dumps(data,indent=4, sort_keys=True))

# запись в файл происходит через dump
with open("students.json", "w") as f:
    json.dump(data, f, indent=4, sort_keys=True)
    
# считываение данных формата json через load
with open("students.json", "r") as f:
    data_again=json.load(f)
    print(sum(data_again[1]["scores"]))
