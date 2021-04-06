phonedict= {
    "brand": "Apple",
    "model": "iphone 12",
    "year": 2020
}

print("phonedict dictionary : ", phonedict)

phonedict["color"] = "red"
print("Add new element -> ", phonedict)

x = phonedict.get("model")
print('get("model") -> ', x)

x = phonedict.keys()
print("keys method -> ", x)

x = phonedict.values()
print("values method -> ", x)

x = phonedict.items()
print("items method -> ", x)