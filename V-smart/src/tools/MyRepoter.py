#!usr/bin/python
# -*- coding: UTF-8 -*-

import HTMLTestRunner
import unittest
import os, time


list_path = os.path.join(os.path.dirname(__file__) + '/../testcase')

def RunSuite():
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(list_path, pattern='*Test.py', top_level_dir=None)
    
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
    return testunit

now = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())
filename = 'D:\\result.html'
fp = open(filename,'wb')

runner = HTMLTestRunner.HTMLTestRunner(
    stream = fp,
    title = u'小V接口测试报告',
    description = u'用例执行情况：')

runner.run(RunSuite())

fp.close()