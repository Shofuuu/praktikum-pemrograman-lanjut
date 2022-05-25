#!/usr/bin/python3

class L1: 
    var = 100
    def func(self):
        return 101
    
class L2(L1):
    var = 200
    def func(self):
        return 201
    
class L3(L2):
    pass

obj = L3()

print(obj.var, obj.func())