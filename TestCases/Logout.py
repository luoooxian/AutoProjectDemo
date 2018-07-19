# -*- coding: utf-8 -*-
'''
#  Created: 2017-07-19
@author: luoxian
Comment: 退出登录
'''

from selenium import webdriver
import unittest,time

class Logout(unittest.TestCase):
    def __init__(self,driver):
        u'''初始化driver参数'''
        self.driver = driver

    def logout(self):
        u'''退出'''
        time.sleep(3)
        self.driver.find_element_by_css_selector("i.icon.icon-seeuser").click()
        # 设置按钮
        self.driver.find_element_by_css_selector("i.icon-setup").click()
        self.driver.find_element_by_css_selector("button.v-btn.v-btn_btn").click()
        # 点确定按钮
        self.driver.find_element_by_css_selector("div.btn.v-dialog__confirm").click()
        # print("Logout successfully!")







