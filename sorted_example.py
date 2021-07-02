# To sorted example.

a = [5,7,6,3,4,1,2]

# 保留原列表
b = sorted(a)       

# print("a:", a)
# print("b:", b)

L=[('b',2),('ff',1),('c',3),('d',4)]
# print(type(L))

key_sort = sorted(L, key=lambda x:x[0])               

print("L:", L)
print("cmp_sort:", key_sort)


# 透過.items()先將資料型態轉成可迭代的對象後，在這裡可迭代的對象會轉成元組(tuple)，資料會以小括號(var_1,var_2,...)儲存。
d = {"zza":123, "b":456, "c":23005}
d_sort = sorted(d.items(), key=lambda b:b[0])

# print(d)
print(d_sort)