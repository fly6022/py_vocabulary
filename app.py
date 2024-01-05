# -*- coding: utf-8 -*-
# @name   : py_word/app.py
# @author : fly6022
# @date   : 2023/8/26
# @Email  : i@fly6022.fun
# @version: 1.0.0
# @license: BSD-3-Clause

import requests as req
import urllib
import json
from datetime import datetime, timezone, timedelta

version = "v1.0.0"

print("py_word - 多快好省的单词整理程序（制作：fly6022 {i@flt6022.fun}）\n版本：" + version)

name = str(input("单词本名称："))

try:
    file_name = name + '.kuai.json'
    url = '../json/' + file_name
    origin_file = open('../json/' + file_name, 'r')    # 创建单词本
    bucket = json.loads(origin_file.read())     # 加载单词本
except:
    bucket = []                                 # 创建空容器并加载

def app():

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) appleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}; # header
    word, *vars = input().split(" ");

    def Kirisame_Req(url, headers):             # 伪造客户端请求服务器
        req = urllib.request.Request(url, headers = headers); 
        response = urllib.request.urlopen(req);
        global html;
        html = eval(response.read().decode('utf-8','ignore').replace(u'\xa9', u''));
        if html == "":
            html = json.loads(response.read().decode('utf-8','ignore').replace(u'\xa9', u''));        
        return html
        
    html = Kirisame_Req("https://dict.youdao.com/suggest?num=5&ver=3.0&doctype=json&cache=false&le=en&q=" + word, headers);

    try:
        word_t = html['data']['entries'][0]['explain'];
        print(word_t);
        
        for var in vars:    # 遍历不定长变量以获取参数信息
            if var == "-a":
                global other_entry_id_max, other_entry_id 
                
                other_entry_id_max = len(html['data']['entries']);
                other_entry_id = 1;
                        
                print("\n与单词" + word + "相关的内容：")
                        
                while 1 <= other_entry_id < other_entry_id_max:     # 循环遍历（相关内容）
                    global other_entry, other_explain
                    other_entry = html['data']['entries'][other_entry_id]['entry']
                    other_explain = html['data']['entries'][other_entry_id]['explain']
                    others = str(other_entry_id) + ":" + "[" + other_entry + "]" + other_explain + "\n"
                    others_bucket = []
                    others_data = {}
                    others_data['other_entry'] = other_entry
                    others_data['other_explain'] = other_explain
                    others_bucket.append(others_data)
                    print(others)
                    other_entry_id = other_entry_id + 1;
                
                pass
            
        for var in vars:
            
            if var == "-b":     # 录入单词本功能
                try:
                    others_bucket = others_bucket
                except:
                    others_bucket = []

                revise_date = ""
                revise_time = 0
                
                utc_now = datetime.utcnow().replace(tzinfo=timezone.utc)
                time = utc_now.astimezone(timezone(timedelta(hours=8)))
                time = datetime(time.year, time.month, time.day, time.hour, time.minute, time.second, time.microsecond)
                
                data = {}
                data['word'] = word;
                data['word_t'] = word_t;
                data['ticket'] = time.strftime('%Y-%m-%d %H:%M:%S');
                data['revise_date'] = revise_date;
                data['revise_time'] = revise_time;
                data['other_entrys'] = others_bucket;
                
                bucket.append(data)
                
                with open(file_name, 'w') as file:
                    file.write(str(json.dumps(bucket)))
                                
                print("已将单词：" + word + "的有关信息写入到“单词本”文件中。")
                
        for var in vars:
                    
            if var == "-rm":
                lenb = len(bucket)
            for a in range(0, len+1):
                pass
                            
    except:
        word_t = "未在互联网上查询到此内容。请检查网络是否成功连接以及您是否有拼写错误。您所输入的内容是：" + word;

if __name__ == "__main__":

    i = 1;

    while i >= 1:
        i+=1;
        app()