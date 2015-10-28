#***************************************************************************************************
    # > File Name: method3.py
    # > Author: ZhouPan / github:dreamer2018 
    # > Mail: zhoupans_mail@163.com
    # > Blog: blog.csdn.net/it_dream_er
    # > Declared: Signed on behalf of not only belongs , but also represent a responsibility!
    # > Created Time: 2015年10月28日 星期三 20时08分27秒
#***************************************************************************************************

#!/usr/bin/env python
#coding=utf-8
def power(a):
    return a**2
print(power(int(input())))
def test(a=100,b=200):
    return a+b
print(test())
print(test(1,2))

def test2(a,b):
    return a+b
print(test(b=2))


