# encoding:utf-8
"""
@author:
@time:
@desc: 用例执行完成后，发进行通知送邮件通知
"""

import smtplib
import settings
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

class SendEmail:
    def __init__(self,fromaddr,password,toaddrs):
        self.fromaddr = fromaddr
        self.password = password
        self.toaddrs = toaddrs

    def send_email(self):
        """
        发送邮件
        :return:
        """
        content = 'TestCase excute finish ! If the attachment, please check aliyun_test/data/aliyun_test_case.xlsx'
        textApart = MIMEText(content)

        attch_file = settings.PROJECT_PATH + 'data/aliyun_test_case.xlsx'
        pdfApart = MIMEApplication(open(attch_file, 'rb').read())
        pdfApart.add_header('Content-Disposition', 'attachment', filename=attch_file)

        mime = MIMEMultipart()
        mime.attach(textApart)
        mime.attach(pdfApart)
        mime['Subject'] = '用例执行完成通知邮件'

        try:
            server = smtplib.SMTP('smtp.qq.com')
            server.login(self.fromaddr,self.password)
            server.sendmail(self.fromaddr, self.toaddrs, mime.as_string())
            print('Send email success !')
            server.quit()
        except smtplib.SMTPException as e:
            print('error:',e) #打印错误

