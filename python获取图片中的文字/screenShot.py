#coding utf-8
#控制键盘事件
import sys
import keyboard
from PIL import ImageGrab
import time
from baiDui import BaiDuAPI
from GetText import getText
from GetText import setText

def screenShot():
    if keyboard.wait(hotkey='ctrl+alt+A') ==None :
        if keyboard.wait(hotkey='ctrl+shift') ==None:
            time.sleep(0.01)
            #读取剪切板里的图片
            IM = ImageGrab.grabclipboard()
            #保存图片
            IM.save('imageGrab.png')



if __name__ == '__main__':
    for i in range(sys.maxsize):
        
        screenShot()
        baiduapi = BaiDuAPI()
        text = baiduapi.picture2Text('imageGrab.png')
        #print (text)   
        setText(text.encode('gb2312'))
        getText()