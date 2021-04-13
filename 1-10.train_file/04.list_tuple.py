#有序列可變動列表 List
'''
grades = [60, 70, 85, 90, 96]
grades[0] = 69
grades[1:4] = []  #連續刪除
print("grades[:5] = ", grades[:5])
print("grades[1:4] = ", grades[1:4])
print("grades = ", grades)

grades2 = [60, 70, 85, 90, 96]
grades2 = grades2 + [12, 33]
length_grades2 = len(grades2)
print("grades2 = ", grades2)
print("length of grades2 = ", length_grades2)
'''
#巢狀列表
'''
data = [[3, 4, 5], [6, 7, 8]]
print("data[0][0:2] = ", data[0][0:2], "data = ", data)
data[0][0:2] = [5, 5, 5]
print("data[0][0:2] = ", data[0][0:2], "data = ", data)
'''

#有序列不可變動列表 Tuple
data = (3, 4, 5)
#data(0) = 5 #錯誤tuple 的資料型態不能變動
print("data = ", data)

