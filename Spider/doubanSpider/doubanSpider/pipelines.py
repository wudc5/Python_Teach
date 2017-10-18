# -*- coding: utf-8 -*-
import csv
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanspiderPipeline(object):
    def __init__(self):
        self.file = open('doubannote.csv','a')
    def process_item(self, item, spider):
        open_file_object = csv.writer(self.file)
        open_file_object.writerow([item["notename"], item["notecontent"]])
        open_file_object.close()
        #line=json.dumps(dict(item))+"\n"
        #self.file.write(line.decode('unicode_escape'))
        return item
