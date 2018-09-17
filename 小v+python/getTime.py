# coding utf-8
import time,urllib.request,csv


def getT(url,times,errorLog):
    _timeformat = '%Y-%m-%d %H:%M:%S'
    ferror = open(errorLog,'w')
    avg = 0
    big = 0
    small = 100
    Sum = 0
    tlist=[]
    i = 0 
    realtimes= times
    #print (realtimes)
    while i < times:
        t2 = -100
        i = i+1
        try:
            t1 = time.time()
            #print (time.strftime(_timeformat,time.localtime(t1)))
            #print (t1)           
            urllib.request.urlopen(url,timeout=5)
            t2 = time.time()-t1
            #print (time.strftime(_timeformat,time.localtime(t2)))
            #print (t2)
            
           
        except (urllib.request.URLError,urllib.request.HTTPError,urllib.error.HTTPError,urllib.error.URLError,Exception) as e:
            #ferror.write("Time:[%s] ,Url:%s  ,第 %d 次 ,error：%s\n" % (time.strftime(_timeformat,time.localtime()) ,url,i,e))
            ferror.write("[%s]\turl %s download times %d error : %s\r\n" %(time.strftime(_timeformat,time.localtime()),url,i,e))
        tlist.append(round(t2,4))
        if t2 > big:
            big = t2
        if t2 < small:
            small = t2
        Sum = Sum +t2
        if t1 == -100:
            realtimes = realtimes -1
            print (realtimes)
            continue
        #ferror.close()
    
            
    if realtimes !=0:
        avg = Sum/realtimes
    

    return {"url": url, "times": realtimes,  "min": round(small,3), "max": round(big,3), "sum": round(Sum,3), "avg": round(avg,3),"time for each": tlist}


if __name__=='__main__':
    ds = getT('http://www.baidu.com',3,'error.txt')
    #print ("url:%s,   sum:%f,  avg:%f,  big:%f,   small:%f\n" %( ti['Url'], ti['sum'], ti['Avg'], ti['Big'], ti['Small']))
    print ("url:%s,   avg:%f s,  times:%d,  min:%f s,  max:%f s" %(ds['url'],ds['avg'],ds['times'],ds["min"],ds['max']))
   