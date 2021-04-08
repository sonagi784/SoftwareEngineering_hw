print("2016113519 유지훈")

import json

x = {
    "name": "Jihoon",
    "age": 25,
    "attending": True,
    "discharge": True,
    "phones": [
        {"model": "iphone 11 pro", "year": 2019},
        {"model": "galaxy s20", "year": 2020}
    ]
}

print('json.dumps(x)')
print(json.dumps(x))

print('\njson.dumps(x, indent=4)')
print(json.dumps(x, indent=4))

print('\njson.dumps(x, indent=4, separators=(". ", " = "))')
print(json.dumps(x, indent=4, separators=(". ", " = ")))

print('\njson.dumps(x, indent=4, sort_keys=True)')
print(json.dumps(x, indent=4, sort_keys=True))