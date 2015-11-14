#!/usr/bin/env python
#coding=utf-8
def is_odd(n):
    return n%2==1
l=filter(is_odd,[1,2,3,4,5,6])
print(list(l))
