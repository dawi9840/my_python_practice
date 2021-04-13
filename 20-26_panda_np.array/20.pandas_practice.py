#載入pandas 模組
import pandas as pd
'''
#建立Series，(Series 單維度資料，是一個類似陣列的物件，裡面可包含陣列的資料)
data = pd.Series([20, 10, 14])

#基本Series操作
#print(data)

print("max = ", data.max())
print("median = ", data.median())
data2 = data * 2
print("data2 = ", data2)

data = data == 20
print("data Series: ", data)
'''

#建立DataFrame
data3 = pd.DataFrame({
    "name":["Amy", "John", "Bob"], 
    "salary":[30000, 50000, 40000]
})
#基本DataFrame操作
#print(data3)

#取得特定的欄位
#print(data3["salary"])

#取得特定列
print(data3)
print("-----------------")
print(data3.iloc[0])      #印出第一列


