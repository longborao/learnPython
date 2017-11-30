# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr


import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = 'raolongbo@panodata.cn'
password = 'Rlb101096'
to_addr = '714759009@qq.com'
smtp_server = 'smtp.mxhichina.com'

msg = MIMEText('hello', 'plain', 'utf-8') #纯文本文件发送
msg['From'] = _format_addr('bobo <%s>' % from_addr)  #相当于备注,如果不进行此操作，被当作陌生来信
msg['To'] = _format_addr('test <%s>' % to_addr)
msg['Subject'] = Header('hello', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
# server.starttls()
server.set_debuglevel(1)    #打印出与smtp交互的所有信息
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()