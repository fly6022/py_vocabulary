# -*- coding: utf-8 -*-
# @name   : py_word/app.py
# @author : fly6022
# @date   : 2024/2/9
# @Email  : i@fly6022.fun
# @version: 2.0.0
# @license: BSD-3-Clause

import os
import requests as req
import urllib
import json
import csv
import time
from datetime import datetime, timezone, timedelta

version = "v2.0.0"

print("py_word - 多快好省的单词整理程序（制作：fly6022 {i@fly6022.fun}）\n版本：" + version)

name = str(input("单词本名称："))                               # 创建空容器并加载

try:
    file_class = ".json"                        # 扩展名
    file_name = 'json/' + name + '.kirisame.pyword'       # 文件名
    path = os.getcwd()
    a_path = os.path.join(path, file_name + file_class)
    origin_file = open(a_path, 'r')             # 创建单词本
    bucket = json.loads(origin_file.read())     # 加载单词本
except:
    bucket = []  

def app():
    

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) appleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}; # header
    key_1, *vars = input().split(" ");

    def Req(url, headers):             # 伪造客户端请求服务器
        req = urllib.request.Request(url, headers = headers); 
        response = urllib.request.urlopen(req);
        global html;
        html = eval(response.read().decode('utf-8','ignore').replace(u'\xa9', u''));
        if html == "":
            html = json.loads(response.read().decode('utf-8','ignore').replace(u'\xa9', u''));        
        return html

    if key_1.find(".txt") != -1:

        words_data = []

        for word_ in open(key_1, 'r'):
            word_ = word_.replace("\n", "")
            words_data.append(word_)

        pass

    if key_1.find(".json") != -1:

        json_r = open(key_1, "r", encoding='utf-8')
        data_list = json.load(json_r)
        title = data_list[0].keys()
        words_data = []
        for data in data_list:
            words_data.append(data.values())
        pass

    else:
        word = key_1
        

    if key_1.find(".txt") == -1 and key_1.find(".json") == -1:
        html = Req("https://dict.youdao.com/suggest?num=5&ver=3.0&doctype=json&cache=false&le=en&q=" + word, headers);
        word_t = html['data']['entries'][0]['explain'];
    
    for var in vars:                        # 遍历不定长变量以获取参数信息

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
                print(others)
                
                others_bucket = []
                others_data = {}
                others_data['other_entry'] = other_entry
                others_data['other_explain'] = other_explain
                others_bucket.append(others_data)
                other_entry_id = other_entry_id + 1;
            
            pass
        
        if var == "-b":                     # 录入单词本功能
            
            def add_word(word):

                try:
                    others_bucket = others_bucket
                except:
                    others_bucket = []

                revise_date = ""
                revise_time = 0

                time = datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8)))
                time = datetime(time.year, time.month, time.day, time.hour, time.minute, time.second, time.microsecond)
                
                data = {}
                data['word'] = word;
                data['word_t'] = word_t;
                data['ticket'] = time.strftime('%Y-%m-%d %H:%M:%S');
                data['revise_date'] = revise_date;
                data['revise_time'] = revise_time;
                # data['other_entrys'] = others_bucket;
                
                bucket.append(data);
                
                with open(a_path, 'w') as file:  # 调用单词本文件
                    file.write(str(json.dumps(bucket)))
                                
                print("已将单词：" + word + "的有关信息写入到“单词本”文件中。")
            
                return data;
        
            if key_1.find(".txt") != -1:            # 判断是否为.txt文件，若是，则批量添加单词

                try: 
                    time_start = time.time()
                    for word in words_data:
                        html = Req("https://dict.youdao.com/suggest?num=5&ver=3.0&doctype=json&cache=false&le=en&q=" + word, headers);
                        word_t = html['data']['entries'][0]['explain'];
                        print(word_t);
                        add_word(word)
                    time_end = time.time()
                    delta_time = time_end - time_start
                    print("批量录入完毕. 用时：", delta_time, 's')
                    pass

                except:
                    print("批量添加单词时出错，请检查文本文件内容及格式。")
                    pass
            
            if key_1.find(".json") != -1:
                
                time_start = time.time()

                csv_fp = open(os.path.join(path, "csv/" + name + ".kirisame.pyword" + ".csv"), "w", encoding='utf-8', newline='')
                writer = csv.writer(csv_fp)
                writer.writerow(title)
                writer.writerows(words_data)
                csv_fp.close()
                
                time_end = time.time()
                delta_time = time_end - time_start
                print("csv文件生成成功！. 用时：", delta_time, 's')


    return

if __name__ == "__main__":

    i = 1;

    while i >= 1:
        i+=1;
        app()