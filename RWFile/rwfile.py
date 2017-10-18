#coding=utf-8
import os,sys

try:
    fsock = open("test.txt", "r")
except IOError:
    print "The file don't exist, Please double check!"
    exit()
print 'The file mode is ', fsock.mode
print 'The file name is ', fsock.name
fsock.close()

#Read file

#Method 1
fsock = open("test.txt", "r")
print "method1: ", fsock.read()

#Method 2
print 'Star'+'='*30
fsock = open("test.txt", "r")
AllLines = fsock.readlines()
for EachLine in AllLines:
    print EachLine
print 'End'+'='*30
fsock.close()

#write this file
fsock = open("test.txt", "a")
fsock.write("""
#Line 1 Just for test purpose
#Line 2 Just for test purpose
#Line 3 Just for test purpose""")
fsock.write("jdfsljfdlsjdflsjfdljslkdfj")
fsock.close()


#check the file status
S1 = fsock.closed
if True == S1:
    print 'the file is closed'
else:
    print 'The file donot close'