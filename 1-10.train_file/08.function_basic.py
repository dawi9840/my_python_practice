'''
#define function
def multiply(n1, n2):
    return n1*n2

#call the function
value = multiply(3,4) + multiply(10,5)
print("value = ", value)
'''
#程式的包裝: 同樣邏輯可重複利用
def calculate(max):
    sum = 0
    for x in range(1, max+1):
            sum = sum+x

    print("sum = ", sum)

calculate(10)
calculate(20)