# -*- coding: utf-8 -*-
'''
@author: luoxian
#  Created: 2017-07-19
Comment: 测试注册
'''

import unittest,time
from selenium import webdriver
from TestCases.Register import Register
from TestCases.Logout import Logout
from TestCases.Login import LoginTest
from Lib.ReadConfig import Config

#获取链接
cfg = Config()
#网站链接
URL = cfg.web_Site()
#密码、电话号码
Password = cfg.name_Password()[1]
Phone = cfg.name_Password()[2]

class TestRegister(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.driver.implicitly_wait(10)
        cls.driver.get(URL)

    def test_Register(self):
        '''注册用户'''
        ListInfo = Register(self.driver).register(Phone,Password, False)
        #获取用户名
        UserName = ListInfo[0]
        #获取协议标题
        proto_title = ListInfo[1]

        #退出登录
        Logout(self.driver).logout()

        # 验证是否登录
        LoginTest(self.driver).loginByName(UserName,Password)
        #退出登录
        Logout(self.driver).logout()

        Expect = "用户服务协议"
        self.assertEqual(Expect,proto_title,msg="失败原因：%s中没有发现%s"%(Expect,proto_title))

    # def test_Register_Noskip(self):

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=="__main__":
    unittest.main()