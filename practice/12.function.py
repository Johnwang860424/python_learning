# 設計一個可以計算矩形面積的函數 rect()
# 函數預設需要提供矩形的寬度(width)跟高度(height)作為輸入值
# 輸出的資料是矩形的面積

from numpy import append


def rect(length, width):
    area = length * width
    # 將area作為此函數的輸出並結束函數
    # 任何寫在return後的流程都不具意義
    return area

# [使用]rect函數
x = rect(40, 30)
print("x:", x)

# 設計一個可以計算個股損益的函數
# calc_profit(股數shares, 成本價cost, 現價current_price)
# 損益值 = ( 現價 - 成本價 ) * 股數
def calc_profit(shares, cost, current_price):
    return (current_price - cost) * shares

# 案例A
# 小明在過去使用成本價100, 買了A公司2000股
# 現在A公司股價漲至120
# 損益值 = (120 - 100) * 2000
# 40000
a = calc_profit(2000, 100, 120)

# 案例B
# 小明在過去使用成本價100, 買了B公司2000股
# 現在B公司股價跌至50
# 損益值 = (50 - 100) * 2000
# -100000
b = calc_profit(2000, 100, 50)
print(a, b)

# 設計一個可把英吋單位轉換為公分的函數 inch_converter
# x = inch_converter(1)
# print(x) # 2.54
def inch_converter(inch, unit = "cm"):
    # 1英吋等於2.54公分
    cm = inch * 2.54
    mm = cm * 10
    if unit == "cm":
        return cm
    elif unit == "mm":
        return mm
x = inch_converter(1)
print(x)
y = inch_converter(1, "mm")
print(y)

# 設計一個可以判斷輸入的正整數是否為質數的函數 (法一)
# is_prime(6) => False
# is_prime(7) => True
# is_prime(8) => False
# is_prime(11) => True
# 任意挑一個數字 不是質數的機率較高
# 質數檢查法n => [2,3,4,5,6...n-1] => 如果數列內的數字[全部]都無法n整除 => n 就為質數
def is_prime(n):
    # 預設n是質數
    ans = True
    for x in range(2, n):
        # 如果n可以被x整除
        if n % x == 0:
            # n就非質數
            ans = False
            break
    return ans
print(is_prime(2003))

# 設計一個可以判斷輸入的正整數是否為質數的函數 (法二)
def is_prime2(n):
    for x in range(2, n):
        if n % x == 0:
            return False
    return True
x = is_prime2(6)
print(x)

# lambda 匿名函數 一行就可以處理完的函數
# 不需要return
rect = lambda width, height: width * height
x = rect(30, 40)
print(x)

circle = lambda r: r * r * 3.14
y = circle(5)
print(y)

# map函數：把串列裡的資料統一處裡
# map(函數程序, 原始資料)
nums = [1, 2, 3, 4, 5]
x = map(lambda n: n ** 2, nums)
print(list(x))

# map邏輯之重現
def copy_map(method, nums):
    ans = []
    for n in nums:
        ans.append(method(n))
    return ans
x = copy_map(lambda n: n ** 2, [1, 2, 3, 4, 5])
print(x)

# filter函數：從串列裡過濾指定資料
# filter(函數程序, 原始資料)
x = filter(lambda n: n % 2 == 0, [1, 2, 3, 4, 5, 6])
x = list(x)
print(x)

#  filter邏輯之重現
def copy_filter(method, nums):
    ans = []
    for n in nums:
        if method(n):
            ans.append(n)
    return ans
x = copy_filter(lambda n: n % 2 == 0, [1, 2, 3, 4, 5, 6])
print(x)