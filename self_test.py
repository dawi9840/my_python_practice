class Test1:
    def prt1(self):
        print(self)
        print(self.__class__)
 
t = Test1()
t.prt1()

class Test:
    def prt(asd):
        print(asd)
        print(asd.__class__)
 
t = Test()
t.prt() #self 不是 python 關鍵字，我們把他換成 asd 也是可以正常執行