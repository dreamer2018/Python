#!/usr/bin/env python
#coding=utf-8
# File Name: signtest.py
# Author: ZhouPan / github:dreamer2018 
# Mail: zhoupans_mail@163.com
# Blog: blog.csdn.net/it_dream_er
# Function:
# Created Time: 2016年01月16日 星期六 06时51分50秒
import string
s1=string.letters+string.digits
s2=string.letters+'_'
print s1
print s2
s3=raw_input('Please Input:')
print s3
if len(s3) <= 0 :
    print 'not input any'
    exit(0)
if s3[0] not in s2:
    print 'Not Symbol in 0'
    exit(0)
for i in range(1,len(s3),1):
    if s3[i] not in s1:
        print 'Not symbol in %d ' % (i)
        exit(0)
print 'It is Symbol'
