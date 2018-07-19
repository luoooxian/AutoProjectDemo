# -*- coding: utf-8 -*-
'''
#  Created: 2017-07-19
@author: luoxian
Comment: 登录页面
'''

from selenium import webdriver
import time

class LoginTest ():
    def __init__(self,driver):
        u'''初始化driver参数'''
        self.driver = driver
        #设置窗口大小
        self.driver.set_window_size(375, 900)

    #移动端登录
    def loginByName(self,username,password):
        u'''用户名和密码登录'''
        time.sleep(1)
        self.driver.find_element_by_css_selector("i.icon.icon-seeuser").click()
        self.driver.find_element_by_css_selector("div.avata > div > img").click()
        # 输入手机号码/用户名
        self.driver.find_element_by_css_selector("input.field-item").clear()
        self.driver.find_element_by_css_selector("input.field-item").send_keys(username)
        # 输入密码
        self.driver.find_element_by_xpath("//input[@type='password']").clear()
        self.driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
        # 登录
        self.driver.find_element_by_css_selector("button.v-btn.v-btn_primary").click()
        time.sleep(2)

    #异常场景测试：用户名、密码为空校验
    def check_msg_empty(self,username):
        u'''输入用户名和密码为空'''
        time.sleep(1)
        self.driver.find_element_by_css_selector("i.icon.icon-seeuser").click()
        self.driver.find_element_by_css_selector("div.avata > div > img").click()
        # 登录
        self.driver.find_element_by_css_selector("button.v-btn.v-btn_primary").click()
        #username empty tips
        username_empty = self.driver.find_element_by_css_selector("div.v-dialog__message").text
        time.sleep(1)
        self.driver.find_element_by_css_selector("div.btn.v-dialog__confirm").click()

        self.driver.find_element_by_css_selector("input.field-item").send_keys(username)
        self.driver.find_element_by_css_selector("button.v-btn.v-btn_primary").click()
        #password empty tips
        password_empty = self.driver.find_element_by_css_selector("div.v-dialog__message").text
        time.sleep(1)
        self.driver.find_element_by_css_selector("div.btn.v-dialog__confirm").click()
        #返回页面
        self.driver.back()
        return  username_empty,password_empty

    # 异常场景测试：用户名、密码错误
    def check_msg_error(self,invalid_name,valid_name,invalid_pwd):
        u'''用户名或密码为错误验证'''
        self.driver.find_element_by_css_selector("i.icon.icon-seeuser").click()
        self.driver.find_element_by_css_selector("div.avata > div > img").click()

        self.driver.find_element_by_css_selector("input.field-item").send_keys(invalid_name)
        self.driver.find_element_by_css_selector("button.v-btn.v-btn_primary").click()
        #获取用户名错误提示
        msg_name_invalid = self.driver.find_element_by_css_selector("div.v-dialog__message").text
        self.driver.find_element_by_css_selector("div.btn.v-dialog__confirm").click()

        #刷新页面
        self.driver.refresh()
        self.driver.find_element_by_css_selector("input.field-item").send_keys(valid_name)
        self.driver.find_element_by_xpath("//input[@type='password']").send_keys(invalid_pwd)
        self.driver.find_element_by_css_selector("button.v-btn.v-btn_primary").click()

        #获取密码提示
        msg_password_invalid = self.driver.find_element_by_css_selector("div.v-dialog__message").text
        self.driver.find_element_by_css_selector("div.btn.v-dialog__confirm").click()
        #返回页面
        self.driver.back()

        return  msg_name_invalid,msg_password_invalid










