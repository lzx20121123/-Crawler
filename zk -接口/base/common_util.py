from data.get_data import Getdata

class commonutil(object):
    def __init__(self):
        self.globa = Getdata()

    def is_contain(self,str1,str2):
        #str1:预期结果
        #str2：run_test返回结果
        
        flag = None

        #if isinstance(str1,str):
            #str1 = str1.encode('unicode-escape').decode('string_escape')
        if str1 in str2:
            flag = True
        else:
            flag = False
        return flag
        

