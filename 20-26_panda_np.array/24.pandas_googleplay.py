import pandas as pd
#讀取資料
data = pd.read_csv("googleplaystore.csv")  #把csv格式檔案讀取成一個DataFrame
#觀察資料
print("資料數量: ", data.shape)
print("資料欄位: ", data.columns)
print("-----------------------------")
'''
#分析資料:評分的各種統計數據
condition = data["Rating"]<=5
data = data[condition]
#print("Rating: ", data["Rating"], sep = "\n")
print("Rating平均數: ", data["Rating"].mean())
print("Rating中位數: ", data["Rating"].median())
print("取得前1000個應用程式Rating的平均數: ", data["Rating"].nlargest(1000).mean())
'''
#分析資料:安裝數量的各種統計數據
#print(data["Installs"])
'''
#把原本一堆字串，經過to_numeric轉成數字再覆蓋給data["Installs"]
#replace("A", "B")  把A用B替換掉
data["Installs"] = pd.to_numeric((data["Installs"]).str.replace("[,+]", "").replace("Free", "")) 
print(data["Installs"] )
print("平均數: ", data["Installs"].mean())
condition2 = data["Installs"]>100000
print("安裝數量大於100000的應用程式有幾個: ", data[condition2].shape[0])
'''
#基於資料的應用:關鍵字搜尋應用程式
'''
keyword = input("please key the keyword:  ")
condition3 = data["App"].str.contains(keyword, case = False) #case = Dalse 忽略大小寫
#print(data[condition3])
#print(data[condition3]["App"])  #只展現condition3條件的["App"]名稱
print(data[condition3].shape[0])   #.shape取得數量:(數量, 欄位)
'''




