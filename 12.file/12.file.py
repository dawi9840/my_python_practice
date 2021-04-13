#save the file
'''
file = open("data.txt", mode = "w", encoding = "utf-8") #開啟, w寫入模式
file.write("Hello! file\n文字檔案的讀取和儲")             #操作
file.close                                              #關閉

with open("data.txt", mode = "w", encoding = "utf-8") as file:
    file.write("5\n3")
'''
#read the file 讀取檔案
#把檔案中的數字資料，一行一行讀取出來，並計算總合
'''
sum = 0
with open("data.txt", mode = "r", encoding = "utf-8") as file:
   for line in file: #一行一行讀取
       sum = sum + int(line)
print("sum = ", sum)
'''
#使用json格式讀取、複寫檔案
#從檔案中讀取json資料，放入變數data裡面
import json
with open("config.json", mode = "r") as file:
    data = json.load(file)

print("data1  =", data) #data是一個字典資料
#print("name =", data["name"])

data["name"] = "New name" #修改變數中的資料

#把最新的資料覆寫回檔案中
with open("config.json", mode = "w") as file:
    json.dump(data, file)



