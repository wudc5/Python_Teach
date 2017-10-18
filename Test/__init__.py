#coding=utf-8
class dog():
    name = 'xiaohuang'
    def __init__(self):
        self.favior = "foot"
    def action(self):
        print self.name
    def bark(self):
        self.action()

xiaohuang = dog()
xiaohuang.action()