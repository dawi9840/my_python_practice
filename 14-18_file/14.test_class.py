#定義類別、與類別屬性(封裝在類別中的變數和函式)
#定義一個類別IO、有兩個屬性supportedSrcs和read
class IO:
    supportedSrcs=["console", "file"]
    def read(src):
        if src not in IO.supportedSrcs:
            print("not supported")
        else:
            print("Read from:", src)


#使用類別
print(IO.supportedSrcs)
IO.read("file")
IO.read("Internet")

