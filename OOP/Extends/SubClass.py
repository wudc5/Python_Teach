#coding=utf-8
import BaseModel
class SubClass(BaseModel.BaseClass):
    def __init__(self, name, age, salary):
        BaseModel.BaseClass.__init__(self, name, age)
        self.salary = salary
        print 'sub class is inited and salary is %s'%salary
    def talk(self,sth):
        print "%s is talking %s"%(self.name, sth)
        BaseModel.BaseClass.speak(self, sth)

if __name__ == "__main__":
    s = SubClass("Joan", 1, 800)
    s.talk("a story")