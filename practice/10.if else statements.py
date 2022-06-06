from numpy import min_scalar_type


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