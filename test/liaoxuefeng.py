# -*- coding: utf-8 -*-

#1:输入
#name=raw_input("please input your name:")
#2:输出
#print "hello,",name
#3:以：结尾代表一个代码块
#1.23x109 浮点数 =1.23e^9
#4:转义字符\     \" \n表示换行, \t表示制表符,\\表示\，用%%来表示一个%
#print "\'hello\'"
#5:不转义r''
#print r'\'hello\''
#6:多行换行''''''
# print '''line1
# line3'''
#7:逻辑运算 and or not
#8：空值用 None 表示
#9：全部大写字母表示常量
#10：Unicode字符串转换成utf-8 u'abc'.encode('utf-8'),utf-8转换成Unicode'abc'.decode('utf-8')
#11:如果你使用Notepad++进行编辑，除了要加上# -*- coding: utf-8 -*-外，中文字符串必须是Unicode字符串(u"你好")
#12：格式化 占位符 %s %d %f 浮点数 %x 十六进制  格式化整数和浮点数还可以指定是否补0和整数与小数的位数
#print "hello,%s,you have %d" %('raolongbo',100)
#print '%.2f' % 3.1415
#print '%d0%d' %(1,2)
#13:list:增删改查,用中括号表示，查找和插入的时间随着元素的增加而增加；占用空间小，浪费内存很少。
# a=[1,2,'hhh','ll']
# a.insert(1,5)   #插入第一个位置的值
# a.append('hhhh')  #从末尾添加一个元素
# a.pop(1)  #删除第一个
# a.pop()     #删除最后一个
# print a[1]
# print a[-1]
#14：tuple:用小括号表示，定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来，所以没有append和insert
#15：if 后面必须要有：，int（）将str转换成整数
#16：循环for x in list or tuple: range(10),生成一个整数序列，while循环
#17：dictionary，键值对，用{}表示
# d={'rao':2,'long':3,'bo':2}
# print d['rao']  #获取key为'rao'的元素
# print d.get('ra5',-1) #判断某一元素是否存在
# d.pop('rao')  #删除
# print d
#18：set，在set中，没有重复的key。会过滤掉所有重复的元素
# s=set([1,1,2,5,5,4])
# s.add(6)
# s.remove(1)
# print s
#19:定义函数，def function(): 导入函数，from  pyfilename import functionname,isinstance()对参数类型检查,
# 函数可以同时返回多个值，但其实就是一个tuple。
# def a():
#      pass  #空函数
# x=1
# print isinstance(x,(int,float))
#20:函数参数：默认参数，可变参数（参数前面*）：参数个数是可变的；关键字参数：关键字参数允许你传入0个或任意个含参数名的参数
#命名关键字:参数必须传入参数名,限制关键字参数的名字
#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
# def a(a,b=1):
#     print a     #b就是默认为1，可以修改b的值
# def b(*args):
#     print args   #可变参数在函数调用时自动组装为一个tuple
# b(1,2,3)
# def c(city,**kwargs): #关键字参数
#     print city
#21：切片,截取list中特定段的元素
# l=[1,2,3]
# print l[0:2] #从第0到第二个元素，不包含第二个
# print l[::1] #没隔一个截取一个元素
#22：迭代
# from collections import Iterable
# print isinstance("abc",Iterable)  #判断是否可迭代
# l=["a",22,'dd']
# for i,value in enumerate(l):   #enumerate函数将list变成索引-元素对
#     print i,value
#23：列表生成式：可以快速生成list
# print [x*x for x in list(range(1,10)) if x%2==0]
#24:generator生成器：这种一边循环一边计算的机制,不用计算全部的list,节省空间
#如果一个函数定义中包含yield关键字，就是一个generator
#变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
# g=(x*x for x in list(range(1,10)) if x%2==0)
# print next(g)
# for i in g:
#     print i
#25：迭代器：
# 可以使用isinstance()判断一个对象是否是Iterable对象：凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象
# Python的for循环本质上就是通过不断调用next()函数实现的
#26：map函数：map()函数接收两个参数，一个是函数，一个是序列
# def f(x):
#     return x*x
# print map(f,[1,2,3])
#27:reduce把结果继续和序列的下一个元素做累积计算
# def fn(x,y):
#     return x*10+y
# print reduce(fn,[1,3,5,6])
#28:filter:把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
# def od(s):
#     return s and s.strip()
# print filter(od,["","ss","","s"])
#29:sorted:对list进行排序,默认是从小到大
# def reversed(x,y):
#     if x>y:
#         return -1
#     if x<y:
#         return 1
#     return 0
# print sorted([222,444,33,44,5],reversed)
#30：匿名函数：关键字lambda表示匿名函数，冒号前面的x表示函数参数。
#print map(lambda x:x*x,[1,2,3])
#31:装饰器
#32：偏函数：functools模块，当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，
# 这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
#print int('1234',base=8) #转换成8进制
#33：模块：一个.py文件就称之为一个模块（Module）
#每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。
#别名：import cStringIO as StringIO  优先引入cStringIO 如果不支持 则使用StringIO
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ' a test module '               #模块的注释
#
# __author__ = 'Michael Liao'
#
# import sys
#
# def test():
#     args = sys.argv      #sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称
#     if len(args)==1:
#         print 'Hello, world!'
#     elif len(args)==2:
#         print 'Hello, %s!' % args[1]
#     else:
#         print 'Too many arguments!'
#
# if __name__=='__main__':
#     test()
#34：第三方库。 pip install library_name
#35:__future__: Python提供了__future__模块，把下一个新版本的特性导入到当前版本
#from __future__ import unicode_literals
#36:面向对象：面向对象的设计思想是抽象出Class，根据Class创建Instance。
#37：类和实例
# class Student(object):        #()里是继承的类
#     def __init__(self,name,age): #构造函数
#         self.name=name
#         self.age=age
#     def printname(self):
#         print self.name
# stu=Student('d',2)
# stu.printname()
# stu._Student__name    #可以访问私有变量，访问私有变量
#38:访问限制
#private 属性的名称前加上两个下划线__
#特殊变量 变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，不是私有变量，可以被外部访问
#单下划线开头的变量：虽然我可以被访问，但是，请把我视为私有变量，不要随意访问
#38：继承和多态：继承可以把父类的所有功能都直接拿过来。多态：可以在运行时动态的绑定实例
#39:获取对象信息
#print type(111) 判断对象是什么类型
# isinstance('a',str)  判断对象是否是哪种类型
# dir('a')获得一个对象的所有属性和方法
#40:动态给实例或者类绑定属性和方法,__slots__限制能添加的类的属性
# class Student(object):
#     __slots__=("age","name")  #只能绑定age和name两个属性
#     pass
# s=Student()
# def setName(self,name):
#     self.name=name
#     print name
# from types import MethodType
# s.setName = MethodType(setName, s, Student)
# s.age=5
# print s.age
# s.setName('rao')
#41:@property:把方法变成属性，加上property之后
# class Student(object):
#
#     @property
#     def birth(self):
#         return self._birth
#
#     @birth.setter
#     def birth(self, value):
#         self._birth = value
#
#     @property
#     def age(self):
#         return 2014 - self._birth
#42：Python支持多继承
# class Person():
#     pass
# class Family():
#     pass
# class Student(Person,Family):
#     pass
#43:python特殊变量和函数名,可以帮我们定制类，比如：__slots__,__len__,__str__，__iter__,__getitem__,__getattr__,__call__
#通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。
#44:使用元类：type()函数既可以返回一个对象的类型，又可以创建出新的类型，metaclass，直译为元类
#45：异常处理：如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获,raise关键字抛出错误
# try:
#     pass
# except:
#     pass
# finally:
#     pass
#46:调试：assert 断言 ，logging
# import logging
# logging.basicConfig(level=logging.INFO)
#pdb.set_trace()设置断点 自带pdb调试工具
#47：单元测试：测试类继承unittest.TestCase
#48：文档注释：doctest 运行文档注释中的代码
#49：文件读写：try:  要读取非ASCII编码的文本文件，就必须以二进制模式打开，再解码。
# try:
#     f = open('/path/to/file', 'r')
#     print f.read()
# finally:
#     if f:
#         f.close()
#
# with open("filepath","rb") as f:
#     pass
#encode()转码  decode（）
#50：对目录操作：os模块封装了操作系统的目录和文件操作，要注意这些函数有的在os模块中，有的在os.path模块中。
# import os
# # 查看当前目录的绝对路径:
# print os.path.abspath('.')
# # 首先把新目录的完整路径表示出来,在当前目录建立一个目录:
# os.path.join('/Users/michael', 'testdir')
# # 然后创建一个目录:
# os.mkdir('/Users/michael/testdir')
# # 删掉一个目录:
# os.rmdir('/Users/michael/testdir')
#51：序列化：序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。pickling，
# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling
#dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。
# 用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：。
# import pickle
# import json
# class Student(object):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def hello(self):
#         print "hello"
#
# def student2dict(std):
#         return {
#             'name': std.name,
#             'age': std.age
#         }
# student=Student("san",3)
# pickle.dumps(student)
# with open("D:/Desktop/test1.txt","wb") as f:
#     pickle.dump(student,f)
# with open("D:/Desktop/test1.txt","rb") as f:
#     (pickle.load(f)).hello()
# d = dict(name='Bob', age=20, score=88)
# print json.dumps(d)
# print json.loads(json.dumps(d))  #json反序列化得到的字符串是Unicode编码格式的
# print json.dumps(student,default=student2dict)   #Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON。
#52:进程和线程  multiprocessing模块,封装了
#启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行
#Python的多线程对IO操作可以并发，对CPU计算不行
#锁 lock = threading.Lock()  lock.acquire() lock.release()
#一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。
# Python的multiprocessing模块不但支持多进程，其中managers子模块还支持把多进程分布到多台机器上。
# 一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信。由于managers模块封装很好，不必了解网络通信的细节，
# 就可以很容易地编写分布式多进程程序。
# from multiprocessing import Pool,Process
# import os, time, random
#
# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))
#
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')
# import time,threading
# # 新线程执行的代码:
# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)
#
# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)

