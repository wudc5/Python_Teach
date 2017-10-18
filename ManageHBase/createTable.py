#coding=utf-8
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from hbase import Hbase
from hbase.ttypes import *

transport = TSocket.TSocket('118.190.159.190', 9090)
transport = TTransport.TBufferedTransport(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport)

client = Hbase.Client(protocol)
transport.open()

content1 = ColumnDescriptor(name='f1:', maxVersions=1)
content2 = ColumnDescriptor(name='f2:', maxVersions=1)
content3 = ColumnDescriptor(name='f3:', maxVersions=1)
content4 = ColumnDescriptor(name='f4:', maxVersions=1)
client.createTable('test0623', [content1, content2, content3, content4])

print client.getTableNames()
# client.scannerOpenWithStop()