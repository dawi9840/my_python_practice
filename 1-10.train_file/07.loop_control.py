#break
'''
n = 0
while n<6:
    if n ==3:
        break
    print("loop in n = ", n)
    n+=1
print("final n = ", n)
'''
#continue
'''
n = 0
for x in [0, 1, 2, 3]:
    if x % 2 == 0:   #x是偶數
        continue
    print("loop in x is ", x)
    n+=1
print("final n = ", n)
'''
#else
#1+2+3+....+9+10
'''
sum =0
for n in range(1, 11):
    sum = sum+n
else:
    print("sum = ", sum)
'''
#找平方根
#input 9, can get 3
#input 11, get "not found square root"
n1 = int(input("Please key the number: "))

for i in range(n1):
    if i*i == n1:
        print("square root is ", i)
        break   #用break強制結束迴圈時，不會執行else區塊
else:
    print("not found the square root!")
