#!/usr/bin/python3

class Top:
    def m_top(self):
        print('Top')

class Middle:
    def m_middle(self):
        print('Middle')

# MRO Problem
class Bottom(Middle, Top):
    def m_bottom(self):
        print('Bottom')

obj = Bottom()
obj.m_top()
obj.m_middle()
obj.m_bottom()