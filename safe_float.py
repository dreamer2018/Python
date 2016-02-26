#!/usr/bin/env python
#coding=utf-8
# File Name: safe_float.py
# Author: ZhouPan / github:dreamer2018 
# Mail: zhoupans_mail@163.com
# Blog: blog.csdn.net/it_dream_er
# Function:设计一个安全的float()函数
# Created Time: 2016年02月05日 星期五 11时17分22秒
def safe_float(obj):
    try:
        retval=float(obj)
    except ValueError,v:
        retval="Error:"+str(v)
    except TypeError,t:
        retval="Error:"+str(t)
    return retval
obj=raw_input('Input:')
retval=safe_float(obj)
print retval
