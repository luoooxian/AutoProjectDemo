# -*- coding: utf-8 -*-
'''
@author: luoxian
#  Created: 2017-07-19
Comment: 测试个人页面
'''

import unittest
from selenium import webdriver
from TestCases.My import My
from Lib.ReadConfig import Config
from TestCases.Login import LoginTest

cfg = Config()
#链接、用户名和密码
URL = cfg.web_Site()
UserName = cfg.name_Password()[0]
Password = cfg.name_Password()[1]

class TestMy(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.driver.implicitly_wait(10)
        cls.driver.get(URL)

    def test_My(self):
        '''我的(头像、XXXX、XXXX、XXXX等)'''
        LoginTest(self.driver).loginByName(UserName,Password)
        My(self.driver).myProfile()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=="__main__":
    unittest.main()