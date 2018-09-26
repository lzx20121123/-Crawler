import os
import re 
import sys

def add_names():
    print('nba')
    text = input('请输入要添加的前缀')
    ma = '[%s]'%text
    old_names = os.listdir()                #每个文件的名称
   
    for i in old_names:
        newnames = ma+i
        os.rename(i,newnames)




            
        
def main():
    option = int(input('请选择功能数值:\n1.添加前缀\n2.退出程序\n'))
    if option ==1:
        add_names()
    
    else:
        exit()

if __name__ =='__main__':
    main()