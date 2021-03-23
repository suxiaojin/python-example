from email.mime.text import MIMEText
import smtplib


class SendEMail(object):
    def __init__(self):
        self.mail_host='smtp.126.com'
        self.mail_user='njbmkj0901@126.com'
        self.mail_pass='MLTXLIIPAKWFYGXS'
        self.sender='njbmkj0901@126.com'
        self.smtpObj=smtplib.SMTP_SSL(self.mail_host,465)
        self.smtpObj.login(self.mail_user,self.mail_pass)

    def sendmail(self,receivers,title,content):
        message=MIMEText(content,'plain','utf-8')
        message['From']='{}'.format(self.sender)
        message['To']=','.join(receivers)
        message['Subject']=title
        try:
            self.smtpObj.sendmail(self.sender,message['To'].split(','),message.as_string())
            print('mail has been send successfully.')
        except smtplib.SMTPException as e:
            print(e)

if __name__ == '__main__':
    sm=SendEMail()
    sm.sendmail(['suxiaojin928380@126.com'],'主题','测试')