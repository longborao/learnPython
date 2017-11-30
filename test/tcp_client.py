# coding: utf-8
import socket,threading
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(('127.0.0.1', 8888))
# print s.recv(1024)
# for i in ["rao","ma"]:
#     s.send(i)
#     print s.recv(1024)
# s.sent('exit')
# s.close()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 9999))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
