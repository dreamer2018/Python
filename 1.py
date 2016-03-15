#!/usr/bin/env python
#coding=utf-8
# File Name: 1.py
# Author: ZhouPan / github:dreamer2018 
# Mail: zhoupans_mail@163.com
# Blog: blog.csdn.net/it_dream_er
# Function:
# Created Time: 2016年01月16日 星期六 06时03分30秒
list=[-2,8,-4,7,-9,2,6,5]
l=sorted(list)
print(l)
l=sorted(list,key=abs)
print(l)
l=sorted(list,key=abs,reverse=True)
print(l)
