import pymysql

class OperationMysql(object):
    #连接数据库
    def __init__(self):
        self.db = pymysql.connect("192.168.1.102","****","*****","*****" )
        self.cursor = self.db.cursor()
    #查询
    def search_one(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()
        
    #插入、删除、等。。。
    def run_sql(self,sql):
        try:            
            self.cursor.execute(sql)        # 执行sql语句            
            #self.db.commit()                # 提交到数据库执行
            res =  "success"
        except:           
            self.db.rollback()              # 发生错误时回滚 
            res = 'fail'     
        self.db.close()                     # 关闭数据库连接
        print (res)
       
    
        
     
   


if __name__ =="__main__":
    #sql = "select * from report_group where name='vb'"
    sql =  'INSERT INTO report_group (hash_key,name,parent_id,relation,is_sync,is_cascade,deleted) VALUES("f7c5c2ad70371c011fc0045e38dcfbc2","group1","0"," ","0","0","1")'
    print (type(sql))
    cn = OperationMysql()
    res = cn.run_sql(sql)
    print (res)
    



    