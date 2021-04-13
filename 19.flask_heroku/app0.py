from flask import Flask
app1 =  Flask(__name__)         #__name__代表目前執行的模組

@app1.route("/")                #函式的裝飾(Decorator)，以函式為基礎，提供附加功能
def home():
    return "Hello Flask 2 dadada 123158w4wd2a1d3a21d"

@app1.route("/test")            #代表要處理的路徑        
def test():
    return "This is test"

if __name__ == "__main__":     #如果以主程式執行
    app1.run()                  #立刻啟動伺服器

