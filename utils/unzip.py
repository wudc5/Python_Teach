#coding=utf-8
import zipfile

path = 'nmnormaltrain/'
f = zipfile.ZipFile(path,'r')
for file in f.namelist():
    print file
    # f.extract(file,"temp/")