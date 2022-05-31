from operator import xor


print(5 + 5 > 9)
print(5 + 5 < 9)

a = 3
b = 7
# a + b 等於 10 嗎?
print(a + b == 10)
# a + b 不等於 10 嗎?
print(a + b != 10)

# and 且
print(True and True)
print(False and True)
print(True and False)
print(False and False)
x = 5
# 是否在10~20之間
print(x < 10 and x < 20)

# or 或
print(True or True)
print(True or False)
print(False or True)
print(False or False)
x = 14
# 判斷x是否不在10~20之間
print(x > 10 or x < 20)

# not 否/反轉
print(not True)
print(not False)

# 布林值與條件判斷
x = True
if x:
    print("如果條件為正向")

score = 70
if score >= 60:
    print(f"我考了{score}分，及格了!")
else:
    # 如果上述條件不是True
    print(f"我考了{score}分，不及格!")

score = 99
gpa = ""
if score >= 90:
    gpa = "A+"
elif score >= 80:
    gpa = "A"
elif score >= 70:
    gpa = "B"
elif score >= 60:
    gpa = "C"
else:
    gpa = "F"
print(f"我考了{score}分，{gpa}")

x = 4
# 取 x 除以 2 的餘數
if x % 2 == 0:
    print(f"{x}是偶數")
else:
    print(f"{x}是奇數")