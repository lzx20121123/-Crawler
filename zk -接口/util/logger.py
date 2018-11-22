#coding:utf-8
import logging
import time
class Logger(object):
    def __init__(self,logname,loglevel,logger):
        self.logname = "responsetimelog%s.txt" %time.strftime('%Y%m%d%H%M%S',time.localtime())      #响应时间记录日志文件名格式

        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        fh = logging.FileHandler(self.logname)
        fh.setLevel(logging.DEBUG)

        format = '[%(asctime)s] %(levelname)s : %(message)s'
        formatter = logging.Formatter(format)
        fh.setFormatter(formatter)

        self.logger.addHandler(fh)

    def info(self,message):
        self.logger.info(message)

    def error(self,message):
        self.logger.error(message)

if __name__ == '__main__':
    updatelog = Logger('updateflog.txt','DEBUG','updatelog')
    updatelog.info("this is a test")
