#!usr/bin/python
# -*- coding: UTF-8 -*-
import csv

class ParseCSV:
    '''
    classdocs:read csv data
    '''
    
    def __init__(self, filename):
        self.filename = filename

    def readCSV(self):
        
        csvFile = open(self.filename, 'r')
        reader = csv.reader(csvFile)
        data = []
        for item in reader:
            data.append(item)
         
        csvFile.close()
        return data
        
# my = ParseCSV('api.csv')
# result = my.readCSV()
# print(result)