#53:正则表达式  re模块
# import re
# test='2017-05-10'
# if re.match(r'^\d{4}\-\d{2}\-\d{2}$',test):
#     print "date"
# else:
#     print 'fail'
# list= re.split(r'\s+', 'a b   c')
# print list[0]
# m=re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')  #分组提取子串
# print m.group(1)

#54：datetime模块
#str转换datetime：
#datetime转换str：
#timedelta（类）算出前几天或者后几天的时刻now + timedelta(days=2, hours=12)

#55:collections模块
#namedtuple：很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用
# from collections import namedtuple
# point=namedtuple("point",['x','y'])#表示一个点的坐标
#deque：list按索引访问数据很快，但是插入和删除数据很慢，为了高效实现插入和删除操作的双向列表，适合用于队列和栈
#defaultdict：使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
# from collections import defaultdict
# dd = defaultdict(lambda: 'N/A')   #默认空的key返回的是‘N/A’
#OrderedDict：按顺序存储key
#Counter：计数器，比如可以统计字符串的出现的字符数

#56：base64模块
#Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。

#57：struct模块 来解决str和其他二进制数据类型的转换。

#58：hashlib模块 提供哈希算法 如md5 sha1加密等

#59：itertools模块 提供了非常有用的用于操作迭代对象的函数
#count()：会创建一个无限的迭代器，所以上述代码会打印出自然数序列，根本停不下来
#cycle()：会把传入的一个序列无限重复下去
#repeat()：负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
#chain()：可以把一组迭代对象串联起来，形成一个更大的迭代器
#groupby()：把迭代器中相邻的重复元素挑出来放在一起
#imap()：可以作用于无穷序列，并且，如果两个序列的长度不一致，以短的那个为准
#itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是迭代对象，只有用for循环迭代的时候才真正计算

