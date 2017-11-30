# encoding:utf-8

from pymongo import MongoClient
from  test import read_file
from util import timeUtil
from multiprocessing import Queue, Pool, Manager, Lock
import sys

def read_file(inputPath):
    with open(inputPath,'rb') as f:
        phone_md5_list = []
        i = 0
        for line in f:
            phone_md5=line.strip()
            phone_md5_list.append(phone_md5)
    return phone_md5_list
def queryFromMongo(list=None):
    mongo_con = MongoClient("192.168.0.238", 27017)
    table = mongo_con["panodata"]["encrypt"]
    l=[]
    filestep = len(list) / 100 + 1
    posBegin = 0
    posEnd = posBegin + filestep
    for i in filestep:
        pass

    # table.insert(read_file.read_file())
    li= list(table.find({"callmd5":{"$in":list}}))
    for i in li:
        l.append(i["_id"])

    print l
    return l
if __name__ == "__main__":

    queryFromMongo()


