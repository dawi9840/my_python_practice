import sys
'''
try:
    mm = 9 / 10
    print(mm)
except:
    # sys.exc_info()[0] 就是用來取出except的錯誤訊息的方法
    print("Unexpected error:", sys.exc_info()[0])
#-----------------------------------------------------------------#
#raise 錯誤類型(“錯誤訊息”)
try:
    raise NameError("This is Name Error!")
except NameError:
    print("We got Name Error!")
    raise
#-----------------------------------------------------------------#'''
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("不能除以零！")
    else:
        print("相除結果是:", result)
    finally:
        print("不論如何都會執行finally")
 
print("2 / 1: ")
divide(2, 1)
print("========================")
print("2 / 0: ")
divide(2, 0)

'''
def display_name(name):
    names = ["Apple", "John", "Merry"]
    if name not in names:
        raise ValueError("name dose not exit.")
    print(name)

try:
    display_name("John")
    display_name("PPAP")
except ValueError as error:
    print(error)

#  as 關鍵字，另取別名

'''


