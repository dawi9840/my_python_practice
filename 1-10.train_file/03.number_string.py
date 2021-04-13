'''
#數字運算
x = 4 % 3
y =4 * 2
z = x+y
print("x = ", x)
print("y = ", y)
print("z = ", z)
x+=1
print("x=", x)
'''
#字串運算
#字串會對內部的字元編號(索引)，從0開始算起
s1 = 'Hello1'*3 + " " + "wow"*2
s2 = "Hell\"o2" "ha\nha" 
s3 = """Hello
world"""
print("s1 = ",s1)
print("s2 = ",s2)
print("s3 = ", s3)

s4 = "Hello"
print("s4[2] = ", s4[:4])