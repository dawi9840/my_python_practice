#參數的預設資料
'''
def power(base, exp = 0):
    print("power(",base,",", exp, ") is",  base ** exp)
    return 

power(3, 2)
power(4)
'''
#使用參數名稱對應
'''
def divide(n1, n2):
    print("divide(", n1, ",", n2, ") is", n1/n2)
    return

divide(2, 4)
divide(n2 = 2, n1 = 4)
'''
#無限 / 不定 參數資料
def avg(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    print("avg(", numbers,") = ", sum/len(numbers))

avg(3,4)
avg(3, 5, 10)
avg(4, 4, -1, -8)


