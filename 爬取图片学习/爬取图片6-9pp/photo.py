#coding=utf-8
import requests
from bs4 import BeautifulSoup
import os
import re

same_url = 'https://www.1800df.com/pic/3/'


#http请求头
Hostreferer = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer':'https://www.1800df.com/pic/3/'
               }
Picreferer = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer':'https://www.1800df.com/pic/3/'
}
#此请求头破解盗链

#此请求头破解盗链

start_html = requests.get(same_url,headers = Hostreferer)

#保存地址
path = '/home/lyt/mzitu/'

#找寻最大页数
'''res = r'<option .*?>(.*?)</option>'
soup = str(BeautifulSoup(start_html.text,"html.parser"))
index_1 = re.findall(r'index_(\d+).html',soup,re.S)
#index= re.findall(r'index_\d+.html',soup,re.S)
max_page = index_1[-1]
print ("最大页数: " + str(max_page))'''

#制作每一页的链接
def every_page():
   
    start_html = requests.get(same_url,headers = Hostreferer)
    soup = str(BeautifulSoup(start_html.text,"html.parser"))
    index  = re.findall(r'index_\d+.html',soup,re.S)
    page_url_list = []
    for i in index:
        url = same_url +str(i)
        page_url_list.append(url)                                   #----获得每一页的链接（前两个是重复的）
    #print (page_url_list)
    return(page_url_list)



def every_group(page_url_list):
    
    for url in page_url_list:
        page_html = requests.get(url,headers = Hostreferer)    #获得每一页的html
        soup_page = str(BeautifulSoup(page_html.text,"html.parser"))
        href  = re.findall(r'/pic/3/\d+-\d+-\d+/\d+.html',soup_page,re.S)#从每一页获得每组图片html元素
        web_url = 'https://www.1800df.com'              
        pic_group_list = []            #外网址
        for i in href:
            pic_group_link = web_url +str(i)
            pic_group_list.append(pic_group_link)                    #-----找到每组图片的链接
            n=1
            for g in pic_group_list:
                print ('开始爬取第%d组'%n)
                group_html =  requests.get(g,headers = Hostreferer)
                soup_g = str(BeautifulSoup(group_html.text,"html.parser"))
                src = re.findall(r'https://.+?.jpg',soup_g,re.S)      #----找到每张图片的链接
                n = n+1
                picnamestr = ''.join(str(n))
                p = 1
                for i in src:                                               #下载每张图片
                    print ('now downloading:' + i)
                    pic = requests.get(i)
                    fp = open('pic\\'+picnamestr +'-'+str(p)+ '.jpg', 'wb')
                    fp.write(pic.content)
                    fp.close()
                    p += 1







page_url_list = every_page()
every_group(page_url_list)