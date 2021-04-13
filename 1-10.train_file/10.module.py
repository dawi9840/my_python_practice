#載入內建sys模組冰取得資訊
'''
import sys as s
print(s.platform)
print(s.maxsize)
'''
#建立 geometry模組，載入使用
'''
import geometry
result = geometry.distance(1, 1, 5, 5)
result2 = geometry.slope(1, 2, 5, 6)
print("Distance is ", result)
print("Slope is  ", result2)
'''
#調整搜尋模組的路徑
import sys as s
s.path.append("./modules") #在模組的搜尋路徑列表中[新增路徑]
print(s.path) #印出模組的路徑列表
import geometry
result = geometry.distance(1, 1, 5, 5)
print("Distance is ", result)

