#coding=utf-8 
from aip import AipOcr
import configparser


class BaiDuAPI(object):
    '''识别文字'''
    
    def __init__(self):
        #实例化对象
        target = configparser.ConfigParser()
        target.read('password.ini')
        APPID = target.get('password','APPID')
        APIKey = target.get('password','APIKey')
        SecretKey = target.get('password','SecretKey')
        
        self.client = AipOcr(APPID,APIKey,SecretKey)
       

    #读取图片
    def getPicture(self,filepath):
        with open(filepath,'rb')as fps:
            return fps.read()


    def picture2Text(self,filePath):
        #读取图片
        image = self.getPicture(filePath)
        #识别图片
        text = self.client.basicGeneral(image)

        alltexts = ''
        for item in text['words_result']:
            alltexts = alltexts + ''.join(item.get('words',''))
        return alltexts

        







    


