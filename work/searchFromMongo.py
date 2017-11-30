#encoding:utf-8

import sys,time,datetime
from pymongo import MongoClient
from multiprocessing import Queue, Pool, Manager, Lock

MONGO_HOST = "192.168.0.238"
MONGO_PORT = 27017
MONGO_DB = "panodata"
PROCESS_NUM=10

#运行时间
#输入路径
#输出路径
#转化条数
#转化成功
#转化失败
#结束时间

mongo_con = MongoClient(MONGO_HOST, MONGO_PORT)
table = mongo_con["panodata"]["encrypt"]
log_table = mongo_con["panodata"]["log"]

def read_file(inputPath):
    with open(inputPath,'rb') as f:
        phone_md5_list = []
        i = 0
        for line in f:
            phone_md5=line.strip()
            phone_md5_list.append(phone_md5)
    return phone_md5_list

def write_file(outputPath,phone_list):
    if phone_list:
        f = open(outputPath, 'wb')
        for phone in phone_list:
            f.write(phone+'\r\n')
        f.close()
    else:
        print "no transform data"

def query(processId,phone_md5_list,q):
    for phone_md5 in phone_md5_list:
        phone=table.find_one({"callmd5":phone_md5})
        q.append(phone["_id"])

def queryProcess(phone_md5_list):
    manager = Manager()
    q = manager.list()
    jobs = PROCESS_NUM
    pool = Pool(jobs)
    filestep = len(phone_md5_list) / jobs + 1
    posBegin = 0
    posEnd = posBegin + filestep
    processList = []
    #创建十个进程,item:进程id , list:每个线程处理的文件大小，q:进程公共变量,收集十个进程统计的数据
    for item in range(0, jobs):
        p = pool.apply_async(query, args=(item, phone_md5_list[posBegin:posEnd], q))
        posBegin = posEnd
        posEnd = posBegin + filestep
        processList.append(p)
    while 1:
        try:
            time.sleep(1)
            status = True
            for item in processList:
                status = status and item.ready()
            if status:
                break
        except KeyboardInterrupt:
            pool.terminate()
            pool.wait(None)
            break

    for item in processList:
        item.wait()
    pool.close()
    pool.join()
    del pool
    return q

if __name__ == "__main__":

    begin_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if len(sys.argv) < 3:
        print "error:please input two filePath args ！"
    inputPath=sys.argv[1]
    outputPath=sys.argv[2]
    # print inputPath,outputPath
    #转化总条数
    phone_md5_list=read_file(inputPath)
    # print phone_md5_list
    transform_count=len(phone_md5_list)
    #成功转化
    phone_list=queryProcess(phone_md5_list)
    # print phone_list
    transform_success_count=len(phone_list)

    transform_fail_count=transform_count-transform_success_count
    write_file(outputPath,phone_list)
    end_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data={"begin_time":begin_time,"inputPath":inputPath,"transform_count":transform_count,"transform_success_count":transform_success_count
        ,"transform_fail_count":transform_fail_count,"outputPath":outputPath,"end_time":end_time}
    log_table.insert(data)

    mongo_con.close()
