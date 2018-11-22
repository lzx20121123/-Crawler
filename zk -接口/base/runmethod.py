import requests
#from requests.packages import urllib3
import json

class RunMethod(object):
    #post请求
    def post_main(self,url,data,header=None):
        res = None
        if header=='yes':
            #urllib3.disable_warnings()
            res = requests.post(url=url,data=data,headers=header)
            
        else:
            #urllib3.disable_warnings()
            res = requests.post(url=url,data=data,headers=None)
          
        return res.json()

    def get_main(self,url,data=None,header=None):
        res = None
        reqs = None
        if header==None:
            res = requests.get(url=url,data=data,verify=False)
                    
        else:            
            res = requests.get(url=url,data=data,headers=header,verify=False)
        
        if res.text.startswith(u'\ufeff'):
            reqs =json.loads(res.text.encode('utf8')[3:].decode('utf8'))
        else:
            reqs = json.loads(res.text)
         
        return reqs

    
    #运行post/get请求
    def run_main(self,method,url,data=None,header=None):
        res = None
        if method=='get':
            res = self.get_main(url,data,header=None)
            
        else:
            res = self.post_main(url,data,header=None)
      
        return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)
        




if __name__ =='__main__':
    url ="http://192.168.1.102:3000/api/log/getaction?html=true&m=oper&_=1541732496173"
    header={
       "Content-Type":"application/json; charset=utf-8"
    }
    method= 'get'
    n = RunMethod()
    #n.get_main(url,header=header)
    n.run_main(method,url,data=None,header=None)