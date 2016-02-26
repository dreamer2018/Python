#!/usr/bin/env python
#coding=utf-8
# File Name: 1.py
# Author: ZhouPan / github:dreamer2018 
# Mail: zhoupans_mail@163.com
# Blog: blog.csdn.net/it_dream_er
# Function:
# Created Time: 2016年01月16日 星期六 06时03分30秒

str='abcdef'
for i in str:
    print i
for i in [None]+range(-1,-len(str),-1):
    print str[:i]

