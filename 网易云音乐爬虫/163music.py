#encoding utf-8
import requests
from bs4 import BeautifulSoup
import csv
import re


#写这个爬虫的目的主要是抓取在网易云音乐里，华语男歌手top10的歌手的热门歌曲信息。

#信息包括歌曲名称，歌曲所属专辑和歌曲的网页链接

#参考自：https://blog.csdn.net/qq_32511479/article/details/76281036?locationNum=6&fps=1


#url ='http://music.163.com/discover/artist/cat?id=1001'


def get_songer(url):

    header ={
        'Referer'	:'https://music.163.com/',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    res = requests.get(url,headers=header).text
    r = BeautifulSoup(res,'lxml')
    songer_ID=re.findall(r'.*?<a class="msk" href="(/artist\?id=.*?)" title="(.*?)的音乐"></a>.*?',str(r))       #歌手ID
    songer_name=re.findall(r'.*?<a class="msk" href="/artist\?id=.*?" title="(.*?)的音乐"></a>.*?',str(r))    #歌手名字
 
    url = 'http://music.163.com'
    singer_dict = {}
    for i in songer_ID:
        singer_url = url +i[0]
        #singer_name = i[1]
        #singer_dict[singer_name]=singer_url            #---------------------------把两个元素循环加成字典
        req = requests.get(singer_url,headers = header).text
        html = BeautifulSoup(req,'lxml')
        song = html.find('ul',{'class':'f-hide'}).find_all('a')
        songname = re.findall(r'.*?<a href="(/song\?id=\d+)">(.*?)</a>.*?',str(song)) 
        #print (songname)
        filename = '%s.csv'%i[1]
        Header = ['歌手','歌曲名称','歌曲链接']
        csvfile = open(filename,'w',encoding='utf-8',newline='')
        wri = csv.writer(csvfile)
        wri.writerow(Header)
        

        for n in songname:
            music_url = 'http://music.163.com'+n[0]
            #return ()
            wri.writerow([i[1],n[1],music_url])
        #print(music_url)
        print('%s的歌曲列表下载完成'%i[1])
        csvfile.close()   
    print('全部完成')



url ='http://music.163.com/discover/artist/cat?id=1001'

songer_ID = get_songer(url)
