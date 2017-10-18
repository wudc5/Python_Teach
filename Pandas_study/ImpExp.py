#coding=utf-8
import pandas as pd
import MySQLdb
from sqlalchemy import create_engine

#读取文件
filepath = "/home/hadoop/下载/data.xlsx"
df = pd.read_excel(filepath, header=0, sep="|")
# data=pd.read_excel("data.xlsx",index_col=None,header=0)
df.columns=['1','2','3','4']
print df['4']
i = 1
for data in df['4']:
    with open("data.txt", 'a') as wp:
        wp.write(str(i)+"|"+data+"\n")
        wp.close()
    print data
    i+=1

# #存储
# save_filepath = "personas.txt"
# df.to_csv(save_filepath, header=None, index=None, sep="|")
#
# #读取mysql
# sql = "select * from antiaddiction"
# conn = MySQLdb.connect(host='localhost', user='root', passwd='123456', db='lottery')
# df = pd.read_sql(sql, con=conn)
# print df
#
# #存入mysql
# mysql_engine = create_engine("mysql+mysqldb://root:123456@localhost:3306/lottery", echo=True)
# df.to_sql(name='tb_name', con=mysql_engine, if_exists='append', index=False)