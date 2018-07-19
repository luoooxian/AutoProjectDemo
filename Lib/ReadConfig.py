# -*- coding:utf-8 -*-
'''
@author: luoxian
#  Created: 2017-07-19
Description: 读取配置文件信息
'''

import os
import configparser

#get file path
curdir = os.path.dirname(os.path.realpath(__file__))
fdir = os.path.abspath(os.path.dirname(curdir)+os.path.sep+".")

config = configparser.ConfigParser()
file_path = fdir + r"\Config\config.ini"
config.read(file_path,encoding='UTF-8')

class Config():

    #读取账号、密码、手机号码
    def name_Password(self):
        Username = config.get("Account","Name")
        Password = config.get("Account","Password")
        Phone = config.get("Account","Phone")
        return Username,Password,Phone

    #读取网站地址
    def web_Site(self):
        URL = config.get("Linkage","URL")
        return  URL

    #读取配置文件的邮件配置
    def emailConfig(self):
        Subject = config.get("Email","Subject")
        Server = config.get("Email","Server")
        Port = config.get("Email","Port")
        Sender = config.get("Email","Sender")
        Password = config.get("Email","Password")
        Receicer = config.get("Email","Receicer")
        return Subject,Server,Port,Sender,Password,Receicer
