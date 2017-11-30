# encoding:utf-8

from sqlalchemy import create_engine,text
import pandas as pd
import  time
import re

# def read_file(inputpath,outputpath):
#     engine = create_engine('postgresql+psycopg2://raolb:raolb123q@172.10.1.2:5433/pano')
#     # sqlalchemy自带查询
#     conn=engine.connect()
#     # sql = 'select call from test.phone_md5_pure_inner_called where callmd5=:callmd5'
#     # s=text(sql)
#     # conn.excute(s,callmd5='dd').fetchall()
#     fo=open(outputpath,"wb")
#     with open(inputpath,'rb') as f:
#         while 1:
#             lines= f.readlines()
#             if not lines:
#                 break
#             i = 1
#             for line in lines:
#                 #匹配hawq对照表中的数据
#                 line=line.strip()
#                 sql = 'select call from test.phone_md5_pure_inner_called where callmd5=:callmd5 limit 1'
#                 s=text(sql)
#                 phone=conn.excute(s,callmd5=line).fetchall()
#                 print phone
#                 fo.write(s)
#                 i=i+1
#     fo.close()
# if __name__ == '__main__':
#     inputpath="D:\\Desktop\\test.txt"
#     outputpath="D:\\Desktop\\phone.txt"
#     start=time.clock()
#     read_file(inputpath,outputpath)
#     elapsed = (time.clock() - start)
#     print elapsed
s='''             call
0  10:13350187618'''
s=s.split('\n')

print (s[1].split("  "))[1]
