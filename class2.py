#!/usr/bin/env python
# coding=utf-8
from types import MethodType
class Student(object):
    __slots__=('name')
def study():
    print "study hard"
def set_age(self,age):
    self.age=age

s=Student()
s.names="ZhouMing"
print s.name
s.set_age=MethodType(set_age,s)
s.set_age(21)
print s.age
Student.set_age=set_age
s2=Student()
s2.set_age(100)
print s2.age
s2.sex=1
