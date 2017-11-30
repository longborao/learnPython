# -*- coding: utf-8 -*-

import socket
import threading,time
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('127.0.0.1',8888))
# s.listen(5)
# print 'wait for connection...'
# def tcplink(sock,addr):
#     print 'accept new connection from %s：' % addr
#     s.send("welcome!")
#     while True:
#         data=sock.recv(1024)
#         time.sleep(1)
#         if data=='exit' or not data:
#             break
#         sock.send('hello,%s!' %data)
#     sock.close()
#     print 'connection from %s:%s close.' %addr
# while True:
#     sock,addr=s.accept()
#     t=threading.Thread(target=tcplink,args=(sock,addr))
#     t.start()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1',9999))
s.listen(5)

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
