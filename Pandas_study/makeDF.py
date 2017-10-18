#coding=utf-8
import pandas as pd
import numpy as np

dic = {"A": 1.,
       "B": pd.Timestamp('20130102'),
       "C": pd.Series(1, index=range(4), dtype='float32'),
       "D": np.array([3]*4, dtype="int32"),
       "E": pd.Categorical(["test", "train", "test", "train"]),  #Pandas_study Categoricals有效地编码了包含大量重复文本的数据
       "F": "foo"}

df = pd.DataFrame(dic)
print "df: ", df

dates = pd.date_range('20170101', periods=6)
df1 = pd.DataFrame(np.arange(24).reshape(6, 4), index=dates, columns=["A", "B", "C", "D"])
print "df1: ", df1

#按照行索引和列索引的大小排序， axis=1表示按照columns名称排序,axis=0则按照index大小排序
df2 = df1.sort_index(axis=1, ascending=True)
print "df2: ", df2

#按照value排序, 默认axis=0，代表上下方向排序, ascending=False 指降序
df3 = df1.sort_values(by="C", ascending=False)
print "df3: ", df3

# axis=1代表左右方向排序
df4 = df1.sort_values(axis=1, by="20170103", ascending=False)
print "df4: ", df4
