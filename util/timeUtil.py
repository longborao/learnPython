# encoding:utf-8
import time,datetime

def getTimestamp(d=None):
    if d is None:
        d = datetime.datetime.now()
        print d
    return time.mktime(d.timetuple())
if __name__ == "__main__":
    print getTimestamp()