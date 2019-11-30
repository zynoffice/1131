import requests
from lxml import etree

# h = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"}

# html = requests.get("https://www.yicai.com/",headers=h)
# html.encoding  = "utf-8"



def caijing(offset):
    #创建文件夹
    # os.makedirs("./images",exist_ok=True)
    # 获取网页
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
    }
    url = "https://www.yicai.com/"
    # 请求连接
    response = requests.get(url, headers=headers)
    html = etree.HTML(response.content.decode("utf-8"))
    data = {}
    for i in html.xpath("//div[@class='m-number f-cb']//tr[1]"):
        data["title"] = i.xpath("string(.//td[1])")
        data["score"] = i.xpath("string(.//td[2])")
        print(data)
# data1 = html.tostring(data[0])

# data2 = HTMLParser().unescape(tree1.decode('utf-8'))
# print(data2)
        


        
if __name__ == "__main__":
    for i in range(10):
        caijing(i*10)
        time.sleep(1)
