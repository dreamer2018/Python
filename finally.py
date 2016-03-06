#!/usr/bin/env python
#coding=utf-8
# File Name: finally.py
# Author: ZhouPan / github:dreamer2018 
# Mail: zhoupans_mail@163.com
# Blog: blog.csdn.net/it_dream_er
# Function:
# Created Time: 2016年03月06日 星期日 22时09分36秒
import time
try:
    time.sleep(100)
except KeyboardInterrupt,e:
    print "Error"

