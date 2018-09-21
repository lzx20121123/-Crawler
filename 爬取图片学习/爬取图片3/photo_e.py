
import os
import requests
import re
base_url = "https://geniesse.vivo.com.cn/index.php//Home/Index/officiaoWebGetImageList?page=1&num=126324"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3018.3 Safari/537.36'}
r = requests.get(base_url,headers = headers)
pat1 = '\d{4}\-\d{2}\-\d{2}'
pat2 = '[\/0-9a-z\.]{41}'
imglist1 = re.compile(pat1).findall(r.text)
imglist2 = re.compile(pat2).findall(r.text)
for i,j in zip(imglist1,imglist2):
    thisimgurl = 'https://files.vivo.com.cn/activity/attachments/geniesse/' + i + j
    # print(thisimgurl)
    root = "D://picss//"
    path = root + thisimgurl.split('/')[-1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            pic = requests.get(thisimgurl,headers = headers)
            with open(path,'wb') as f:
                f.write(pic.content)
                print("文件保存成功...")
        else:
            print("文件已存在...")
    except:
        print("爬取失败！")

