#!/usr/bin/env python
#coding=utf-8
# File Name: seek.py
# Author: ZhouPan / github:dreamer2018 
# Mail: zhoupans_mail@163.com
# Blog: blog.csdn.net/it_dream_er
# Function:
# Created Time: 2016年03月03日 星期四 21时30分36秒
f=open('map.py','r')
for eachLine in f:
    print eachLine,
#回到开头
f.seek(0)
print f.readline(),
#从当前位置算起
f.seek(1)
f.seek(1)
print f.readline(),
print f.readline(),
print f.readline(),
print f.readline(),
print f.readline(),
#回到末尾
f.seek(1)
f.readline(),
f.close()
