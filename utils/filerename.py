#coding=utf-8
import os
path = "E:\lingzhong\NMTech/nmnormaltrain\homework"
for file in os.listdir(path):
    if os.path.isdir(os.path.join(path,file))==True:
        # print file
        if 'python' in file or 'Python' in file:
            newname=file[7:]
            print newname
            os.rename(os.path.join(path,file),os.path.join(path,newname))
            # print file,'ok'
#        print file.split('.')[-1]