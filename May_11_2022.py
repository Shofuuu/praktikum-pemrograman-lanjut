#!/usr/bin/python3

class Egg:
    def __init__(self, come_from, method):
        self.come_from = come_from
        self.method = method
    
    def lay(self):
        return self.come_from
    
    def getMethod(self):
        return self.method
    
class Boiled(Egg):
    def __init__(self, come_from, total_eggs):
        super().__init__(come_from, method='boiled')
        self.total_eggs = total_eggs
    
    def boil(self):
        return self.total_eggs

class Fried(Egg):
    def __init__(self, come_from, total_eggs):
        super().__init__(come_from, method='fried')
        self.total_eggs = total_eggs
    
    def fry(self):
        return self.total_eggs

egg = Egg('Chicken', 'none')
boiled = Boiled('Duck', 2)
fried = Fried('Ostrich', 2)

print(egg.lay(), 'Layed an egg')
print(boiled.lay(), 'Layed an egg and', boiled.getMethod(), 'it', boiled.boil())
print(fried.lay(), 'Layed an egg and', fried.getMethod(),'it', fried.fry())