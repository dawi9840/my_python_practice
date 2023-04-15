a = "123" # 這個123是字串格式
b = 123   # 這個123是數字格式

print(f'a:{a}\n')
print(f'b:{b}\n')

type_a = type(a)
type_b = type(b)

print(f'a:{a}, type:{type_a}\n')
print(f'b:{b}, type:{type_b}\n')

#有順序、可動的列表 List
list_a = [3,4,5, 6, 7, 8]
list_b = ["hello", "normal", "dsasda", "banana"]

print(list_a)
print(list_b)

print(type(list_b)) 


#集合set 
set_a = {345}
set_b = {"hello", "normal"}

print(f'set a : {set_a}')
print(f'set b : {set_b}')
print("--------------------------")
#字典 dictionary
dictionary_a ={
    "key":"value", 
    "apple":"蘋果", 
    "data":"資料"
}
for i in dictionary_a:
    print(f'key: {i}, value: {dictionary_a[i]}\n')
