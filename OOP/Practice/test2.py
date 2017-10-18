#coding=utf-8
class dictclass(object):
    def __init__(self, dict):
        self.dict = dict
    def get_dict(self, key):
        if self.dict.has_key(key):
            return self.dict[key]
        else:
            return 'not found'
    def del_dict(self, key):
        if self.dict.has_key(key):
            self.dict.pop(key)
        else:
            return 'no that key'
    def get_key(self):
        return self.dict.keys()

A = dictclass({'a': 1, 'b': 2})
print A.get_dict('c')
print A.del_dict('c')
print A.get_key()