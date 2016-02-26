#!/usr/bin/env python
#coding=utf-8
# File Name: three.py
# Author: ZhouPan / github:dreamer2018 
# Mail: zhoupans_mail@163.com
# Blog: blog.csdn.net/it_dream_er
# Function:
# Created Time: 2016年01月30日 星期六 14时30分56秒
def Max(x,y):
    #return x if x>y else y
    return x and x>y or y
x=100
y=200
max=Max(100,200)
print(max)
