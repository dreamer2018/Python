#***************************************************************************************************
    # > File Name: method.py
    # > Author: ZhouPan / github:dreamer2018 
    # > Mail: zhoupans_mail@163.com
    # > Blog: blog.csdn.net/it_dream_er
    # > Declared: Signed on behalf of not only belongs , but also represent a responsibility!
    # > Created Time: Fri 09 Oct 2015 04:51:37 PM CST
#***************************************************************************************************

#!/usr/bin/env python
#coding=utf-8
def fun1():
    print 'hello world'
def fun2(a):
    print a
    return a*a
fun1()
print fun2(4)
def fun3(a=100):
    print a
    return fun2(a)
print fun3(10)
