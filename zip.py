#!/usr/bin/env python
#coding=utf-8
# File Name: zip.py
# Author: ZhouPan / github:dreamer2018 
# Mail: zhoupans_mail@163.com
# Blog: blog.csdn.net/it_dream_er
# Function:
# Created Time: 2016年03月03日 星期四 19时41分38秒
a=[1,2,3,4,5]
b=['a','b','c','d']
c=zip(a)
print type(c)
print c
c=zip(a,b)
print c
d=zip(*c)
print d
