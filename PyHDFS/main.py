#coding=utf-8
import pyhdfs
fs = pyhdfs.HdfsClient(hosts="118.190.159.190")
print fs.listdir("/")