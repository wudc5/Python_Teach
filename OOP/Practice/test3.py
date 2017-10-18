#coding=utf-8
class Vehicle:
    def __init__(self, wheels, weight):
        self.wheels = wheels
        self.weight = weight
    def print1(self):
        print "Vehicle 车轮：{0}; 车重：{1}".format(self.wheels, self.weight)
class Car(Vehicle):
    def __init__(self, wheels, weight, loader):
        Vehicle.__init__(self, wheels, weight)
        self.loader = loader
    def print2(self):
        print"Car 车轮：{0}; 车重：{1}; 人数：{2}".format(self.wheels, self.weight, self.loader)

class Truck(Car):
    def __init__(self, wheels, weight, loader, payload):
        Car.__init__(self, wheels, weight, loader)
        self.payload = payload
    def print3(self):
        print "Truck 车轮：{0}; 车重：{1}; 人数：{2}; 有载重量:{3}".format(self.wheels, self.weight, self.loader, self.payload)

if __name__ == "__main__":
    v = Vehicle(4, 50)
    v.print1()
    c = Car(4, 30, 4)
    c.print2()
    t = Truck(4, 100, 2, 80)
    t.print3()