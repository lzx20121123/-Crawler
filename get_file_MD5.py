import os
import hashlib
allpath=[]
allname=[]

#遍历文件夹下所有文件，并将MD5和路径写入到文件

def getallfile(path):
    allfilelist=os.listdir(path)
    # 遍历该文件夹下的所有目录或者文件
    for file in allfilelist:
        filepath=os.path.join(path,file)
        # 如果是文件夹，递归调用函数
        if os.path.isdir(filepath):
            getallfile(filepath)
        # 如果不是文件夹，保存文件路径及文件名
        elif os.path.isfile(filepath):
            allpath.append(filepath)
            allname.append(file)
    return allpath, allname
if __name__ == "__main__":
    rootdir = 'E:\\文档'
    files, names = getallfile(rootdir)
    #fi= open('../md5.txt','r+')
    for file in files:
        #print(file)
        #print (hashlib.md5(open(r'%s'% file, 'rb').read()).hexdigest())
        fi= open('../md5.txt','a')
        fi.write(file)
        fi.write(',  MD5:')
        fi.write(hashlib.md5(open(r'%s'% file, 'rb').read()).hexdigest()+"\n")

        
