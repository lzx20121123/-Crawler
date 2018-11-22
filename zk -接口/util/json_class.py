import json 

#a =open(file)
#b=json.load(a)
#print (b['login'])


class OperationJson(object):
    def __init__(self,name_id,file_name=None):
        if file_name:
            self.file_name = file_name
            
        else:
            self.file_name = 'C:/Users/li zhongxue/Desktop/zk/file/user.json'
        self.name_id = name_id
        self.data = self.read_data()
       
    #读取json
    def read_data(self):
        with open(self.file_name) as fi:
            data = json.load(fi)
            return data
    #返回ID对应的数据
    def get_data(self):
        return self.data[self.name_id]
    #返回



if __name__=="__main__":
    
    
    file = './file/case.json'
    id = 'login'
    ab = OperationJson(id)
    c= ab.get_data()
    print (c)