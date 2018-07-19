# -*- coding: utf-8 -*-
'''
@author: XXXXX
#  Created: 2017-07-19
Comment: 测试登录
'''

import unittest,time
from selenium import webdriver
from TestCases.Login import LoginTest
from TestCases.Logout import Logout
from Lib.ReadConfig import Config

cfg = Config()
UserName = cfg.name_Password()[0]
Password = cfg.name_Password()[1]
Phone = cfg.name_Password()[2]

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.driver.implicitly_wait(10)
        #获取链接
        URL = cfg.web_Site()
        cls.driver.get(URL)

    def test_LoginByName(self):
        '''用户名登录测试场景'''
        LoginTest(self.driver).loginByName(UserName,Password)
        time.sleep(2)
        Actual = self.driver.find_element_by_xpath("//div[@id='app']/div/div/div/p[2]").text
        Expect = UserName
        self.assertEqual(Expect,Actual,msg="失败原因：%s中没有发现%s"%(Expect,Actual))
        Logout(self.driver).logout()

    def test_LoginByPhone(self):
        '''手机号码登录测试场景'''
        LoginTest(self.driver).loginByName(Phone,Password)
        time.sleep(2)
        Actual = self.driver.find_element_by_xpath("//div[@id='app']/div/div/div/p[2]").text
        Logout(self.driver).logout()
        Expect = UserName
        self.assertEqual(Expect,Actual,msg="失败原因：%s中没有发现%s"%(Expect,Actual))

    def test_Message(self):
        '''登录异常测试场景(用户名为空/密码为空/用户名不合法/密码不合法)
           1.用户名为空，提示：用户名不能为空！
           2.密码为空，提示：密码不能为空！
           3.用户名不合法，提示：用户名为手机号码，或6-18位字母、数字，至少要包含字母，不区分大小写！
           4.密码不合法，提示：密码限6-18位，包含“字母、数字、符号”，其中的任意两种组合，区分大小写！
        '''

        #1.用户名不能为空/密码不能为空
        EmpMessages = LoginTest(self.driver).check_msg_empty(UserName)
        Actual_EmpMsg_name = EmpMessages[0]
        Actual_EmpMsg_pwd = EmpMessages[1]
        Expect_EmpMsg_name = "用户名不能为空！"
        Expect_EmpMsg_pwd = "密码不能为空！"
        self.assertEqual(Actual_EmpMsg_name,Expect_EmpMsg_name,"用户名/手机号提示语:[%s]不正确，正确提示语是[%s]"%(Actual_EmpMsg_name,Expect_EmpMsg_name))
        self.assertEqual(Actual_EmpMsg_pwd,Expect_EmpMsg_pwd,"密码提示语:[%s]不正确，正确提示语是[%s]"%(Actual_EmpMsg_pwd,Expect_EmpMsg_pwd))

        #2.用户名/密码不合法
        ErrMessages = LoginTest(self.driver).check_msg_error("13800",UserName,"123")
        Actual_ErrMsg_name = ErrMessages[0]
        Actual_ErrMsg_pwd = ErrMessages[1]
        Expect_ErrMsg_name = "用户名为手机号码，或6-18位字母、数字，至少要包含字母，不区分大小写！"
        Expect_ErrMsg_pwd = "密码限6-18位，包含“字母、数字、符号”，其中的任意两种组合，区分大小写！"
        self.assertEqual(Actual_ErrMsg_name,Expect_ErrMsg_name,"用户名/手机号提示语:[%s]不正确，正确提示语是[%s]"%(Actual_ErrMsg_name,Expect_ErrMsg_name))
        self.assertEqual(Actual_ErrMsg_pwd,Expect_ErrMsg_pwd,"密码提示语:[%s]不正确，正确提示语是[%s]"%(Actual_ErrMsg_pwd,Expect_ErrMsg_pwd))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=="__main__":
    unittest.main()