#!/usr/bin/env python
#coding=utf-8
g=(x*x for x in range(1,11))
for i in g:
    print(i)
#生成斐波那契数列
def fib(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n=n+1
    return 'done'
fib(6)

