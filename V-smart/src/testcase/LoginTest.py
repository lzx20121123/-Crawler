#!usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
from interface.Login import Login
from common.ParseCSV import ParseCSV
from common.request import request

class Test(unittest.TestCase):
    
    
    def test_01(self):
        
        login_data = ParseCSV('../data/login.csv').readCSV()
        
        for i in range(len(login_data)):
            
            data = Login.login_phone(self, login_data[i][1], login_data[i][2])
            response = request.pull_post(self, data)
            
            #analyze the response for add assert
            req_result = Login.login_phone_analyse(self, response)
            
            #add assert
            n = int(login_data[i][3])
            self.assertEqual(n, req_result)
            

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()