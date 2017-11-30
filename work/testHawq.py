# encoding:utf-8

from sqlalchemy import create_engine,text
import pandas as pd
import  time

def read_file(inputpath,outputpath):
    # engine = create_engine('postgresql+psycopg2://raolb:raolb123q@172.10.1.2:5433/pano')
    # sqlalchemy自带查询
    # conn=engine.connect()
    # sql = 'select call from test.phone_md5_pure_inner_called where callmd5=:callmd5'
    # s=text(sql)
    # conn.excute(s,callmd5='dd').fetchall()
    fo=open(outputpath,"wb")
    with open(inputpath,'rb') as f:
        while 1:
            lines= f.readlines()
            if not lines:
                break
            i = 1
            for line in lines:
                #匹配hawq对照表中的数据
                line=line.strip()
                s='''        call
0	13006354990'''
                sql = 'select call from test.phone_md5_pure_inner_called where callmd5=\'%s\'' % (line)
                # phone=pd.read_sql(sql,mysql_engine)
                # phone=engine.con
                s=(str(i)+":"+line+'hello')
                print sql
                fo.write(s)
                i=i+1
    fo.close()
if __name__ == '__main__':
    inputpath="D:\\Desktop\\test.txt"
    outputpath="D:\\Desktop\\phone.txt"
    start=time.clock()
    read_file(inputpath,outputpath)
    elapsed = (time.clock() - start)
    print elapsed