#60：解析xml 操作XML有两种方法：DOM和SAX。DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。
# SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。优先选择sax模式，start_element，end_element和char_data三个事件
# 生成xml 一般采用字符串拼接的方式
# from xml.parsers.expat import ParserCreate
#
# class DefaultSaxHandler(object):
#     def start_element(self, name, attrs):
#         print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
#
#     def end_element(self, name):
#         print('sax:end_element: %s' % name)
#
#     def char_data(self, text):
#         print('sax:char_data: %s' % text)
#
# xml = r'''<?xml version="1.0"?>
# <ol>
#     <li><a href="/python">Python</a></li>
#     <li><a href="/ruby">Ruby</a></li>
# </ol>
# '''
# handler = DefaultSaxHandler()
# parser = ParserCreate()
# parser.returns_unicode = True
# parser.StartElementHandler = handler.start_element
# parser.EndElementHandler = handler.end_element
# parser.CharacterDataHandler = handler.char_data
# parser.Parse(xml)

#61：HTMLParser模块：解析HTML
# from HTMLParser import HTMLParser
# from htmlentitydefs import name2codepoint
#
# class MyHTMLParser(HTMLParser):
#
#     def handle_starttag(self, tag, attrs):
#         print('<%s>' % tag)
#
#     def handle_endtag(self, tag):
#         print('</%s>' % tag)
#
#     def handle_startendtag(self, tag, attrs):
#         print('<%s/>' % tag)
#
#     def handle_data(self, data):
#         print('data')
#
#     def handle_comment(self, data):
#         print('<!-- -->')
#
#     def handle_entityref(self, name):
#         print('&%s;' % name)
#
#     def handle_charref(self, name):
#         print('&#%s;' % name)
#
# parser = MyHTMLParser()
# parser.feed('<html><head></head><body><p>Some <a href=\"#\">html</a> tutorial...<br>END</p></body></html>')

