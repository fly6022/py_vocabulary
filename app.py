import requests as req
import urllib

def app():

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) appleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}; # header
    word = input();
    
    def Kirisame_Req(url, headers):
        req = urllib.request.Request(url, headers = headers); # 伪造客户端请求服务器
        response = urllib.request.urlopen(req);
        html = eval(response.read().decode('utf-8','ignore').replace(u'\xa9', u''))
        return html
        
    html = Kirisame_Req("https://dict.youdao.com/suggest?num=5&ver=3.0&doctype=json&cache=false&le=en&q=" + word, headers)
    
    try:
        word_t = html['data']['entries'][0]['explain']
    
    except:
        word_t = "未查询到此单词，请检查是否有拼写错误。您所输入的内容是：" + word
    
    print(word_t)
    
i = 1;

while i >= 1:
    i+=1
    app()