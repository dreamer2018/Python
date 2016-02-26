#!/usr/bin/env python
#coding=utf-8
# File Name: for_test.py
# Author: ZhouPan / github:dreamer2018 
# Mail: zhoupans_mail@163.com
# Blog: blog.csdn.net/it_dream_er
# Function:
# Created Time: 2016年01月30日 星期六 14时19分24秒
def showMaxFactor(num):
    count=num/2
    while count>1:
        if num % count ==0:
            print 'largest factor of %d is %d ' % (num,count)
            break
        count -= 1
    else:
        print num,'is prime'
for eachNum in xrange(10,21):
    showMaxFactor(eachNum)
