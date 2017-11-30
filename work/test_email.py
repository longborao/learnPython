# -*- coding: utf-8 -*-

import sys
import os

import re
from copy import deepcopy

from ftplib import FTP
import datetime
import string
import time, datetime, calendar
import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders


# print except info
def printException():
    errmsg = " ".join((str(sys.exc_info()[0]), str(sys.exc_info()[1]), str(sys.exc_info()[2].tb_lineno)))
    print errmsg


class SendmailJob(object):
    def __init__(self, mailinfo=None):
        self.fro = mailinfo['fro']
        self.to = mailinfo['to']
        # self.pwd = '!!!'
        self.pwd = mailinfo['pwd']
        self.subject = mailinfo['subject']
        self.text = mailinfo['text']
        self.files = mailinfo['files']
        self.server = mailinfo['server']
        self.server_port = mailinfo['server_port']
        try:
            pass
        except:
            self.fro = '@163.com'
            self.to = ['']
            self.subject = 'error'
            self.text = 'test'
            self.files = ['aaa.cfg']
            self.server = 'smtp.163.com'
            self.server_port = 25

    def __call__(self):
        # def sendHtmlMail(fro, to, subject, text, files,server, server_port = 25 ):

        # global part1,part2 ,part3

        COMMASPACE = ','
        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg["Accept-Language"] = "zh-CN"
        msg["Accept-Charset"] = "ISO-8859-1,utf-8"
        msg['Subject'] = self.subject
        msg['From'] = self.fro
        msg['To'] = COMMASPACE.join(self.to)
        # msg['To']=self.to



        # Create the body of the message (a plain-text and an HTML version).

        # Record the MIME types of both parts - text/plain and text/html.
        part1 = MIMEText(self.text, 'plain', "utf-8")
        part2 = MIMEText(self.text, 'html', "utf-8")

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        msg.attach(part1)
        msg.attach(part2)

        if len(self.files) > 0:
            part3 = MIMEBase('application', "octet-stream")
            for file in self.files:
                part3.set_charset('utf-8')
                part3.set_payload(open((file), "rb").read(), 'utf-8')
                encoders.encode_base64(part3)
                part3.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file))
                # %Header(os.path.basename(file),'utf-8'))
            msg.attach(part3)

        # Send the message via local SMTP server.
        RESENDCOUNT = 1
        for icount in range(RESENDCOUNT):
            try:
                s = smtplib.SMTP(self.server, self.server_port)
                print 'login use ', self.fro, self.pwd
                s.starttls()
                s.login(self.fro, self.pwd)
                s.sendmail(self.fro, self.to, msg.as_string())
                s.quit()
                return True
                pass
            except:
                printException()
                print datetime.datetime.now(), 'send failure ,resend after 5 seconds '
                time.sleep(5)
                continue
        return False


def file_down(host, username, password):
    today = datetime.date.today()
    delta_days = datetime.timedelta(1)
    yesterday = today - delta_days
    date_format = '%Y-%m-%d'
    yesterday = yesterday.strftime(date_format)
    print 'create the ftp'
    ftp = FTP(host)
    # ftp.set_debuglevel(2)
    ftp.login(username, password)
    print 'current directory:', ftp.pwd()
    print 'change dir'
    ftp.cwd('rlb/logs/')
    print 'current dir:', ftp.pwd()
    fileList = ftp.nlst()
    ftp.retrlines('LIST')
    filename = 'E:\\raolongbo\\python\\pyhonScript\\file\\' + yesterday + '.log'
    if os.path.exists(filename):
        pass
    else:
        file_handler = open(filename, 'wb').write
        ftp.retrbinary('RETR rlb.log', file_handler, 1024)
    return ftp


def read_file(path):
    linux_type_dict = dict()
    with open(path, 'rb') as f:
        linux_type_list = f.read().strip().split('\n')

    if linux_type_list is not None:
        linux_type_list_to_purge = deepcopy(linux_type_list)
        for member in linux_type_list_to_purge:
            if re.search('^#+.*', member) is not None:
                member_to_purge = member
                linux_type_list.remove(member_to_purge)
        for member in linux_type_list:
            sub_member = member.split('=')
            linux_type_dict[sub_member[0]] = sub_member[1].strip('"')
        print linux_type_dict
        print linux_type_dict['callnewusers']
        return linux_type_dict

