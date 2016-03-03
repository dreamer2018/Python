#!/usr/bin/env python
#coding=utf-8
# File Name: enumerate.py
# Author: ZhouPan / github:dreamer2018 
# Mail: zhoupans_mail@163.com
# Blog: blog.csdn.net/it_dream_er
# Function:
# Created Time: 2016年03月03日 星期四 19时30分54秒
seq=[1,2,'3','zhoupan']
for i in seq:
    print i
i=0
for element in seq:
    print seq[i]
    i+=1
for i,element in enumerate(seq):
    print i,seq[i]

