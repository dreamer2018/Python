#!/usr/bin/env python
# coding=utf-8

class Student(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    def getnamescore(self):
        print self.__name,self.__score
s=Student('liming',58)
s.getnamescore()
print s._Student__name
