import pandas as pd 
#資料索引
data = pd.Series([5, 4, -2, 3, 7], index = ["a", "b", "c", "d", "e"])
#觀察資料
'''
print("資料型態: ", data.dtype)
print("資料數量: ", data.size)
print("資料索引: ", data.index)

print(data.dtype)
print("max value: ", data.max())
print("sum value:", data.sum())
print("Standard deviation: ", data.std())
print("median value:", data.median())
print("取最大3個數: ", data.nlargest(3))
print("2 of smallst: ", data.nsmallest(2))

N = len(data)
mean = float(data.mean())
SD = float((((5-mean)**2 + (4-mean)**2 + ((-2)-mean)**2 + (3-mean)**2 + (7-mean)**2 )/N) ** 0.5)
print("SD: ", SD)
'''
#取得資料: 根據順序、根據索引
'''
print(data[2], data[0])
print(data["e"], data["d"])
#數字運算: 基本、統計、順序
'''

data2 = pd.Series(["你好", "Python", "Pandas"])
#字串運算: 基本、串接、搜尋、取代
'''
print(data2.str.lower())            #英文字變小寫
print(data2.str.upper())            #英文字變大寫
print(data2.str.len())              #算每個字串長度
'''
print(data2.str.cat())              #cat()連接, sep是cat()裡面，可自訂串接符號參數
print(data2.str.cat(sep = ", "))
print(data2.str.contains("P"))      #判斷字串是否包含特定的字元
print(data2.str.replace("你好", "Hello")) #取代