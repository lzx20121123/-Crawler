#coding:utf-8
import logging


#日志类
class Logger():
    def __init__(self,logname,loglevel,logger):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        fh = logging.FileHandler(logname)
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
