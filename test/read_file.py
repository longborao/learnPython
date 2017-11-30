#!/usr/local/bin/python2.7
# -*- encoding: utf-8 -*-
from pymongo import *

from util import timeUtil
def read_file():
    with open("D:\\Desktop\\phone_md5_680282.csv",'rb') as f:
        test = []
        i=0
        for line in f:
        # list=f.readlines()
        # for line in list:

            list=filter(None,line.strip().split(" "))
            list=list[0].split('\t')

            call=list[0]
            callmd5=list[1]

            # month=list[2]
            # day=list[3]
            s={"_id":call,"callmd5":callmd5}
            # print s
            # s={"call":call}
            test.append(s)
            # i=i+1

    return test

if __name__ == '__main__':
    
    list=read_file()
    print len(list)
