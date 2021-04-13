a = 1

def F3():
    def F():
        global a  # a是最外層的全域性變數
        print("In F3's F, a =", a)

    a = 3
    F()

def F4():
    global a

    def F():
        a = 2  # a是F的區域性變數
        print("In F4's F,a_in=", a)

    F()
    print("In F4, a_go =", a)  # a是全域性變數

def F5():
    def F():  # a不是F的區域性變數，那就繼承上層函式中a的屬性
        print("In F5's F,a =", a)

    a = 3
    F()

F4()

