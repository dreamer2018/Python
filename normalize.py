#!/usr/bin/env python
#coding=utf-8
def normalize(str):
    return str[0].upper()+str[1:].lower()
l=map(normalize,['adam','LISA','barT'])
print(list(l))
