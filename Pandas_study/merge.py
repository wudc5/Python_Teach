#coding=utf-8
import pandas as pd
import numpy as np

#创建两个DataFrame
dates = pd.date_range('20170101', periods=3)
left_df = pd.DataFrame(np.arange(12).reshape(3, 4), index=dates, columns=['A', 'B', 'C', 'D'])
left_df['key'] = ['001', '002', '003']
print "left_df: ", left_df

right_df = pd.DataFrame(np.random.randn(3, 4), index=pd.date_range('20170102', periods=3), columns=['B', 'C', 'D', 'E'])
right_df['key'] = ['002', '003', '004']
print "right_df: ", right_df

#how: inner, outer, left, right

res1 = pd.merge(left_df, right_df, on='key') #默认是inner
print "res1: ", res1

res2 = pd.merge(left_df, right_df, on='key', how="outer")
print "res2: ", res2

res3 = pd.merge(left_df, right_df, on='key', how="left")
print "res3: ", res3

res4 = pd.merge(left_df, right_df, on='key', how="right")
print "res4: ", res4