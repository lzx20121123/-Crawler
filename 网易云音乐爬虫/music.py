import requests
from tkinter import *
from bs4 import BeautifulSoup
import urllib.request
import time

#获取网页代码
#获取ID、生成下载链接
#下载音乐



def download_music():
    
    url =entry.get()                    #获取用户输入的网址
    #请求头
    header={
        'Host':'music.163.com',
        'Referer':'https://music.163.com/',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
    }

    # https://music.163.com/playlist?id=404757132
    res = requests.get(url,headers=header).text             #获取网页代码
    #方法1
    #r = BeautifulSoup(res,'html.parser')                           #解析网页
    #dict_id = r.find('ul',{'class':'f-hide'}).find_all('a')
    #print (dict_id)
    #方法2
    r = BeautifulSoup(res,'lxml')
    dict_music = r.find('ul',{'class':'f-hide'}).find_all('a')
    music_dict ={}
    for music in dict_music:
        music_ID = music.get('href').strip('/song?id=')
        music_name= music.text
        #print (music_ID)
        #print (music_name)
        music_dict[music_ID]=music_name                                 #---------------------------把两个元素循环加成字典
    #print(music_dict)


    #下载
    for song_id in music_dict:
        song_URL = 'http://music.163.com/song/media/outer/url?id=%s.mp3' %song_id
        path ='C:\\Users\li zhongxue\Desktop\网易云音乐\music\\%s.mp3'%music_dict[song_id]



        text.insert(END,'正在下载%s'%music_dict[song_id])
        text.see(END)
        text.update()

        time.sleep(1)
        #下载
        urllib.request.urlretrieve(song_URL,path)
        print ('%s下载完成'%song_id)
        text.insert(END,'%s下载完成'%music_dict[song_id])
        text.see(END)
        text.update()

# 搭建界面
root = Tk()                                                             #创建窗口
root.title('网易云音乐下载')                                             #窗口的标题
root.geometry('460x400')                                                #窗口的大小
root.geometry('+500+230')                                               #窗口的位置
label = Label(root,text= '请输入要下载的URL:',font=('微软雅黑',10))       #文本框
label.grid(row=0, column=0)                                              #文本框的大小
entry = Entry(root,font =('微软雅黑',20))                               #输入框的位置 
entry.grid(row=0,column = 1)                                            #输入框的大小
text = Listbox(root,font=('微软雅黑',15),width=38,height=10)            # 信息框的大小
text.grid(row =1,columnspan=2)                                          # 信息框的位置   columnspan:组件跨越的列数
button = Button(root,text='开始下载',font=('微软雅黑',15),command=download_music)              #开始按钮大小
button.grid(row=2,column=0,sticky=W)                                    #开始按钮的位置   N S W E:上下左右
button2= Button(root,text='退出',font=('微软雅黑',15))                  #结束按钮大小
button2.grid(row=2,column=1,sticky=E)                                   #结束按钮位置
root.mainloop()                                                         # 显示窗口