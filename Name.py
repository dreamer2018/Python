#!/usr/bin/env python
#coding=utf-8
# File Name: Name.py
# Author: ZhouPan / github:dreamer2018 
# Mail: zhoupans_mail@163.com
# Blog: blog.csdn.net/it_dream_er
# Function:
# Created Time: 2016年03月14日 星期一 21时56分32秒
def Normalize(name):
    return name[0].upper()+name[1:len(name)].lower()
L1 = ['adam', 'LISA', 'barT']
L2=list(map(Normalize,L1))
print(L2)
