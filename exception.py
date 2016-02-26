#!/usr/bin/env python
#coding=utf-8
# File Name: exception.py
# Author: ZhouPan / github:dreamer2018 
# Mail: zhoupans_mail@163.com
# Blog: blog.csdn.net/it_dream_er
# Function:python异常的练习
# Created Time: 2016年02月05日 星期五 10时42分52秒
import sys
if len(sys.argv) < 2:
    print "Error"
    exit()
try:
    f=open(sys.argv[1])
    print "test"
except IOError,e:
    print e
    exit()
print sys.argv[1],"已经打开"
