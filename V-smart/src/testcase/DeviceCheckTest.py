#!usr/bin/python
# -*- coding: UTF-8 -*-

import unittest,sys
sys.path.append('C:\Users\work\Desktop\V-smart')
from common.ParseCSV import ParseCSV
from interface.DeviceInfo import DeviceInfo
from common.request import request

class Test(unittest.TestCase):
    

    def test_01(self):
        
        device_data = ParseCSV('../data/deviceinfo.csv').readCSV()
        
        data = DeviceInfo.getInfo(self, device_data[0][1], device_data[0][2], device_data[0][3], device_data[0][4])
        response = request.pull_post(self, data = data)
        print(response)
        self.assertIsNotNone(response)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()