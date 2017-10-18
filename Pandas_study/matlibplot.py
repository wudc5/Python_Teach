#coding=utf-8
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#折线图
data = pd.DataFrame(np.random.randn(1000, 4), index=np.arange(1000), columns=list('ABCD'))
print "data: ", data
data = data.cumsum()  #cumsum作用：累计求和，比如一个列表是这样[1,2,3,4,5] 返回是这样[1,3,6,10,15]
data.plot()
plt.show()


# 散点图
x = data['A']
y = data['B']
u = data['C']
v = data['D']
# fig = plt.figure()
axes = plt.subplot(111)
type1 = axes.scatter(x, y, c='red')  # scatter 代表描绘散点图
type2 = axes.scatter(u, v, c='green')
type3 = axes.scatter(x, u, c='blue')
type4 = axes.scatter(y, v, c='orange')
plt.xlabel('x1')
plt.ylabel('x2')

#当我们有多个 axes时，我们如何把它们的图例放在一起
axes.legend((type1, type2, type3, type4), ('0', '1', '2', '3'), loc=1)
plt.show()
