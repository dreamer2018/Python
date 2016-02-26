#!/usr/bin/env python
#coding=utf-8
# File Name: countchar.py
# Author: ZhouPan / github:dreamer2018 
# Mail: zhoupans_mail@163.com
# Blog: blog.csdn.net/it_dream_er
# Function:计算文件字符个数
# Created Time: 2016年02月04日 星期四 17时13分42秒
import sys
if len(sys.argv) <2 :
    print "Usage countchar.py file_name"
    exit()
file_name=sys.argv[1]
try:
    f=open(file_name)
except(IOError):
    print "Size: 0"
    exit()
count=0
for eachline in f:
    for each in eachline:
        count+=1
print "Size:",count
