# -*- coding: utf-8 -*-
'''
@author: luoxian
#  Created: 2017-07-19
Description: Email configuration
'''

import smtplib,time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from Lib.ReadConfig import Config

cfg = Config()
#标题
subjValue = cfg.emailConfig()[0]
#服务器
serverValue = cfg.emailConfig()[1]
#端口
portValue = cfg.emailConfig()[2]
#发送者
senderValue = cfg.emailConfig()[3]
#密码
pwdValue = cfg.emailConfig()[4]
#接受者
recValue = cfg.emailConfig()[5]

class Email():
    # 邮件配置
    def emailConfig(output):
        smtpserver = serverValue
        port = portValue
        sender = senderValue
        password = pwdValue
        receicer = [recValue]

        # 发送内容
        subject = subjValue
        msg = MIMEMultipart()
        msg['from'] = sender
        msg['to'] = ';'.join(receicer)
        msg['subject'] = subject

        txt = MIMEText(output, 'html', 'utf-8')
        msg.attach(txt)

        # 添加附件
        now = time.strftime("%Y-%m-%d %H-%M-%S")
        Report_name = now + '_TestResult.html'
        att = MIMEText(output, 'html', 'utf-8')
        att.add_header('Content-Disposition', 'attachment', filename = Report_name)
        msg.attach(att)

        # 发送邮件
        try:
            smtp = smtplib.SMTP()
            smtp.connect(smtpserver)
            smtp.login(sender, password)
        except:
            smtp = smtplib.SMTP_SSL(smtpserver, port)
            smtp.login(sender, password)

        #发送邮件
        smtp.sendmail(sender, receicer, msg.as_string())
        print("邮件发送成功！")
        smtp.quit()
