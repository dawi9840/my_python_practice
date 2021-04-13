#抓取PTT八卦版的網頁原始碼(HTML)
import urllib.request as req
def getData(url):
    #建立一個Request物件，附加Request Headers的資訊
    request = req.Request(url, headers = {
        "cookie":"over18=1",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    #解析原始碼，取得每篇文章的標題
    import bs4 
    root = bs4.BeautifulSoup(data, "html.parser") #利用BeautifulSoup套件協助解析HTML格式文件
    titles = root.find_all("div", class_="title") #找所有 class = "title" 的div標籤
    for title in titles:
        if title.a != None:                       #如果標題含a標籤 (沒有被刪除)，印出來
            print(title.a.string)
    #抓取上一頁連結
    nextLink = root.find("a", string = "‹ 上頁") #找到內文是‹ 上頁的a標籤
    return nextLink["href"]

#主程序:抓取多個頁面的標題
pageURL = "https://www.ptt.cc/bbs/Gossiping/index.html"
count = 0
while count < 3:
    pageURL = "https://www.ptt.cc" + getData(pageURL)
    count+=1




