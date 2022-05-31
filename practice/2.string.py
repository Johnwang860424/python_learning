# 字串與多變數的組合方式
name = "Andy"
title = "工程師"
city = "台北市"
intro = "Hi，我叫" + name + "是一個住在" + city + "的" + title + "。"
print(intro)

intro_2 = f"Hi，我叫{name}是一個住在{city}的{title}。"
print(intro_2)

intro_3 = "Hi，我叫{}是一個住在{}的{}".format(name, city, title)
print(intro_3)

# input函數
name = input("請填寫您的名字:")
title = input(f"{name}，您目前是甚麼職業呢")
city = input(f"{name}，您目前居住在哪個城市呢")
intro = f"Hi，我叫{name}是一個住在{city}的{title}。"
print(intro)

# 取得資料的資料型別
a = "Hello World"
print(type(a))
print(type("Hi"))
print(type(20))
print(type(20.5))
print(type(True), type(False))