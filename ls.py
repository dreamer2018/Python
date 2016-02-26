#!/usr/bin/env python
#coding=utf-8
# File Name: ls.py
# Author: ZhouPan / github:dreamer2018 
# Mail: zhoupans_mail@163.com
# Blog: blog.csdn.net/it_dream_er
# Function:
# Created Time: 2016年02月04日 星期四 18时23分45秒
import sys
import os
import os.path
length=len(sys.argv)
if length > 2:
    print "Usage ls.py dir_name"
    exit()
elif length==2 :
    dir_name=sys.argv[1]
else:
    dir_name='.'
result=os.listdir(dir_name)
for i in range(len(result)):
    print result[i]," ",
