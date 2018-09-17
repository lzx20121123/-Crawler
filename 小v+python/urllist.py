import csv
from logger import Logger
from getTime import getT


def getURL(file,enD):
    n = open(file)
    URLlist= []
    b = n.readlines()
    index=0
    for i in b:
        
        if index in range(0,enD):
            URLlist.append(i.strip('\n'))
        else:
            break
        index = index+1
    n.close()
    return URLlist
    print (URLlist)


