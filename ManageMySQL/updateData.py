#coding=utf-8
# -*- coding: UTF-8 -*-
import MySQLdb
# 打开数据库连接
db = MySQLdb.connect(host='localhost', user='root',passwd='123456', db='lottery',port=3306)
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# SQL 更新语句
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
   # 执行SQL语句
cursor.execute(sql)
   # 提交到数据库执行
db.commit()
db.close()
