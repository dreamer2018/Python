#!/usr/bin/env python
#coding=utf-8
# File Name: remove_space.py
# Author: ZhouPan / github:dreamer2018 
# Mail: zhoupans_mail@163.com
# Blog: blog.csdn.net/it_dream_er
# Function:
# Created Time: 2016年03月14日 星期一 22时05分28秒
def is_empty(s):
    return s and s.strip()
print(list(filter(is_empty,['A', '', 'B', None, 'C', ' '])))
