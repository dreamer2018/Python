#!/usr/bin/env python
#coding=utf-8
# File Name: stat.py
# Author: ZhouPan / github:dreamer2018 
# Mail: zhoupans_mail@163.com
# Blog: blog.csdn.net/it_dream_er
# Function:
# Created Time: 2016年02月04日 星期四 18时12分15秒
import os
import sys
if len(sys.argv) < 2 :
    print "Usage: stat filename"
    exit()
result=os.stat(sys.argv[1])
#for i in range(0,len(result),1):
#    print result[i]
print result
