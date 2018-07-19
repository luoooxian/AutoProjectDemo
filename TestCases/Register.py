# -*- coding: utf-8 -*-
'''
@author: luoxian
#  Created: 2017-07-19
Project: Register function
'''

from selenium import webdriver
from time import sleep


class Register():
    def __init__(self, driver):
        u'''初始化driver参数'''
        self.driver = driver
        self.driver.set_window_size(375, 900)

    def register(self,phone ,password ,noSkip):
        #param: noSkip选择是否跳过
        self.driver.find_element_by_css_selector("i.icon.icon-seeuser").click()
        self.driver.find_element_by_css_selector("div.avata > div > img").click()
        #立即注册 register
        self.driver.find_element_by_css_selector("div.right").click()
        sleep(1)

        #用户协议 protocol
        self.driver.find_element_by_css_selector("span.proto").click()
        #获取协议页面的标题，判断是否进入该页面
        proto_title = self.driver.find_element_by_css_selector("div.side-page-wrapper.proto-wrapper > div.v-header.border-retina > div.center").text
        self.driver.find_element_by_css_selector("div.side-page-wrapper.proto-wrapper > div.v-header.border-retina > div.left > i.icon-arrow-left").click()
        sleep(1)

        #填写注册信息 如：用户名、短信验证码、密码等
        self.driver.find_element_by_css_selector ("div.register-cotent > div > div.cells.no-group-title > div.cell-wrapper > div.cell-bd > div.field-wrapper > input.field-item").send_keys \
            (phone)
        #填入验证码
        self.driver.find_element_by_xpath("(//input[@type='number'])[2]").send_keys("3456")
        #填入密码
        self.driver.find_element_by_xpath("(//input[@type='password'])[2]").send_keys(password)
        #勾选协议
        self.driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div[2]/"
                                          ""
                                          "div[2]/div/div").click()
        self.driver.find_element_by_css_selector("div.register-cotent > div.btn-wrapper > button.v-btn.v-btn_primary").click()

        #不跳过，填写公司信息
        if noSkip == True:
            self.driver.find_element_by_css_selector("XXXXX").send_keys("XXXXX")
            # ...
        else:
            sleep(1)
            # 跳过，不填写公司信息
            self.driver.find_element_by_css_selector("span.header-right").click()
        sleep(2)
        #获取用户名
        Name = self.driver.find_element_by_xpath("//div[@id='app']/div/div/div/p[2]").text

        return  Name,proto_title





