#coding=utf-8
import pandas as pd
import numpy as np

#创建一个Series
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20170101', periods=6))
# print s1

#创建两个DataFrame
dates = pd.date_range('20170101', periods=3)
df1 = pd.DataFrame(np.arange(12).reshape(3, 4), index=dates, columns=['A', 'B', 'C', 'D'])
df1['key'] = ['001', '002', '003']
print "df1: ", df1

df2 = pd.DataFrame(np.random.randn(3, 4), index=pd.date_range('20170102', periods=3), columns=['B', 'C', 'D', 'E'])
df2['key'] = ['002', '003', '004']
print "df2: ", df2

############concat 合并
#axis=0代表上下合并
res1 = pd.concat([df1, df2], axis=0)
print "res1: ", res1

#axis=1代表左右合并
res2 = pd.concat([df1, df2], axis=1)
print "res2: ", res2

#去除掉原有index
res3 = pd.concat([df1, df2], axis=0, ignore_index=True)
print "res3: ", res3

#join: inner, outer, 默认为outer
res4 = pd.concat([df1, df2], axis=0, ignore_index=True, join="inner")
print "res4: ", res4
