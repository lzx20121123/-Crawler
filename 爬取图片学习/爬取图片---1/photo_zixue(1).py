#coding utf-8 
#auther zhongxue li
#2018-06-27

import requests
from bs4 import BeautifulSoup
import re


url = 'http://pic.yxdown.com/list/0_0_1.html'
def maxpage(url):
    #查询最大页数
    res = requests.get(url)
    soup = BeautifulSoup(res.text,"html.parser")
    last_page = str(soup.find_all('a',class_='last'))
    max_page_1 = re.findall(r'\d+',last_page)
    max_page =int(max_page_1[-1])  #最大页数
    print ('最大页数为：'+ str(max_page))
    return max_page
def every_page(url,maxpage):
    #制作每一页的链接
    now_page = int(re.search('0_0_(\d+).html',url,re.S).group(1))
    #print (now_page)
    page_group = []
    for i in range(now_page,maxpage+1):
        link = re.sub('0_0_\d+','0_0_%s'%i, url,re.S )
        page_group.append(link)
    #print (page_group)
    return (page_group)

def every_group(page_group):
    #制作每页上每个组的链接
    
    for url in page_group:
        req= requests.get(url)
        soup = BeautifulSoup(req.text,"html.parser")
        pic_group_1 = str(soup.find_all('a',class_='proimg' ))       #半筛选
        pic_group_2 = re.findall(r'/html/\d+.html',pic_group_1,re.S) #获得组图片的/html/
        same_url = 'http://pic.yxdown.com'
        Everygroup = []
        for i in pic_group_2:
            ul = str(same_url +str(i))                               #得到每组图片的链接
            Everygroup.append(ul.split('\n')[0])
        #print (Everygroup)
        return (Everygroup)
def Down_pic(every_group):
    #每个图片的链接
    pic_list = []
    F=1
    for url in every_group:
        req= requests.get(url)
        soup = BeautifulSoup(req.text,"html.parser")
        pic_url_1= str(soup.find_all('img' )) 
        pic_url = re.findall(r'src="(http:.+?\.jpg)"',pic_url_1,re.S)  #得到每张图片的链接
        F = F+1
        picnamestr = ''.join(str(F))
        n = 1
    print (pic_url) 


'''

     for i in pic_url:                                               #下载每张图片
            print ('now downloading:' + i)
            pic = requests.get(i)
            fp = open('pic\\'+picnamestr +'-'+str(n)+ '.jpg', 'wb')
            fp.write(pic.content)
            fp.close()
            n += 1'''

        #print(pic_url )  





if __name__ == '__main__':   
    page_group = every_page(url, 1)

    every_group = every_group(page_group)
    Down_pic(every_group)









