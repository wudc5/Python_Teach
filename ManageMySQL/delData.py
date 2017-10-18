#coding=utf-8
# -*- coding: UTF-8 -*-
import MySQLdb
# 打开数据库连接
db = MySQLdb.connect(host='localhost', user='root',passwd='123456', db='lottery',port=3306)
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# SQL 删除语句
sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
# 执行SQL语句
cursor.execute(sql)
   # 提交修改
db.commit()
# 关闭连接
db.close()