def html_text():
    filePath='D:\\Desktop\\test.txt'
    dict=read_file(filePath)
    for key in dict:
        print dict[key]
    today = datetime.date.today()
    daylist=[]
    for i in range(7):
        i=i+2
        delta_days = datetime.timedelta(i)
        daylist.append((today-delta_days).strftime('%Y-%m-%d'))
    print daylist[0]
    htmlstr = """
    <html>
	<head>
	测试
	</head>
    <body>
		<table style="width:600px;font-family: verdana,arial,sans-serif;font-size:11px;color:#333333;border-width: 1px;border-color: #666666;border-collapse: collapse;">

                <tr>
                    <th align="center" style="width:150px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #dedede;">类型</th>
                    <th align="center" style="width:150px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #dedede;">当日新增</th>
					<th align="center" style="width:150px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #dedede;">当日总数</th>
					<th align="center" style="width:150px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #dedede;">历史总数</th>
                </tr>

                <tr>
                    <td align="center" style="width:150px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">短信表(用户数)</td>
                    <td align="center" style="width:150px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">{}</td>
					<td align="center" style="width:150px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">—————</td>
					<td align="center" style="width:150px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">{}</td>
                </tr>

                <tr>
                    <td align="center" style="width:150px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">呼叫表(用户数)</td>
                    <td align="center" style="width:150px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">{}</td>
					<td align="center" style="width:150px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">—————</td>
					<td align="center" style="width:150px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">{}</td>
                </tr>
		</table>
		</br>
		最近七天数据统计
		<table style="width:600px;font-family: verdana,arial,sans-serif;font-size:11px;color:#333333;border-width: 1px;border-color: #666666;border-collapse: collapse;">

                <tr>
                    <th align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #dedede;">日期</th>
                    <th align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #dedede;">短信表新增用户数</th>
					<th align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #dedede;">短信表当日总用户数</th>
					<th align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #dedede;">呼叫表新增用户数</th>
                    <th align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #dedede;">呼叫表当日总用户数</th>
                    <th align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #dedede;">db1大小</th>

                </tr>

                <tr>
                    <td align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">{}</td>
                    <td align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">111111111</td>
					<td align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">999999999</td>
					<td align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">-</td>
                    <td align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">-</td>
					<td align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">-</td>
                </tr>

                <tr>
                    <td align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">{}</td>
                    <td align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">-</td>
					<td align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">-</td>
					<td align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">-</td>
					<td align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">-</td>
					<td align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">-</td>
				</tr>

				<tr>
                    <td align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">{}</td>
                    <td align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">-</td>
					<td align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">-</td>
					<td align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">-</td>
					<td align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">-</td>
					<td align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">-</td>
				</tr>

				<tr>
                    <td align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">{}</td>
                    <td align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">-</td>
					<td align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">-</td>
					<td align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">-</td>
					<td align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">-</td>
					<td align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">-</td>
				</tr>

				<tr>
                    <td align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">{}</td>
                    <td align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">-</td>
					<td align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">-</td>
					<td align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">-</td>
					<td align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">-</td>
					<td align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">-</td>
				</tr>、

				<tr>
                    <td align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">{}</td>
                    <td align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">-</td>
					<td align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">-</td>
					<td align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">-</td>
					<td align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">-</td>
					<td align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">-</td>
				</tr>

				<tr>
                    <td align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">{}</td>
                    <td align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">-</td>
					<td align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">-</td>
					<td align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">-</td>
					<td align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">-</td>
					<td align="center" style="width:100px;border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;">-</td>
				</tr>
		</table>
	</body>
    </html>
    """.format(dict['smsnewusers'],dict['smstotalusers'],dict['callnewusers'],dict['calltotalusers'],daylist[6],daylist[5],daylist[4],daylist[3],daylist[2],daylist[1],daylist[0])
    #print htmlstr
    return htmlstr


if __name__ == "__main__":
    # test get mail entry from redis queue ,and retuan sending mail info

    # download logs from the ftp
    #ftp = file_down('172.10.1.102', 'ftpde', 'ftpde')
    #ftp.quit()

    # get the data from  log
    print datetime.datetime.now(), 'begin get mail info to send '
    today = datetime.date.today()
    delta_days = datetime.timedelta(1)
    yesterday = today - delta_days
    date_format = '%Y-%m-%d'
    yesterday = yesterday.strftime(date_format)
    #filePath = 'E:\\raolongbo\\python\\pyhonScript\\file\\' + yesterday + '.log'
    filePath ='D:\\Desktop\\test.txt'
    str_parm = read_file(filePath)

    mailparam = {}
    mailparam['fro'] = '962265052@qq.com'
    mailparam['to'] = ['714759009@qq.com']
    mailparam['pwd'] = 'vtgsjvktuzylbdhi'
    mailparam['subject'] = yesterday + '数据统计'
    #mailparam['text'] = '<html><body><p>' + str_parm + '</p></body></html>'
    mailparam['text'] = html_text()
    # mailparam['text'] = '<html><body><p>hello<br/>world</p></body></html>'
    mailparam['files'] = []
    mailparam['server'] = 'smtp.qq.com'
    mailparam['server_port'] = 25
    mail = SendmailJob(mailparam)
    sendstatus = mail.__call__()
    if sendstatus:
        print datetime.datetime.now(), 'sucess to send mail to ', mailparam['to']
        try:
            print datetime.datetime.now(), 'sucess to send mail to ', mailparam['to'], " mail title is ", mailparam[
                "subject"]
        except:
            pass
    else:
        print datetime.datetime.now(), 'error to send mail to ', mailparam['to']
    del mailparam
    del mail

    print datetime.datetime.now(), 'end send mail info to reciever'
