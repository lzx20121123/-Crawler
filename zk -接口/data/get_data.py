from util.xlsx_class import OperationExcel
from data.data_config import global_var
from util.json_class import OperationJson
import json
from util.mysql_search import OperationMysql

class Getdata(object):
    def __init__(self):
        self.opera_excel = OperationExcel()
        self.da_config = global_var()
        #self.opera_json = OperationJson()
    #获取excel行数，即case个数
    def get_caselines(self):
        return self.opera_excel.get_lines()
    #判断是否run
    def get_isrun(self,row):
        flage = None
        col = self.da_config.get_run()      #列
        is_run = self.opera_excel.get_cell_value(row,int(col))
        if is_run =='yes':
            flage = True
        else:
            flage = False
        return flage
    #判断是否携带header
    def is_header(self,row):
        flag = None
        col = self.da_config.get_header()
        header = self.opera_excel.get_cell_value(row,int(col))
        if header =='yes':
            flag = self.da_config.get_header()                  #-----------------------------
        else:
            flag = None
        return flag
    #判断请求方方法
    def get_request_method(self,row):
        col = int(self.da_config.get_requses_way())
        try:
            request_method = self.opera_excel.get_cell_value(row,col)
            return request_method
        except:
            return '请求方式获取异常'
    #获得url
    def get_Url(self,row):
        col = int(self.da_config.get_url())
        try:
            url = self.opera_excel.get_cell_value(row,col)
            return url
        except:
            return 'api 为空'

    #判断是否有请求数据，如果有，获得请求数据
    def get_request_data(self,row):
        flag =None
        col = int(self.da_config.get_data())
        request_data = self.opera_excel.get_cell_value(row,col)
        if request_data =="no":
            flag = None
        else:
            flag = request_data
        return flag
    


    #，如果有data，通过关键字拿到data数据
    def get_data_for_json(self,row):
        flag = None
        da = self.get_request_data(row)
        if da ==None:
            flag = None
        else:
            opera_json = OperationJson(da)
            flag = opera_json.get_data()
        return flag


    #判断是否有mysql命令，如果有，获得mysql关键词
    def get_mysql_data(self,row):
        flag= None
        col =int(self.da_config.get_mysql())
        mysql =self.opera_excel.get_cell_value(row,col)
        if mysql =='no':
            flag = None
        else:
            flag = mysql
        return flag

    #通过mysql关键词获得mysql命令
    def get_mysql_for_json(self,row):
        flag = None
        my = self.get_mysql_data(row)
        if my ==None:
            flag=None
        else:
            opera_json = OperationJson(my)
            flag = opera_json.get_data()
        return flag

    #通过获得预期结果
    def get_expect_data(self,row):
        
        col = int(self.da_config.get_expect())
        expect = self.opera_excel.get_cell_value(row,col)
        return expect
    
    #通过sql语句获取预期结果
    #def get_expect_data_for_mysql(self,row):
        #col = int(self.da_config.get_expect())
        #mys = OperationMysql()
        #res = mys.search_one(self.get_expect_data(row))
        #return res


    #excel中写入结果
    def write_result(self,row,result):
        col = int(self.da_config.get_result())
        result = self.opera_excel.write_value(row,col,result)
        


if __name__=="__main__":
    n = Getdata()
    print (n.get_isrun(1))