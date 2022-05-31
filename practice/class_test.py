# class 類別
# 用途為封裝變數or函式->統稱為類別的屬性
# 類別與類別屬性
# https://www.youtube.com/watch?v=uPKgQ3FoVtY&ab_channel=%E5%BD%AD%E5%BD%AD%E7%9A%84%E8%AA%B2%E7%A8%8B(參考資料)
class Baseball:
    player = ["Bryce Harper", "Gary Sanchez"]  # 定義變數

    def read(player):  # 定義函式
        if player in Baseball.player:
            print("good job")
        else:
            print("try again")
# 使用類別
print(Baseball.player)
Baseball.read(player="A-Rod")
Baseball.read("Derek Jeter")


############################################################################################################
# 類別與實體物件、實體屬性
# https://www.youtube.com/watch?v=Lr5N2r1rmtM&ab_channel=%E5%BD%AD%E5%BD%AD%E7%9A%84%E8%AA%B2%E7%A8%8B(參考資料)
class Point:
    # 定義初始化函式
    def __init__(self, x, y):
        self.x = x
        self.y = y
# 建立第一個實體物件，放入變數obj中
p1 = Point(1, 5)
print(p1.x + p1.y)
# 建立第二個實體物件
p2 = Point(2, 8)
print(p2.x, p2.y)


class FullName:
    def __init__(self, first, last):
        self.first = first
        self.last = last
name1 = FullName("Weihan", "Wang")
print(name1.first, name1.last)
name2 = FullName("GG", "DA")
print(name2.first, name2.last)


# 實體方法 ->封裝在實體物件中的函式
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # 定義實體方法
    def show(self):
        print(self.x, self.y)
    def distance(self, targetX, targetY):
        return (((self.x-targetX)**2)+((self.y-targetY)**2))**0.5
p = Point(3, 4)
p.show()  # 呼叫實體方法
result = p.distance(0, 0)  # 計算座標3,4 與0,0之間的距離
print(result)

# File 實體物件的設計:包裝檔案讀取的程式
class File:
    # 初始化函式
    def __init__(self, name):
        # 定義實體屬性
        self.name = name
        self.file = None  # 尚未開啟檔案:初期式None
    # 定義實體方法
    def open(self):
        self.file = open(self.name, mode="r", encoding="utf-8")
    def read(self):
        return self.file.read()
# 讀取第一個檔案
f1 = File("data1.txt")
f1.open()
data = f1.read()
print(data)
# 讀取第二個檔案
f2 = File("data2.txt")
f2.open()
data = f2.read()
print(data)