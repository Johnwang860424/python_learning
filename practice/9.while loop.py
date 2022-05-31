# 所有的 for 迴圈都可以用while迴圈改寫；反之則不一定
# for 迴圈就像田徑、游泳比賽；while迴圈就像桌球、網球比賽

n = 1
while n < 11:
    print(n)
    n += 1

# 引用random模組 (寫法一)
import random

nums = [10, 20, 30, 40, 50]

# 可從串列中隨機挑選一筆資料
n = random.choice(nums)

print(n)

# 從random模組引用choice函數 (寫法二)
from random import choice

nums = [10, 20, 30, 40, 50]

n = choice(nums)

print(n)

# 隨機投擲硬幣的遊戲
# 不斷隨機投擲硬幣直到第三個正面出現後才停止
coin = ["正面", "反面"]
# 紀錄每次投擲結果
result = []
# 當result 裡的"正面" 少於3個, 迴圈就繼續
while result.count("正面") < 3:
    # 從coin裡隨機挑選一個結果
    c = choice(coin)
    # 把結果加到(紀錄)result裡
    result.append(c)

print(result)
print(f"總共丟了{len(result)}次才出現三次正面")

# s = 1+2+3+4+...+n
# 直到總和s大於1000程式才停止
s = 0
n = 1

result = []
# 當 s <= 1000,迴圈繼續
while s <= 1000:
    result.append(n)
    s += n
    n += 1

print(s)
print(result[-1])
print(result)

# 產生出10個Fibonacci sequence
fibonacci = [0, 1]
# 當數列內的資料量少於10,繼續的產生下一個數字並存到數列內
while len(fibonacci) < 10:
    # 算出下一個數字
    n = fibonacci[-2] + fibonacci[-1]
    fibonacci.append(n)

print(fibonacci)

# 產生四個可重複的隨機數
# 參考數列
nums = list(range(10))
result = []
# 當數列裡的數字少於4個,迴圈繼續
while len(result) < 4:
    n = (choice(nums))
    result.append(n)

print(result)

# 產生四個不重複的隨機數 (method1)
nums = list(range(10))
result = []
while len(result) < 4:
    n = choice(nums)
    result.append(n)
    # 從nums裡將n移除
    nums.remove(n)

print(nums)
print(result)

# 產生四個不重複的隨機數 (method2)
nums = list(range(10)) 
result = []
while len(result) < 4:
    n = choice(nums)
    if n not in result:
        result.append(n)

print(nums)
print(result)