#!/usr/bin/env python
#coding=utf-8
def max(a,b):
    if a>b:
        return a
    return b

def MAX(a,b,c,f):
    return f(f(a,b),c)
print(MAX(1,2,8,max))
