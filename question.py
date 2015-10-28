#***************************************************************************************************
    # > File Name: question.py
    # > Author: ZhouPan / github:dreamer2018 
    # > Mail: zhoupans_mail@163.com
    # > Blog: blog.csdn.net/it_dream_er
    # > Declared: Signed on behalf of not only belongs , but also represent a responsibility!
    # > Created Time: Fri 09 Oct 2015 05:13:43 PM CST
#***************************************************************************************************

#!/usr/bin/env python
#coding=utf-8
def add_end(L=None):
    if L is None:
        L=[]
    L.append("end")
    return L
print(add_end([1,2,3]))
print(add_end(['a','b','c']))
print(add_end())
print(add_end())
print(add_end())
def calc(*number):
    sum=0
    for i in number:
        sum=sum+i
    return sum
print(calc(1,2,3,4))
print(calc(5,6,7,8,9,5))

def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
person('ZhouPan',20)
person('ZhouPan',20,mail='zhoupans_mail@163.com',address='Xi^An')


