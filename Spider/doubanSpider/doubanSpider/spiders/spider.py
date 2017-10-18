#!/usr/bin/env python
# coding=utf-8
from scrapy.spiders import Spider
from doubanSpider.items import DoubanspiderItem
from bs4 import BeautifulSoup
from scrapy.http import Request
from scrapy.selector import Selector
# from Spider.douban_login import *
from doubanSpider.settings import user_agent
import requests
# from http import cookiejar
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
class DoubanSpider(Spider):
    name = 'doubannote'
    allowed_domains = ['douban.com']
    # start_urls = ["https://www.douban.com/accounts/login"]
    # print "start_urls: ", start_urls
    # for i in range(1, 5, 1):
    #     start_urls.append('https://www.douban.com/accounts/login')
        # start_urls=['http://poj.org/problemlist?volume=2']
    def start_requests(self):
            print "user_agent: ", user_agent
            headers = user_agent
            print 'here'*10
            yield Request("https://www.douban.com/accounts/login", headers=headers, callback=self.parse)

    #    def parse(self,response):
    #    #    item=PojItem()
    #    #    item['title']='hello word'
    #    #    item['link']='www.'
    #    #    item['content']='wdcwdc'
    #    #    return item
    #        soup=BeautifulSoup(response.body)
    #        tags=soup.findAll("td",attrs={"align":"left"})
    #        print 'tags:',tags
    #        print '!'*10
    #        for tag in tags:
    #            item=PojItem()
    #            item['title']=tag.text
    #            item['link']=tag.find('a').get('href')
    #            next_url='http://poj.org/'+item['link']
    #            print next_url
    #            yield Request(url=next_url,meta={'item':item},callback=self.parse2)

    def parse(self, response):
        # print response.body
        item = DoubanspiderItem()
        url = "https://www.douban.com/accounts/login"
        data = {
            'redir': 'https://www.douban.com',
            'form_email': '',
            'form_password': ''
        }
        header = {
            'Host': 'accounts.douban.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:49.0) Gecko/20100101 Firefox/49.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://www.douban.com/accounts/login',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': '126'
        }
        data['form_email'] = "15711057804"
        data['form_password'] = "qst12345"
        s = requests.Session()
        text = s.get(url).text
        if '请输入上图中的单词' in text:  # 如果有验证码
            page = etree.HTML(text)
            img = page.xpath('//img[@id="captcha_image"]/@src')  # 取得验证码图片
            id = page.xpath('//div[@class="captcha_block"]/input[@type="hidden"]/@value')  # 取得登录必需的验证码值
            pic = requests.get(img[0])
            with open('/home/hadoop/文档/HiData/青软实训/python/PythonProject/Spider/doubanSpider/checkMa.jpg', 'wb') as f:
                for chunk in pic.iter_content(1024):
                    if chunk:
                        f.write(chunk)
            captcha = raw_input('请输入验证码:')
            print captcha
            data['captcha-solution'] = captcha
            data['captcha-id'] = id[0]
        p = s.post(url, headers=header, data=data)
        if '的帐号' in p.text:
            print('登录成功')
            print "s.cookies: ", s.cookies
            next_url = "https://www.douban.com/mine/"
            cont = s.get(next_url).text
            print "cont: ",  cont
            item = self.parse2(cont, s, item)
            return item
            # yield Request(url=next_url, meta={'item': item}, cookies=cookie, headers=user_agent, callback=self.parse2)
        else:
            print('登录失败')

            # def parse2(self,response):
            #     soup=BeautifulSoup(response.body)
            #     tag=soup.find("div",attrs={"class":"rich_media_content","id":"js_content"})
            #     content_list=[tag_i.text for tag_i in tag.findAll('p')]
            #     content="".join(content_list)
            #    # content='wdc'
            #     item=response.meta['item']
            #     item['content']=content
            #     return item

    # def parse2(self, response):
    #     # print "response.url: ", response.url
    #     # print "response.cookies: ", response.cookies
    #     print "response.body: ", response.body
    def parse2(self, htmlcontent, session, item):
        sel = etree.HTML(htmlcontent)
        # sel = Selector(htmlcontent)
        notelink = sel.xpath('//*[@id="db-usr-profile"]/div[2]/ul/li[4]/a/@href')[0]
        print "notelink:", notelink
        notehtmlcontent = session.get(notelink).text
        print "notehtmlcontent: ", notehtmlcontent
        item['notename'] = "fsdfas"
        item['notecontent'] = "fadasfad"
        return item
        # Memory_Limit = sel.xpath('//div[@class="plm"]/table/tr[1]/td[3]/text()').extract()[0]
        # print 'len(Memory_Limit)', len(Memory_Limit)
        #
        # DescriptionTag = sel.xpath('//div[@class="ptx"]')
        # print '!' * 20
        # print 'length of Des:', len(DescriptionTag)
        # Description = DescriptionTag[0].xpath('string(.)').extract()[0]
        #
        # InputTag = sel.xpath('//div[@class="ptx"]')
        # Input = InputTag[1].xpath('string(.)').extract()[0]
        #
        # OutputTag = sel.xpath('//div[@class="ptx"]')
        # Output = OutputTag[2].xpath('string(.)').extract()[0]
        #
        # Sample_InputTag = sel.xpath('//pre[@class="sio"]')
        # Sample_Input = Sample_InputTag[0].xpath('string(.)').extract()[0]
        #
        # Sample_OutputTag = sel.xpath('//pre[@class="sio"]')
        # Sample_Output = Sample_OutputTag[1].xpath('string(.)').extract()[0]
        #
        # print 'length of Sample_InputTag:', len(Sample_InputTag)
        # item = response.meta['item']
        # item['Time_Limit'] = Time_Limit
        # item['Memory_Limit'] = Memory_Limit
        # item['Description'] = Description
        # item['Input'] = Input
        # item['Output'] = Output
        #
        # item['Sample_Input'] = Sample_Input
        #
        # item['Sample_Output'] = Sample_Output
        # return item
