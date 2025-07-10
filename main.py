
import json

with open ("data.json",'r') as file:
    data = json.load(file)
    data.append({
        "name" : "Petar petrovic",
        "age" : 22,
        "height" : 190,
        "gender" : "male"
    })

print(data)

with open("data.json", 'w') as file:
    json.dump(data, file, indent = 4)