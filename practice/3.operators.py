a = 30
b = 10

print(a + b)
print(a - b)
print(a * b)
print(a / b)
# 取得a除以b的商
print(a//b)
# 取得a除以b的餘數
print(a%b)
# 次方
print(b**2)

# int("20") => 20
# float("15.7") => 15.7
# str(20) => 20

# 透過input所取得的值一定是str
age = int(input("請數入您的年齡"))
text = f"今年我是{age}歲，明年我是{age+1}"
print(text)

# +=, -=, *=, /=, %= 賦值運算子
card = 50
# 加值100
# card = card + 100
card += 100
# 消費15
# card = card - 15
card -= 15
print(card)