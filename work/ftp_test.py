# -*- coding: utf-8 -*-

# 导入ftplib扩展库
from ftplib import FTP

# 创建ftp对象实例
ftp = FTP()

# 指定IP地址和端口，连接到FTP服务，上面显示的是FTP服务器的Welcome信息
FTPIP = "121.0.0.1"
FTPPORT = 22233

USERNAME ="root"
USERPWD = "zzvPqMnO"


ftp.connect(FTPIP, FTPPORT)

# 通过账号和密码登录FTP服务器
ftp.login(USERNAME, USERPWD)

# 如果参数 pasv 为真，打开被动模式传输 (PASV MODE) ，
# 否则，如果参数 pasv 为假则关闭被动传输模式。
# 在被动模式打开的情况下，数据的传送由客户机启动，而不是由服务器开始。
# 这里要根据不同的服务器配置
ftp.set_pasv(2)

# 在FTP连接中切换当前目录
CURRTPATH = "/root/rlb/test"
ftp.cwd(CURRTPATH)

# 为准备下载到本地的文件，创建文件对象
DownLocalFilename = "test_file"
f = open(DownLocalFilename, 'wb')

# 从FTP服务器下载文件到前一步创建的文件对象，其中写对象为f.write，1024是缓冲区大小
DownRoteFilename = "test_file"
ftp.retrbinary('RETR ' + DownRoteFilename, f.write, 1024)

# 关闭下载到本地的文件
# 提醒：虽然Python可以自动关闭文件，但实践证明，如果想下载完后立即读该文件，最好关闭后重新打开一次
f.close()

# 关闭FTP客户端连接
ftp.close()