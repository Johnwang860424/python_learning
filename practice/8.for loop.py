character_list = ["Walter White", "Skyler White", "Jesse Pinkman", "Hank Schrader", "Saul Goodman"]

# 迭代子
# for 迭代子 in 一批資料:
for character in character_list:
    print(character)

# 預設n是1
n = 1
for character in character_list:
    print(f"第{n}位角色是{character}")
    n += 1

print(f"角色清單共有{len(character_list)}個人")


nums = [10, 20, 30, 40, 50]
# 預設x是0
x = 0

for n in nums:
    x += n

print(f"nums的總和是{x}")


cart = [
    {
        "name": "產品A",
        "price": 30,
        "quantity": 2
    },
    {
        "name": "產品B",
        "price": 40,
        "quantity": 4
    },
    {
        "name": "產品C",
        "price": 50,
        "quantity": 3
    },
    {
        "name": "產品D",
        "price": 100,
        "quantity": 5
    }
]

cart_value = 0

for item in cart:
    # 一個商品總金額 = 單價 * 數量
    item_value = item["price"] * item["quantity"]
    cart_value += item_value

print(f"購物車內共有{len(cart)}個品項,總金額是{cart_value}元")


item_map = {
    "產品A": 30,
    "產品B": 40,
    "產品C": 50
}

for name in item_map:
    # print(name)
    # print(item_map[name])
    price = item_map[name]
    print(f"產品名稱:{name} 價格:{price}")

for a in "Hello World":
    print(a)

# range(起始值, 結尾值(不包含在產生的數列內))
nums = range(10)
# 轉換成list型別
nums = list(nums)

print(nums)

start = int(input("請輸入開始值:"))
end = int(input("請輸入結尾值:"))
summation = 0
for n in range(start, end+1):
    # print(n)
    summation += n

print(f"{start}加到{end}的總和是{summation}")

nums = range(1, 9+1)

for x in nums:
    for y in nums:
        if x < y:
            print("\n")
            break
        else:
            print(f"{x} x {y} = {x * y}", end="  ")