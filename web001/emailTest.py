#!/user/bin/python
import smtplib
from email.mime.text import MIMEText
from email.header import Header

subject = 'email test'
message = 'here is the message'
mail_from = 'robot@tomlucky.com'
mail_to = ['dev@linuxgg.com']
auth_user = 'robot@tomlucky.com'
auth_password = '123Jkl123'
mail_host = 'smtp.tomlucky.com'


mail_host_port = 25

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, mail_host_port)
    smtpObj.login(auth_user, auth_password)
    smtpObj.sendmail(mail_from, mail_to, message)
    print 'ok'
except smtplib.SMTPException:
    print 'Error'
