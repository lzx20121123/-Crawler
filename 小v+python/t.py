import csv
from logger import Logger
from urllist import getURL
from getTime import getT

if __name__ =='__main__':
    csvfile = open('resultlist.csv','w',newline='')
    wri = csv.writer(csvfile)
    header = ['url','realtimes','sum','avg','big','small']
    wri.writerow(header)
    Url = getURL('website.txt',50)
    log = Logger('log.txt','DEBUG','writerlog')



    for i in Url:
        ti = getT(i,5,'error.txt')
        print ("'url':%s,   'sum':%f,   'avg':%f,  'big':%f,    'small':%f" %(ti['url'],ti['sum'],ti['avg'],ti['max'],ti['min']))
        #print (ti)
        wri.writerow([ti['url'],ti['times'],ti['sum'],ti['avg'],ti['max'],ti['min']])
        #log.info("'url':%s, 'realtimes':%d, 'sum':%f, 'avg':%f, 'big':%f, 'small':%f,'timelist':%s"% (ti['url'],ti['times'],ti['sum'],ti['avg'],ti['max'],ti['min'],ti['time for each']))
        log.info(ti)
    csvfile.close()

