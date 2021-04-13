#判斷式
'''
x = input("Please key the number: ") #取得字串形式的使用這輸入
x = int(x) #將字串型態轉換成數字型態
if x > 200:
    print("Your number = ", x, "大於200")
elif 50 < x <= 200:
    print("Your number = ", x, "介於50到200之間")
else:
    print("Your number = ", x, "小於等於50")
'''
#四則運算
n1 = int(input("Please key the number1: "))
n2 = int(input("Please key the number2: "))
op = input("Please choes the operation(+, -, *, /): ")
if op == "+":
    print("number1 + number2 = ", n1+n2)
elif op == "-":
    print("number1 - number2 = ", n1-n2)
elif op == "*":
    print("number1 * number2 = ", n1*n2)
elif op == "/":
    print("number1 / number2 =", n1/n2)
else:
    print("Sorry, we are not suport the operation! :( ")


