#coding=utf-8
import random
import base64
from selenium import webdriver
import time
from scrapy.http import HtmlResponse
from settings import PROXIES
class RandomUserAgent(object):
  """Randomly rotate user agents based on a list of predefined ones"""
  def __init__(self, agents):
    self.agents = agents
  @classmethod
  def from_crawler(cls, crawler):
    return cls(crawler.settings.getlist('USER_AGENTS'))
  def process_request(self, request, spider):
    #print "**************************" + random.choice(self.agents)
    request.headers.setdefault('User-Agent', random.choice(self.agents))
class ProxyMiddleware(object):
  def process_request(self, request, spider):
    proxy = random.choice(PROXIES)
    if proxy['user_pass'] is not None:
      request.meta['proxy'] = "http://%s" % proxy['ip_port']
      encoded_user_pass = base64.encodestring(proxy['user_pass'])
      request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
      print "**************ProxyMiddleware have pass************" + proxy['ip_port']
    else:
      print "**************ProxyMiddleware no pass************" + proxy['ip_port']
      request.meta['proxy'] = "http://%s" % proxy['ip_port']

class JavaScriptMiddleware(object):
  driver = webdriver.Firefox()
  driver.set_script_timeout(10)
  driver.set_page_load_timeout(10)
  def process_request(self, request, spider):
        # executable_path = '/home/hadoop/crawlcompanyinfo0906/phantomjs'
        print "PhantomJS is starting..."
        # driver = webdriver.PhantomJS(executable_path)  # 指定使用的浏览器
        self.driver.get(request.url)
        print "htmlcontent: ", self.driver.page_source
        if "验证码" in self.driver.page_source:
          print "请在30秒内完成验证码验证！"
          time.sleep(30)
        # js = "var q=document.documentElement.scrollTop=10000"
        # self.driver.execute_script(js)  # 可执行js，模仿用户操作。此处为将页面拉至最底端。
        time.sleep(3)
        body = self.driver.page_source
        print ("访问" + request.url)
        return HtmlResponse(self.driver.current_url, body=body, encoding='utf-8', request=request)
