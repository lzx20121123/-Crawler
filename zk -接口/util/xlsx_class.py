import xlrd
from xlutils.copy import copy


class OperationExcel(object):
    def __init__(self,file_name=None,sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id= sheet_id
        else:
            self.file_name='C:/Users/li zhongxue/Desktop/zk/file/case1.xlsx'
            self.sheet_id=0
        self.data = self.get_data()

    #打开第*张表
    def get_data(self):
        data=xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables
    #读取表的行数
    def get_lines(self):
        tab = self.data.nrows
        return tab
    #读取某个数据   
    def get_cell_value(self,row,low):
        data = self.data.cell_value(row,low)
        return data
    #写入excel
    def write_value(self,row,col,value):
        data = xlrd.open_workbook(self.file_name) #打开
        write_data = copy(data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row,col,value)
        write_data.save(self.file_name)

        



if __name__=='__main__':
    #print ("buxin")
    file_name='./file/case.xlsx'
    sheet_id=0
    table = OperationExcel(file_name,sheet_id)
    
    print (table.get_lines())
    print (table.get_cell_value(2,3))