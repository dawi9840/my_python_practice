#Point 實體物件的設計、平面座標上的點
'''
class Point:
    def __init__(self, x, y):  #__init__ 定義初始化函數，操作self來定義實體物件屬性  
        self.x=x
        self.y=y
#建立第一個實體物件
p1= Point(3, 4)
print("(p1.x, p1.y) = ", p1.x, p1.y)
#建立第一個實體物件
p2 = Point(7, 8)
print("(p2.x, p2.y) = ", p2.x, p2.y)
'''
#FullName 實體物件的設計: 分開紀錄姓、名資料的全名
class FullName:
    def __init__(self, first, last):
        self.first = first
        self.last = last
name1 = FullName("Deng You", "Lyu")
name2 = FullName("A.K", "Lin")

print("Full name is ", name1.first, name1.first)
print("Second full name is", name2.first, name2.last)

