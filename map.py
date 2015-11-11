#!/usr/bin/env python
#coding=utf-8
def pow(a):
    return a**2
l=map(pow,[1,2,3,4])
print(list(l))
from functools import reduce
def f(a,b):
    return a*10+b
print(reduce(f,[1,2,3,4]))
