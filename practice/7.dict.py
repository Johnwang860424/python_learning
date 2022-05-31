user1 = {
    # key(字串): value(任意型別)
    "name": "Andy",
    "age": 30,
    "phone": "0912-345-678",
    "is_admin": False
}
# 字典["key"] => value
print(user1["name"])
print(user1["age"])
print(user1["phone"])
# 更新字典value
user1["name"] = "Eric"
user1["age"] += 1
user1["email"] = "andy@gmail.com"
print(user1)

user2 = {
    "name": "Kate",
    "age": 24,
    "address": {
        "city": "台北市",
        "district": "大安區",
        "street": "復興南路一段1號",
        "zip": "106"
    } 
}

print(user2["address"]["city"])
print(user2["address"]["district"])

address = user2["address"]
print(address)
print(address["city"])

# 移除字典 name
user2.pop("name")

print(user2)