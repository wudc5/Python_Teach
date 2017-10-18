# coding: utf-8

import csv

# 写入
# csvfile = file('csv_test.csv', 'wb')
# writer = csv.writer(csvfile)
# writer.writerow(['姓名', '年龄', '电话'])
#
# data = [
#     ('小河', '25', '1234567'),
#     ('小芳', '18', '789456')
# ]
# writer.writerows(data)
#
# csvfile.close()

# 读取
csvfile = open('csv_test.csv', 'rb')
reader = csv.reader(csvfile)

for line in reader:
    print line

csvfile.close()
