# -*- coding: utf-8 -*-
# Author:   BinBin
# Email:    289594665@qq.com
# Time :    2017/07/27

import sys
import urllib
import requests
import scrapy
import pandas as pd
from datetime import datetime
import time
from lxml import etree
import subprocess
# from PIL import Image
# import zbar
from scrapy import Request
from scrapy.selector import Selector
from ..items import ArticleItem

reload(sys)
sys.setdefaultencoding("utf-8")

class WechatSpider(scrapy.Spider):
    name = "Wechat"
    # allowed_domains = ["weixin.sogou.com", "mp.weixin.qq.com"]
    # start_urls = ['http://weixin.sogou.com/weixin?type=1&s_from=input&query=qqchuangye']
    data = pd.read_excel("data.xlsx", index_col=None, header=0)
    data.columns = ['1', '2', '3', '4']

    # data=data.rename(columns={col_name:'new_name'})
    # data=data[data.D.notnull()]

    # def start_requests(self):
    #     headers = {
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36'}
    #     print 'here' * 10
    #     yield Request('http://weixin.sogou.com/weixin?type=1&s_from=input&query=shenzhengig', headers=headers,
    #                   callback=self.parse)

    start_urls = []
    print 'len(data)',len(data['4'])
    print "data['4'][0]:",data['4'][0]
    i=0
    for weixinid in data['4']:
        if weixinid is not None and len(weixinid)>0:
            print 'weixinid:',weixinid
            start_urls.append("http://weixin.sogou.com/weixin?type=1&query=%s&page=1" % weixinid)

    def parse(self, response):
        print "url: ", response.url
        print "parse: ", response.body
        url = response.url
        page = response.body
        s = requests.session()
        if "访问过于频繁" in page:
            header = {
                'Host': 'weixin.sogou.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:49.0) Gecko/20100101 Firefox/49.0',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Language': 'zh-CN,zh;q=0.8',
                'Accept-Encoding': 'gzip, deflate',
                # 'Referer': 'http://weixin.sogou.com',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Content-Length': '126'
            }
            page = etree.HTML(page)
            data = {'c': '', 'r': '', 'v': ''}
            r = page.xpath('//*[@id="from"]/@value')[0]
            v = '5'
            img_url = "http://weixin.sogou.com/antispider/" + page.xpath('//*[@id="seccodeImage"]/@src')[0]
            print "img_url: ", img_url
            pic = requests.get(img_url)
            with open('checkma.jpg', 'wb') as f:
                for chunk in pic.iter_content(1024):
                    if chunk:
                        f.write(chunk)
            captcha = raw_input('请输入验证码:')
            data['c'] = captcha
            data['r'] = r
            data['v'] = v
            print "data: ", data
            p = s.post(url, headers=header, data=data)
            print "p.text: ", p.text
            print "new page: ", s.get("http://weixin.sogou.com/weixin?type=1&s_from=input&query=shenzhengig").text
            # img = page.xpath('//*[@id="seccodeImage"]')
            # pic = requests.get(img[0])
        else:
            sel = Selector(response)
            next_url = sel.xpath('//*[@id="sogou_vr_11002301_box_0"]/div/div[2]/p[1]/a/@href').extract()[0]
            print "next_url: ", next_url
            # soup=BeautifulSoup(response.body)
            # tag=soup.find("div",attrs={"id":"sogou_vr_11002301_box_0"})
            # for site in sites:
            # item = WechatprojectItem()
            item = {}
            # username = site.xpath('div[@class="txt-box"]/h3/em/text()').extract() # 其中在item.py中定义了title = Field()
            # item["username"]="".join(username)
            # link = site.xpath("@href").extract() # 其中在item.py中定义了link = Field()
            item["link"] = next_url  # 其中在item.py中定义了link = Field()
            # next_url = item["link"]
            print "next_url: ", next_url
            yield Request(url=next_url, meta={"item": item}, callback=self.parse2)  ## 抓取当前页数和二级页面数据

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
    # start_urls = ['http://weixin.sogou.com/weixin?type=1&s_from=input&query=shenzhengig',
    #               'http://weixin.sogou.com/weixin?type=1&s_from=input&query=touwho2015',
    #               'http://weixin.sogou.com/weixin?type=1&s_from=input&query=fxtzvc',
    #               'http://weixin.sogou.com/weixin?type=1&s_from=input&query=CVCF2003',
    #               'http://weixin.sogou.com/weixin?type=1&s_from=input&query=healthib',
    #               'http://weixin.sogou.com/weixin?type=1&s_from=input&query=MEDCAPTAIN',
    #               'http://weixin.sogou.com/weixin?type=1&s_from=input&query=yiyaobinggou',
    #               'http://weixin.sogou.com/weixin?type=1&s_from=input&query=xyzqyysw',
    #               'http://weixin.sogou.com/weixin?type=1&s_from=input&query=WuXiAppTecChina',
    #               'http://weixin.sogou.com/weixin?type=1&s_from=input&query=iyiyaomofang',
    #               'http://weixin.sogou.com/weixin?type=1&s_from=input&query=MIC366',
    #               'http://weixin.sogou.com/weixin?type=1&s_from=input&query=geekheal_com',
    #               'http://weixin.sogou.com/weixin?type=1&s_from=input&query=MW-Group',
    #               'http://weixin.sogou.com/weixin?type=1&s_from=input&query=jihuibaoribao',
    #               'http://weixin.sogou.com/weixin?type=1&s_from=input&query=Laoqishidian-Meishan',
    #               'http://weixin.sogou.com/weixin?type=1&s_from=input&query=sdictktrust',
    #               'http://weixin.sogou.com/weixin?type=1&s_from=input&query=Trendhc',
    #               'http://weixin.sogou.com/weixin?type=1&s_from=input&query=nfsyyjjb',
    #               'http://weixin.sogou.com/weixin?type=1&s_from=input&query=Pharmaguider',
    #               'http://weixin.sogou.com/weixin?type=1&s_from=input&query=zhuanhuayixue']
    #
    # def parse(self, response):
    #     print "url:" + response.url
    #     print "response:" + response.__str__()
    #
    #     # asdgs = response.xpath('//div[@class="news-box"]/ul[@class="news-list2"]').extract()
    #     # print "asdgs:" + asdgs[0].__str__()
    #
    #     list_url = response.xpath('//div[@class="news-box"]/ul[@class="news-list2"]/li[1]/div[@class="gzh-box2"]/div[@class="img-box"]/a/@href').extract()
    #     print "list_url:" + list_url.__str__()
    #
    #     yield Request(list_url[0], callback=self.parse_list)
    #
    # def parse_list(self, response):
    #     print "next url:" + response.url
    #     print "response:" + response.__str__()
    #
    #     # asdgs = response.xpath('//html').extract()
    #     # print "asdgs:" + asdgs[0].__str__()
    #
    #     article_srcs = response.xpath("//div[@class='profile_info']/strong[@class='profile_nickname']/text()").extract()
    #     article_src = article_srcs[0].strip()
    #
    #     date = datetime.now().timetuple()
    #     dateStr = str(date.tm_year) + u'年' + str(date.tm_mon) + u'月' + str(date.tm_mday) + u'日'
    #     re_path = u'//div[@id="history"]/div[@class="weui_msg_card"]/div[contains(./text(), "{0}")]/../div[@class="weui_msg_card_bd"]/div[@class="weui_media_box appmsg"]'.format(dateStr)
    #     today_cards = response.xpath(re_path)
    #     if len(today_cards) <= 0:
    #         print "《" + article_src + "》今日没有发布内容！"
    #         return
    #
    #     for card in today_cards:
    #         article_summary = ""
    #         article_summarys = card.xpath('./div[@class="weui_media_bd"]/p[@class="weui_media_desc"]/text()').extract()
    #         for tmp in article_summarys:
    #             article_summary = article_summary + tmp
    #         article_summary = article_summary.strip()
    #         print "article_summary:" + article_summary
    #
    #         article_main_time = ""
    #         article_main_times = card.xpath('./div[@class="weui_media_bd"]/p[@class="weui_media_extra_info"]/text()').extract()
    #         for tmp in article_main_times:
    #             article_main_time = article_main_time + tmp
    #         article_main_time = article_main_time.strip()
    #         print "article_main_time:" + article_main_time
    #
    #         article_main_url = ""
    #         article_main_urls = card.xpath('./div[@class="weui_media_bd"]/h4/@hrefs').extract()
    #
    #         for tmp in article_main_urls:
    #             article_main_url = article_main_url + tmp
    #         article_main_url = article_main_url.strip()
    #         article_main_url = response.urljoin(article_main_url)
    #
    #         article_icon_style = ""
    #         article_icon_styles  = card.xpath('./span[@class="weui_media_hd"]/@style').extract()
    #         for tmp in article_icon_styles:
    #             article_icon_style = article_icon_style + tmp
    #         article_icon = article_icon_style[article_icon_style.find("url(")+4:article_icon_style.find(")")]
    #
    #         yield Request(article_main_url, callback=self.parse_item, meta={
    #             'article_icon': article_icon, 'article_src':article_src,
    #             'article_summary': article_summary,
    #         })
    #
    # def parse_item(self, response):
    #     item = ArticleItem()
    #     print "parse_item url:" + response.url
    #     print "parse_item response:" + response.__str__()
    #
    #     article_title = self.get_text(response.xpath('//h2[@id="activity-name"]/text()').extract())
    #     item["article_title"] = article_title
    #     print "article_title:" + article_title
    #
    #     if  article_title == None or article_title.strip() == "":
    #         return
    #
    #     article_icon = response.meta['article_icon']
    #     item["article_icon"] = article_icon
    #     print "article_icon:" + article_icon
    #
    #     article_summary = response.meta['article_summary']
    #     item["article_summary"] = article_summary
    #     print "article_summary:" + article_summary
    #
    #     article_src = response.meta['article_src']
    #     item["article_src"] = article_src
    #     print "article_src:" + article_src
    #
    #     article_time = self.get_text(response.xpath('//em[@id="post-date"]/text()').extract())
    #     item["article_time"] = article_time
    #     print "article_time:" + article_time
    #
    #     em = response.xpath('//div[@id="meta_content"]/em[2]')
    #     if em is not None:
    #         article_author = self.get_text(em.xpath('./text()').extract())
    #     else:
    #         article_author = article_src
    #     item["article_author"] = article_author
    #     print "article_author:" + article_author
    #
    #     # 删除超链接
    #     article_content_hrefs = response.xpath('//div[@id="js_content"]//a')
    #     for href in article_content_hrefs:
    #         try:
    #             href.root.getparent().drop_tree()
    #         except Exception, e:
    #             print "del href exception:" + e.__str__()
    #
    #     article_content_imgs = response.xpath('//div[@id="js_content"]//img')
    #     # 下载、替换微信文章中的图片
    #     for img in article_content_imgs:
    #         img_src = self.get_text(img.xpath('./@src').extract())
    #         img_data_src = self.get_text(img.xpath('./@data-src').extract())
    #
    #         if img_data_src == None or img_data_src == '':
    #             img_data_src = img_src
    #
    #         img_type = self.get_text(img.xpath('./@data-type').extract())
    #         if img_type.lower().strip() != "bmp" and img_type.lower().strip() != "jpg" and img_type.lower().strip() != "png" and img_type.lower().strip() != "jpeg":
    #             img_type = "jpg"
    #
    #         timestamp = self.get_time_stamp()
    #         abs_path = u'/Uploads/Spider/Wechat/Content/' + timestamp + '.' + img_type
    #         save_path = u'D:/UserUploadFiles勿删' + abs_path
    #
    #         if img_data_src == None or img_data_src == '':
    #             continue
    #
    #         urllib.urlretrieve(img_data_src.encode("utf8"), save_path)
    #
    #         # 判断图片是否包含二维码，如果包含则去掉
    #         # 这里用python调用zbar的exe来识别二维码，因为服务器是windows 2003，装zbar插件库各种问题。
    #         if self.check_qr_code(save_path):
    #             img.root.drop_tree()
    #         else :
    #             img.root.attrib['src'] = abs_path
    #             img.root.attrib['data-src'] = abs_path
    #
    #         # 判断图片是否包含二维码，如果包含则去掉
    #         # qr_code = self.get_qr_code(save_path)
    #         # if None != qr_code and '' != qr_code:
    #         #     img.root.drop_tree()
    #         # else :
    #         #     img.root.attrib['src'] = abs_path
    #         #     img.root.attrib['data-src'] = abs_path
    #
    #     article_content = self.get_text(response.xpath('//div[@id="js_content"]').extract())
    #     item["article_content"] = article_content
    #     # print "article_content:" + article_content
    #     article_url = response.url
    #     item["article_url"] = article_url
    #     article_type = 1
    #     item["article_type"] = article_type
    #
    #     yield  item
    #
    # def get_text(self, texts):
    #     text = ""
    #     if len(texts) > 0:
    #         for tmp in texts:
    #             text = text + tmp
    #     return text.strip()
    #
    # def get_time_stamp(self):
    #     ct = time.time()
    #     local_time = time.localtime(ct)
    #     data_head = time.strftime("%Y%m%d%H%M%S", local_time)
    #     data_secs = (ct - long(ct)) * 1000
    #     time_stamp = "%s%05d" % (data_head, data_secs)
    #     return time_stamp
    #
    # # 通过调用zbar的exe来识别二维码，前提是要先安装zbar的windows程序，找到安装目录下的zbarimg.exe
    # def check_qr_code(self, img_path):
    #     try:
    #         process = subprocess.check_output(
    #             ["C:\\Program Files (x86)\\ZBar\\bin\\zbarimg", '-q', img_path], shell=True,
    #             stderr=subprocess.STDOUT)
    #         result = process.decode('gbk')
    #         print result
    #         if result.find("QR-Code:") >= 0:
    #             return True
    #         # process = subprocess.check_output("'C:\\Program Files (x86)\\ZBar\\bin\\zbarimg' -q ./125.png",shell=True,stderr=subprocess.STDOUT)
    #         # print process.decode('gbk')
    #     except subprocess.CalledProcessError as e:
    #         # raise RuntimeError(
    #         #     "command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output.decode('gbk')))
    #         return False

    # 通过调用zbar的python库来识别二维码，前提是要先安装zbar插件，windows环境安装可能会有很多地雷
    # def get_qr_code(self, img_path):
    #     data = ''
    #     try :
    #         scanner = zbar.ImageScanner()
    #         scanner.parse_config("enable")
    #         pil = Image.open(img_path).convert('L')
    #         width, height = pil.size
    #         # raw = pil.tostring()
    #         raw = pil.tobytes()
    #         image = zbar.Image(width, height, 'Y800', raw)
    #         scanner.scan(image)
    #         for symbol in image:
    #             data += symbol.data
    #         del (image)
    #     except Exception, e:
    #         print "get_qr_code exception:" + e.__str__()
    #     finally:
    #         return data