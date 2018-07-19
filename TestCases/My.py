# -*- coding: utf-8 -*-
'''
@author: luoxian
Created on 2018-6-12
Comment: 个人设置模块
'''

from selenium import webdriver
import time,os

#获取当前目录
curdir = os.path.dirname(os.path.realpath(__file__))
#获取上级目录
fdir = os.path.abspath(os.path.dirname(curdir)+os.path.sep+".")

#个人设置模块
class My():
    def __init__(self,driver):
        u'''初始化driver参数'''
        self.driver = driver

    def myProfile(self):
        '''上传头像'''
        self.driver.find_element_by_css_selector("i.icon.icon-seeuser").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector("input.v-uploader__input").send_keys(fdir + r"\Img\avata.png")

    # def myOrder(self):
    # def myfavorites(self,option):
    # def myDelivery(self):
    # def myInvoice(self):
    # def myCertification(self,CompName):

