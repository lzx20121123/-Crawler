#!usr/bin/python
# -*- coding: UTF-8 -*-

import requests
from common.ParseCSV import ParseCSV


class request(object):
    '''
    package requests
    '''
    
    def pull_post(self, data):
        try:
            headers = {"Content-Type": "application/octet-stream"}
            api_data = ParseCSV('../data/api.csv').readCSV()
            url = api_data[0][1]
            response = requests.post(url, data = data, headers = headers, verify=False)
            
            return response
        except Exception as e:
            return e
        
