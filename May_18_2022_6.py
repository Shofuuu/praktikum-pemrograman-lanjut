#!/usr/bin/python3

class Top:
    def m_top(self):
        print('Top')

class Middle_Left(Top):
    def m_middle(self):
        print('Middle Left')

class Middle_Right(Top):
    def m_middle(self):
        print('Middle Right')

class Bottom(Middle_Left, Middle_Right):
    def m_bottom(self):
        print('Bottom')

obj = Bottom()
obj.m_bottom()
obj.m_middle()
obj.m_top()