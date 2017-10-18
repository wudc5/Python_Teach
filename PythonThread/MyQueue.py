#coding=utf-8
import Queue,MySQLdb
import threading
from utils.DBHelper import getDBdata
import datetime, csv
import sys
reload(sys)
sys.setdefaultencoding('utf8')

info_que = Queue.Queue(0)
start_time = datetime.datetime.now()

class MyThread(threading.Thread):
    def __init__(self, info, threadnum):
        self.info_queue = info
        self.threadnum = threadnum
        threading.Thread.__init__(self)
    def run(self):
        while True:
            if self.info_queue.qsize() > 0:
                data = self.info_queue.get()
                self.dojob(data)

        # while True:
        #     if self.peroninfo_queue.qsize() > 0:
        #         print 'length of queue:', self.peroninfo_queue.qsize()
        #         personinfo = self.peroninfo_queue.get()
        #         self.dojob(personinfo)

    def dojob(self, data):
        print data[0], data[1], data[2]
        str = "{0}|{1}|{2}\n".format(data[0],data[1], data[2])

        filepath = "dbdata.txt"
        self.writeToFile(filepath, str)

        # writeToFile()
        # personinfolist = data.split("|")
        # print "personinfolist[0]: ", personinfolist[0]
        # print "personinfolist[0]: ", personinfolist[1]
        # print "personinfolist[0]: ", personinfolist[2]
        # print "personinfolist[0]: ", personinfolist[3]
        # print "personinfolist[0]: ", personinfolist[4]

    def writetocsv(self, filename, datalist):
        with open(filename, 'ab+') as wp:
            writer = csv.writer(wp)
            writer.writerow(datalist)

    def writeToFile(self, filepath, line):
        with open(filepath, 'ab+') as wp:
            wp.write(line)
            wp.write("\n")
            wp.close()

if __name__ == '__main__':
    for i in range(5):
        MyThread(info_que, i).start()

    sql = "select * from personas limit 10"
    datalist = getDBdata(sql, host='localhost', user="root", passwd='123456', db='lottery')

    # file = open("E:\lingzhong\NMTech\data\UserBasicInfo.txt")
    num = 1
    for line in datalist:
        # line = line.strip()
        info_que.put(line)
        print num
        num += 1