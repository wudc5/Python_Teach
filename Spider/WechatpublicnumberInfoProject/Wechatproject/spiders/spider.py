#coding: utf-8
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from Wechatproject.items import WechatprojectItem
from bs4 import BeautifulSoup
from scrapy.http import Request
import pandas as pd
import numpy as np
import xlrd
from lxml import etree
import requests
class WechatSpider(BaseSpider):
    #############################################################################################
    '''微信搜索程序'''
    name = "Wechatproject"
    data=pd.read_excel("data.xlsx",index_col=None,header=0)
    data.columns=['1','2','3','4']

    # def start_requests(self):
    #     headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36'}
    #     print 'here'*10
    #     yield Request('http://weixin.sogou.com/weixin?type=1&s_from=input&query=shenzhengig',headers=headers,callback=self.parse)

    start_urls = []
    print 'len(data)',len(data['4'])
    print "data['4'][0]:",data['4'][0]
    i=0
    for weixinid in data['4']:
        if weixinid is not None and len(weixinid) > 0:
            print 'weixinid:',weixinid
            start_urls.append("http://weixin.sogou.com/weixin?type=1&query=%s&page=1" % weixinid)

    def parse(self, response):
        print "url: ", response.url
        print "parse: ", response.body
        sel = Selector(response)
        next_url = sel.xpath('//*[@id="sogou_vr_11002301_box_0"]/div/div[2]/p[1]/a/@href').extract()[0]
        print "next_url: ", next_url
        item = WechatprojectItem()
        #username = site.xpath('div[@class="txt-box"]/h3/em/text()').extract() # 其中在item.py中定义了title = Field()
        #item["username"]="".join(username)
        # link = site.xpath("@href").extract() # 其中在item.py中定义了link = Field()
        item["link"] = next_url # 其中在item.py中定义了link = Field()
        # next_url = item["link"]
        print "next_url: ", next_url
        yield Request(url=next_url, meta={"item":item}, callback=self.parse2) ## 抓取当前页数和二级页面数据

    def parse2(self, response):
        print "parse2: ", response.body
        # soup = BeautifulSoup(response.body)
        # weixinnametag=soup.find("strong",attrs={"class":"profile_nickname"})
        # weixinname=weixinnametag.get_text()
        # print "weixinname:",weixinname
        # introtag=soup.find("div",attrs={"class":"profile_desc_value"})
        # intro ="".join(introtag.get_text())
        #
        # #content='haha'
        # # print content
        # # item = WechatprojectItem()
        # item = response.meta['item']
        # item["username"]=weixinname
        # item["intro"] =intro
        # return item
