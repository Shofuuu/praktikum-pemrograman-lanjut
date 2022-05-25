#!/usr/bin/python3

str_a = "Mary had a little"
str_b = "Mary had a little lamb"
str_a += " lamb"

print(str_a == str_b, str_a is str_b)

class ExampleClass:
    def __init__(self, val):
        self.val = val
    
obj_a = ExampleClass(0)
obj_b = ExampleClass(2)
obj_c = obj_a
obj_c.val += 1

print(obj_a is obj_b)
print(obj_b is obj_c)
print(obj_c is obj_a)
print(obj_a.val, obj_b.val, obj_c.val)