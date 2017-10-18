#coding=utf-8
class dog(object):
    def __init__(self, jaw, paw, mouth):
        self.jaw = jaw
        self.paw = paw
        self.mouth = mouth
    def bark(self):
        return "Wang, wang"
    def escape(self):
        return "eacape with " + self.paw
    def bite(self):
        return "bite with " + self.jaw
    def eat(self):
        return "eat with " + self.mouth
    def reaction(self, provoke):
        action = {"attack": self.bark() + ", "+ self.escape(), "food": self.eat(), "person": self.bark() + ", "+ self.bite()}
        return action[provoke]
xiaohuang = dog("bigjaw", "bigpaw", "bigmonth")
print xiaohuang.reaction("attack")
print xiaohuang.reaction("person")
print xiaohuang.reaction("food")
