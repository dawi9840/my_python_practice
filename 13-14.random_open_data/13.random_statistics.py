#隨機模組
'''
import random as r
#隨機選取
data1 = r.choice([1, 5, 6, 10, 20])
data2 = r.sample([1, 5, 6, 10, 20], 3)

data3 = [1, 5, 6, 10, 20]
r.shuffle(data3)    #隨機調換data3資料

print("data1 = ", data1)
print("data2 = ", data2)
print("data3 = ", data3)

#隨機取得亂數
data4 = r.random()            #random()取0~1之間的隨機亂數
data5 = r.uniform(0.0, 1.0)   #uniform()取0.0~1.0之間的隨機亂數
data6 = r.uniform(70, 100)    #uniform()取70~100之間的隨機亂數

print("data4 = ", data4)
print("data5 = ", data5)
print("data6 = ", data6)

#取得常態分配亂數
#normalvariate(平均數, 標準差)
data7 = r.normalvariate(100, 10) #平均數100, 標準差10, 得到的資料"多數"在90 ~ 100之間 
data8 = r.normalvariate(0, 5)    #平均數0,   標準差5,  得到的資料"多數"在-5 ~ 5之間 

print("data7 = ", data7) 
print("data8 = ", data8)
'''
#統計模組
import statistics as s
data9 = s.mean([1, 2, 3, 7, 8, 12, 55, 66, 200])     #取得列表平均數
data10 = s.median([1, 2, 3, 7, 66, 12, 55, 8, 200])  #取得列表中位數
data10 = s.stdev([1, 2, 3, 7, 66, 12, 55, 8, 200])   #取得列表標準差
data11 = s.stdev([1, 2, 3, 7, 66, 12, 55, 8, 10]) 

print("mean = ", data9)
print("median = ", data10)
print("Standard Deviation data10= ", data10)
print("Standard Deviation data11= ", data11)

#key word: 平均數、中位數、標準差、常態分配(高斯分布)