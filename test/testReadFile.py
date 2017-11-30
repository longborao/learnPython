#!/usr/local/bin/python2.7
#encoding:utf-8

def readFile():
    with open("D:\\Desktop\\test.txt",'rb') as f:
        for line in f:
            line = line.strip()
            day=line[-10:]
            month=line[-17:-10]
            callmd5=line[-49:-17]
            call=line[:-49]
            print call

if __name__ == "__main__":
    readFile()