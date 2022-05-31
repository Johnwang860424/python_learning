# list 表達多筆資料的資料型別
# 清單,串列
from re import I


nums = [1, 5, 3, 10, 12]
print(type(nums))
print(nums)

name_list = ["Andy", "Tony", "Abby", "Josh", "Kate", "Benson"]

# 串列[索引]
name = name_list[-3]
print(name)
# 串列[索引] = 新值
name_list[0] = "Eric"
name_list[-1] = "Ben"
print(name_list)

nums = [99, 1, 2, 3, 4, 5]
# 串列.append(新資料)
nums.append(6)
nums.append(600)
nums.append(1200)
# 串列.insert(索引, 新資料)
nums.insert(0, 100)
print(nums)

# 串列.pop(索引) 移除指定索引的資料 預設最後一筆
nums.pop(0)
# 串列.remove(要移除的資料) 移除一個指定的資料
nums.remove(1200)
print(nums)
# 串列.sort() 由小到大排序資料
nums.sort(reverse=True)
print(nums)
# len(串列) => 串列裡的資料長度
print(f"nums裡有{len(nums)}筆資料")

nums = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
# 把1更新為99
idx = nums.index(1)
print("idx:", idx)
# 串列[索引] = 新資料
nums[idx] = 99
print("nums:", nums)