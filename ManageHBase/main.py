#coding=utf-8
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from hbase import Hbase
from hbase.ttypes import *

class HBaseHelper:
    def __init__(self, client):
        self.client = client
    def getAllTableName(self):
        return self.client.getTableNames()
    def createTable(self, tname, contents):
        self.client.createTable(tname, contents)
    def deleteTable(self, tname):
        self.client.disableTable(tname)
        self.client.deleteTable(tname)
    def insertTable(self, tname, row, mutations):
        self.client.mutateRow(tname, row, mutations)
    def getOneRowData(self, tname, rowkey):
        return self.client.getRow(tname, rowkey)
    def getMoreRowData(self, tname, startRow, columns):
        return self.client.scannerOpen(tableName=tname, startRow=startRow, columns=columns)

if __name__ == "__main__":
    transport = TSocket.TSocket('118.190.159.190', 9090)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = Hbase.Client(protocol)
    transport.open()
    hbase = HBaseHelper(client)

    #get all table's name
    tnames = hbase.getAllTableName()
    print "tnames: ", tnames

    #create table
    content1 = ColumnDescriptor(name='f1:', maxVersions=1)
    content2 = ColumnDescriptor(name='f2:', maxVersions=1)
    content3 = ColumnDescriptor(name='f3:', maxVersions=1)
    content4 = ColumnDescriptor(name='f4:', maxVersions=1)
    hbase.createTable('testTable', [content1, content2, content3, content4])

    # insert data
    row = 'row-key1'
    mutations = [Mutation(column="f1:a", value="1")]
    hbase.insertTable('testTable', row, mutations)

    # get one row data
    tableName = 'testTable'
    rowKey = 'row-key1'
    result = hbase.getOneRowData(tableName, rowKey)
    print "result: ", result
    for r in result:
        print 'the row is: ', r.row
        print 'the values is: ', r.columns.get('f1:a').value

    # get some rows data
    tableName = "testTable"
    start_rowkey = "row-key1"
    columns = ['f1:a']
    result = hbase.getMoreRowData(tableName, start_rowkey, columns)
    print result

    # delete table
    del_table = "testTable"
    hbase.deleteTable(del_table)




