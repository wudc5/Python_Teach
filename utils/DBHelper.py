#coding=utf-8

import MySQLdb

 # 从mysql取数据
def getDBdata(sql, host, user, passwd, db):
    conn = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db, charset='utf8')
    cur = conn.cursor()
    cur.execute('SET NAMES UTF8')
    conn.commit()
    oper = cur.execute(sql)
    data = cur.fetchmany(oper)
    cur.close()
    return data

# 插入、更新、删除数据
def managerDBData(sql_insert, host, user, passwd, db):
    conn = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db, charset='utf8')
    cur = conn.cursor()
    cur.execute('SET NAMES UTF8')
    conn.commit()
    cur.execute(sql_insert)
    conn.commit()
    cur.close()

# sql = "delete from personas where id='5'"
# managerDBData(sql, 'localhost', 'root', '123456', 'lottery')

# get data
sql_getdata = "select * from personas limit 10"
data_resultset = getDBdata(sql_getdata, host='localhost', user="root", passwd='123456', db='lottery')
# for data in data_resultset:
#     print data[0],data[2]
