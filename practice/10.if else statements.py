print(10 > 100)

n = 101
if n > 100:
    print(f"n:{n}大於100")
elif n < 100:
    print(f"n:{n}小於100")
else:
    # 上述條件都不符合(都是False)
    print(f"n:{n}等於100")

n = 4
# 計算 n / 2 的餘數
print(n % 2)

ans = []
for n in range(1,101):
    if n % 2 == 0:
        ans.append(n)
print(ans)

# 試著在不用max()、min()與sort()的情況下
# 寫出一個能找出串列中最大與最小數值的方法
nums = [1, 3, 4, 5, 100, -20, 20]
# 預設最小數字是第一個數字
min_n = nums[0]
# 預設最大數字是第一個數字
max_n = nums[0]
for i in nums:
    if min_n > i:
        min_n = i
    if max_n < i:
        max_n = i
print(f"最小值是{min_n}", f"\n最大值是{max_n}")

# 隨機取出 weather_options 中的一個元素
# 取到晴天或多雲印"跑步"，毛毛雨印"去健身房"，否則印"當沙發馬鈴薯"

# 引入random模組的choice函式
from random import choice
weather_options = ["晴天", "多雲", "毛毛雨", "狂風", "暴雨", "下雪", "打雷閃電"]
# 隨機挑選一次天氣
weather = choice(weather_options)
if weather in ["晴天", "多雲"]: #if weather == "晴天" or "多雲" 是判斷多雲是否在weather裡 如果有的話 就會一直是此結果
    print("跑步")
elif weather == "毛毛雨":
    print("去健身房")
else:
    print("當沙發馬鈴薯")

# break 停止迴圈
nums = range(1, 101)
for n in nums:
    if n == 10:
        # 停止迴圈
        break
    # 迴圈僅運行10次
    print(n)

# continue 略過這一圈，並讓迴圈繼續
ans = []
for n in range(1, 11):
    if n % 2 == 0:
        continue
    ans.append(n)
print(ans)

# 將120的因數儲存在ans中並印出 (法一)
x = 120
ans = []
for i in range(1, 121):
    # 如果 x 可被 n 整除
    if x % i == 0:
        # 把 n 加到 ans 內
        ans.append(i)
print(ans)

# 將120的因數儲存在ans中並印出 (法二)
x = 120
ans = []
for i in range(1, 121):
    # 如果 x 無法被 n 整除
    if x % i != 0:
        # 略過這一圈
        continue
    # 把 n 加到 ans 內
    ans.append(i)
print(ans)

# 設計 while 無窮迴圈的中止開關 (法一)
while True:
    a = input("請輸入\"q\"\"quit\"\"離開\"停止程序:").lower()
    if a in ["q", "quit", "離開"]:
        break
print("程序已經停止")

# 設計 while 無窮迴圈的中止開關 (法二)
process = True
while process:
    a = input("請輸入\"q\"\"quit\"\"離開\"停止程序:").lower()
    if a in ["q", "quit", "離開"]:
        process = False
print("程序已經停止")

# 終極密碼(猜數字)
# 由程式自動從1~100挑選一隨機數
# 使用者可透過輸入猜數字
# 使用者才錯則提示(大一點、小一點)
# 遊戲將猜到使用者猜對為止
ans = choice(range(1, 101))
while True:
    n = int(input("請輸入一個正整數"))
    if n > ans:
        print("猜小一點")
    elif n < ans:
        print("猜大一點")
    else:
        print("答對了")
        break
print("程序結束")