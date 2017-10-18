#coding=utf-8
from lxml import etree
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def writeToFile(filepath, content):
    with open(filepath, "w") as wp:
        wp.write(content)
        wp.close()

if __name__ == "__main__":
    url = "http://music.baidu.com/"
    content = getHtml(url)
    print content
    writeToFile("music.txt", content)
    content = open("music.txt", 'r').read()

    selector = etree.HTML(content)
    classvaluelist = selector.xpath('//div/@class')  # 解析出所有的div标签的class属性值
    for cvalue in classvaluelist:
        print cvalue

    valuelist = selector.xpath("//a[@class='key']/text()")   #解析出所有属性为class=”key”的a标签中的内容
    for value in valuelist:
        print value

    songnamelist = selector.xpath("//div[@class='song']/a/@title")  #解析出所有的歌名
    for songname in songnamelist:
        print songname

    songhreflist = selector.xpath("//div[@class='song']/a/@href")  #解析出所有的歌名链接
    for href in songhreflist:
        print href
