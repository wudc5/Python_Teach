#coding=utf-8
import pandas as pd
import numpy as np

#创建一个DataFrame
dates = pd.date_range('20170101', periods=6)
df1 = pd.DataFrame(np.arange(24).reshape(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])
df1['key'] = ['001', '002', '003', '004', '005', '006']
print "df1: "
print df1
print "df1.A: "
print df1.A
print "df1['A']: "
print df1['A']
print "df1[['A', 'C']]: "
print df1[['A', 'C']]
print "df1[0:2]: "
print df1[0:2]   #选择前两行

# select by label: loc
# loc 不能选取不连续的多行
#通过行索引名字和列索引名字选择数据：
print df1.loc['20170101']
# print df1.loc[['20170101','20170102']]

#通过索引选择某一行某些列
print df1.loc['20170101', ['A', 'C']]

# 通过loc选择不连续的多行时会报错
# print df1.loc[['20170101','20170103'], 'A':'C']

# 通过loc选择连续的多行时没有问题, 左闭右闭
print "df1.loc['20170101':'20170103', 'A':'C']: "
print df1.loc['20170101':'20170103', 'A':'C']

# select by position: iloc
print df1.iloc[0]   #选择第一行
print df1.iloc[0, [0, 2]] #选择第一行的第一、三列
print df1.iloc[[0, 2], [0, 2]] #选择第一、三行的第一、三列
print "df1.iloc[0:3, 1:4]: "  #选择连续的多行多列时，左闭右开
print df1.iloc[0:3, 1:4]

#mixed selection: ix
print df1.ix[0, 'C']   #选择第一行的‘C’列
print df1.ix[[0, 2], 'C']   #选择第一、三行的C列

print df1.ix[0:3, 0:2]  #使用位置选择连续的多行多列时左闭右开
print df1.ix[[1, 3], [0, 2]]

print df1.ix['20170101':'20170103', 'A':'C']  #使用索引名字选择连续的多行多列时左闭右闭

print df1.ix[['20170101', '20170103']]  # 使用索引名字不能选择不连续的多行！！！

print df1.ix['20170101',["A", "C"]]  # 使用索引名字可以选择不连续的多列

print df1.index
print df1.columns
print df1.values