#62：第三方类库：PIL:python imaging library:算是 python的图像处理标准库。
# PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图。比如要生成字母验证码图片。
# import Image, ImageDraw, ImageFont, ImageFilter
# import random
#
# # 随机字母:
# def rndChar():
#     return chr(random.randint(65, 90))
#
# # 随机颜色1:
# def rndColor():
#     return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
#
# # 随机颜色2:
# def rndColor2():
#     return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
#
# # 240 x 60:
# width = 60 * 4
# height = 60
# image = Image.new('RGB', (width, height), (255, 255, 255))
# # 创建Font对象:
# font = ImageFont.truetype('Arial.ttf', 36)
# # 创建Draw对象:
# draw = ImageDraw.Draw(image)
# # 填充每个像素:
# for x in range(width):
#     for y in range(height):
#         draw.point((x, y), fill=rndColor())
# # 输出文字:
# for t in range(4):
#     draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# # 模糊:
# image = image.filter(ImageFilter.BLUR)
# image.save('code.jpg', 'jpeg');

#63:GUI Python支持多种图形界面的第三方库 QT TK wxWidgets GTK
# Python自带的库是支持Tk的Tkinter，使用Tkinter，无需安装任何包，就可以直接使用。

#64：网络编程
#1：导入socket库
# import socket
# #2：创建socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #3：建立连接
# s.connect(('www.baidu.com',80))
# #4：发送请求
# s.send('GET / HTTP/1.1\r\nHost: www.baidu.com.cn\r\nConnection: close\r\n\r\n')
# #5:接受数据
# buffer=[]
# while True:
#     #每次接受的最大字节数
#     d=s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# data=''.join(buffer)
# print data
#UDP:s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  不需要建立连接，服务器绑定ip和端口，客户端直接发送数据

#65:发送和接受邮件
#1：发送邮件：SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。

#2：接收邮件：poplib模块

#66:访问数据库
#1：访问SQLite3 ：sqlite3
#2：mysql
# 导入MySQL驱动:
# import mysql.connector
# 注意把password设为你的root口令:
# conn = mysql.connector.connect(user='root', password='password', database='test', use_unicode=True)
# cursor = conn.cursor()
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# # 插入一行记录，注意MySQL的占位符是%s:
# cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
# cursor.rowcount
# # 提交事务:
# conn.commit()
# cursor.close()
# # 运行查询:
# cursor = conn.cursor()
# cursor.execute('select * from user where id = %s', ('1',))
# values = cursor.fetchall()
# # 关闭Cursor和Connection:
# cursor.close()
# conn.close()
#3：SQLAlchemy ORM框架  object-relationship-mapping 关系对象映射，ORM框架的作用就是把数据库表的一行记录与一个对象互相做自动转换。
# 导入:
# from sqlalchemy import Column, String, create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
#
# # 创建对象的基类:
# Base = declarative_base()
# # 定义User对象:
# class User(Base):
#     # 表的名字:
#     __tablename__ = 'user'
#
#     # 表的结构:
#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))
# # 初始化数据库连接:
# engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
# # 创建DBSession类型:
# DBSession = sessionmaker(bind=engine)

