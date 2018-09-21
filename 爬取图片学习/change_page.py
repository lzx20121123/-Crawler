# coding=utf-8
import requests
import re
from lxml import etree
import time
import sys
import importlib
importlib.reload(sys)

 
 
def changepage(url,total_page):
    now_page = int(re.search('1-0-0-0-0-(\d)',url,re.S).group(1))   #可修改
    print (now_page)
    page_group = []
    for i in range(now_page,total_page+1):
        link = re.sub('1-0-0-0-0-(\d)','1-0-0-0-0-%s'%i,url,re.S)       #可修改
        page_group.append(link)
    print(page_group)
    return page_group
    
url = 'https://ibaotu.com/guanggao/1-0-0-0-0-1.html'   #可修改
changepage(url,100)

