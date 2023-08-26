# -*- coding: utf-8 -*-
# @name   : py_word/app.py
# @author : fly6022
# @date   : 2023/8/26
# @Email  : i@fly6022.fun
# @version: 1.0.0
# @license: The Unlicense license 

import requests as req
import urllib
import os

"""
def bucket(): # 记录ID、单词、记录时间（数据库功能：增删查），艾宾浩斯记忆曲线复习
    global file
    file = 0
    return file
"""

def app():

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) appleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}; # header
    word, *vars = input().split(" ");

    def Kirisame_Req(url, headers):
        req = urllib.request.Request(url, headers = headers); # 伪造客户端请求服务器
        response = urllib.request.urlopen(req);
        html = eval(response.read().decode('utf-8','ignore').replace(u'\xa9', u''));
        return html
        
    html = Kirisame_Req("https://dict.youdao.com/suggest?num=5&ver=3.0&doctype=json&cache=false&le=en&q=" + word, headers);

    try:
        word_t = html['data']['entries'][0]['explain'];
        print(word_t);
        
        for var in vars:
            if var == "-a":
                global other_entry_id_max, other_entry_id 
                
                other_entry_id_max = len(html['data']['entries']);
                other_entry_id = 1;
                        
                print("\n与单词" + word + "相关的内容：")
                        
                while 1 <= other_entry_id < other_entry_id_max:
                    global other_entry, other_explain
                    other_entry = html['data']['entries'][other_entry_id]['entry']
                    other_explain = html['data']['entries'][other_entry_id]['explain']
                    print(str(other_entry_id) + ":" + "[" + other_entry + "]" + other_explain + "\n")
                    other_entry_id = other_entry_id + 1;

    except:
        word_t = "未查询到此单词，请检查是否有拼写错误。您所输入的内容是：" + word;


if __name__ == "__main__":

    i = 1;

    while i >= 1:
        i+=1;
        app()