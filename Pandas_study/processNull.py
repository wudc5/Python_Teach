#coding=utf-8
import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.arange(24).reshape(6, 4))
df1.iloc[3, 2] = np.nan
print df1

#填充0
df2 = df1.fillna(value=0)
print df2

#删除包含空值的行列, axis=0 代表行， axis=1代表列
#how= ['any', 'all']
df3 = df1.dropna(axis=0, how='any')
print df3


