import sys
sys.path.append("C:/Users/li zhongxue/Desktop/zk")
from base.runmethod import RunMethod
from data.get_data import Getdata
from base.common_util import commonutil
from util.send_email import SendEmail
from util.mysql_search import OperationMysql
from util.logger import Logger
import time


class RunTest(object):
    def __init__(self):
        self.runmethod = RunMethod()
        self.getdata = Getdata()
        self.common = commonutil()
        self.sd_Email = SendEmail()
        self.Msql = OperationMysql()
    #程序执行的主入口
    def go_on_run(self):

        logname= "loger%s.txt" %time.strftime('%Y%m%d%H%M%S',time.localtime())          #日志名称
        testlog = Logger(logname,'DEBUG',"loger")                                       


        errorname = "errorlog%s.txt" %time.strftime('%Y%m%d%H%M%S',time.localtime())     #异常日志                  
        ferror = open(errorname ,'w')

        _timeformat = '%Y-%m-%d %H:%M:%S'
        pass_count =[]
        fail_count = []
        address = "http://192.168.1.102:3000"

        rows_count = self.getdata.get_caselines()               #行数
        for i in range(1,rows_count):                            #
            url = address + self.getdata.get_Url(i)             #url 
            #print (url)               
            method = self.getdata.get_request_method(i)         #请求方式
            is_run = self.getdata.get_isrun(i)                  #是否执行
            data = self.getdata.get_data_for_json(i)             #请求数据
            expect = self.getdata.get_expect_data(i)            #获得预期结果
            #res
            #print (expect)
            header = self.getdata.is_header(i)                  #是否携带heaers 
            if is_run:
                sql = self.getdata.get_mysql_data(i)         #是否有数据库命令
                #print (sql)
                try:
                    if sql ==None:
                        res = self.runmethod.run_main(method,url,data,header)
                        #print (res)                   
                    else:
                        self.Msql.run_sql(sql)
                        res = self.runmethod.run_main(method,url,data,header)
                        print(22)
                    com = self.common.is_contain(expect,res)
                    
                    testlog.info("url:%s,  method:%s,  data:%s, expect:%s, sql:%s, result:%s"%(url,method,data,expect,sql,com))  #日志
                    if com is True:
                        self.getdata.write_result(i,'pass')          #测试结果写入excel
                        print ('测试通过')
                        pass_count.append(com)
                    else:
                        self.getdata.write_result(i,res)          #测试结果写入excel
                        fail_count.append(com)
                        print(res)
                        print ('测试失败') 
                except Exception as e:
                    
                    ferror.write("[%s]  port：%s, error: %s \n"   %(time.strftime(_timeformat,time.localtime()),url,e))           #异常日志
                    self.getdata.write_result(i,'-----run fail---------')
                    com = False
                    print ("-----run fail---------")
                    fail_count.append(com)
        #ferror.close()        
        cont = self.sd_Email.send_main(pass_count,fail_count)    #邮件内容
        send_result = self.sd_Email.send_Email(cont)             #发送邮件
        return send_result
    
if __name__ =="__main__":
    run = RunTest()
    result = run.go_on_run()
    
    