#67：http协议
#http格式：header和body
#http请求步骤：
# 步骤一：浏览器首先向服务器发送HTTP请求，方法：GET还是POST，GET仅请求资源，POST会附带用户数据；
# 路径：/full/url/path；
# 域名：由Host头指定：Host: www.sina.com.cn
# 以及其他相关的Header；
# 如果是POST，那么请求还包括一个Body，包含用户数据
# Content-Encoding

# 步骤2：服务器向浏览器返回HTTP响应，响应包括：
# 响应代码：200表示成功，3xx表示重定向，4xx表示客户端发送的请求有错误，5xx表示服务器端处理时发生了错误；
# 响应类型：由Content-Type指定；
# 以及其他相关的Header；
# 通常服务器的HTTP响应会携带内容，也就是有一个Body，包含响应的内容，网页的HTML源码就在Body中。

# 步骤3：如果浏览器还需要继续向服务器请求其他资源，比如图片，就再次发出HTTP请求，重复步骤1、2。
# Web采用的HTTP协议采用了非常简单的请求-响应模式，从而大大简化了开发。当我们编写一个页面时，我们只需要在HTTP请求中把HTML发送出去，
# 不需要考虑如何附带图片、视频等，浏览器如果需要请求图片和视频，它会发送另一个HTTP请求，因此，一个HTTP请求只处理一个资源。

#68：html简介 http://www.w3schools.com/

#69：WSGI：(web server gateway interface)  web服务网管接口
# 无论多么复杂的Web应用程序，入口都是一个WSGI处理函数。HTTP请求的所有输入信息都可以通过environ获得，
# HTTP响应的输出都可以通过start_response()加上函数返回值作为Body。
# 复杂的Web应用程序，光靠一个WSGI函数来处理还是太底层了，我们需要在WSGI之上再抽象出Web框架，进一步简化Web开发。
# def application(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/html')])
#     return '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')

#70：web框架: flask模块
# from flask import Flask
# from flask import request
# app = Flask(__name__)
#
# @app.route('/', methods=['GET', 'POST'])
# def home():
#     return '<h1>Home</h1>'
#
# @app.route('/signin', methods=['GET'])
# def signin_form():
#     return '''<form action="/signin" method="post">
#               <p><input name="username"></p>
#               <p><input name="password" type="password"></p>
#               <p><button type="submit">Sign In</button></p>
#               </form>'''
#
# @app.route('/signin', methods=['POST'])
# def signin():
#     # 需要从request对象读取表单内容：
#     if request.form['username']=='admin' and request.form['password']=='password':
#         return '<h3>Hello, %s!</h3>' %request.form['username']
#     return '<h3>Bad username or password.</h3>'
#
# if __name__ == '__main__':
#     app.run()

#71:模板：目的是将后台逻辑和html分离,在html中添加{{参数}}，进行显示

#72：协程：在同一个线程里可以中断一个函数跳转到另外一个函数运行（没有按顺序执行）
#优势：一：最大的优势就是协程极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，
# 因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。
#二：不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，
# 在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多。
#多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。

#73：gevent模块：第三方库，在window不保证实现。
#当一个greenlet遇到IO操作时，比如访问网络，就自动切换到其他的greenlet，等到IO操作完成，再在适当的时候切换回来继续执行。
# 由于IO操作非常耗时，经常使程序处于等待状态，有了gevent为我们自动切换协程，就保证总有greenlet在运行，而不是等待IO。

#web 开发
import mysql.connector
conn=mysql.connector.connect(user='root',password='root',database='person',host='127.0.0.1',use_unicode=True)
print conn
cursor=conn.cursor()
print cursor.execute("select * from student")
