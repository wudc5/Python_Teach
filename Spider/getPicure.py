#coding=utf-8

import urllib
import re
import urllib2

proxy_info = {'host': 'web-proxy.oa.com', 'port':8080}

proxy_support = urllib2.ProxyHandler({"http": "http://%(host)s:%(port)d" % proxy_info})

opener = urllib2.build_opener(proxy_support)
urllib2.install_opener(opener)

def getHtml(url):
    page = urllib.urlopen(url)
    htmlcontent = page.read()
    return htmlcontent
def getImg(htmlcontent):
    reg = r'src="(.+?\.jpg|png)"'
    imgre = re.compile(reg)
    imgurllist = re.findall(imgre, htmlcontent)
    x = 0
    for imgurl in imgurllist:
        # if len(imgurl) ==0 or len(imgurl) >100:
        #     continue
        # urllib.urlretrieve(imgurl, 'C:\Users\wdc\Pictures\%s.jpg' % x)
        x += 1
        print "imgurl: ", imgurl
if __name__ == "__main__":
    html = getHtml("http://image.baidu.com")
    print html
    getImg(html)