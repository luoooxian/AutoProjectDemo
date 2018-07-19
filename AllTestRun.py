# -*- coding: utf-8 -*-
'''
@author: luoxian
#  Created: 2017-07-19
Comment: 自动运行自动套件test suites
'''

import unittest,os
from Lib.HTMLTestRunner import HTMLTestRunner

curdir = os.path.dirname(os.path.realpath(__file__))
TestSuites = curdir + r'/TestSuites'

suite = unittest.defaultTestLoader.discover(TestSuites, pattern="Test*.py")

if __name__=="__main__":

    runner = HTMLTestRunner(title="测试报告",
                            description="以下是测试报告的详细信息，请查看，谢谢。")
    runner.run(suite)
