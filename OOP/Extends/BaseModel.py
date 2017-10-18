#coding=utf-8
class BaseClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print 'baseclass is inited'

    def speak(self, sth):
        print "base class is speak: %s"%sth

# if __name__ == "__main__":
#     b = BaseClass()
