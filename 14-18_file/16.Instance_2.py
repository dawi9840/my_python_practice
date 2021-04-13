#Point 實體物件的設計、平面座標上的點
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    #定義實體方法
    def show(self):
        print(self.x, self.y)
    def distance(self, targetx, targety):
        return (((self.x - targetx) ** 2) + ((self.y - targety) ** 2)) ** 0.5

p = Point(3, 4)
p.show()  #實體方法 / 函式
result = p.distance(0, 0)   #計算座標3,4 和座標0,0 之間距離
print("distance = ", result)
'''
#FullName 實體物件的設計: 分開紀錄姓、名資料的全名
class file:
    def __init__(self, name):
        self.name = name
        self.file = None #尚未開啟檔案: 初始None
    def open(self):
        self.file = open(self.name, mode = "r", encoding = "utf-8")
    def read(self):
        return self.file.read()
#讀取第一個檔案
f1 = file("data1.txt")
f1.open()
data = f1.read()
print("data1 = ", data)
#讀取第二個檔案
f2 = file("data2.txt")
f2.open()
data2 = f2.read()
print("data2 = ", data2)
