import pandas as pd 
#篩選練習 - Series
'''
data = pd.Series([30, 15, 20])
condition1 = [True, False, True]
condition2 = data>18
print("condition2: ", condition2, sep = "\n")

filteredData1 = data[condition2]
print("filteredData1: ", filteredData1, sep = "\n")
'''

'''
data2 = pd.Series(["你好", "Python", "Pandas"])
condition3 = [False, True, True]
condition4 = data2.str.contains("P")   #如果字串有包含P，就是True，沒有就是False
print("condition4: ", condition4, sep = "\n")

filteredData2 = data2[condition4]
print("condition4: ", condition4, sep = "\n")
'''
#篩選練習 - DataFrame
data3 = pd.DataFrame({
    "name":["Amy", "Bob", "Charles"],
    "salary":[30000, 50000, 40000]
})

print(data3)
condition5 = [False, True, True]
#condition6 = data3["salary"]>=40000
#print("condition6: ", condition6, sep = "\n")

condition7 = data3["name"] == "Amy"
print("condition7: ", condition7, sep = "\n")

filteredData3 = data3[condition7]
print("filteredData3: ", filteredData3, sep = "\n")