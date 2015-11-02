#!/usr/bin/env python
#coding=utf-8

#生成1-110这些数的列表
l=list(range(1,111))
for i in l:
    print(i)
#生成i*i的列表
L=[x*x for x in range(1,11)]
for i in L:
    print(i)
#生成1-10中偶数的平方
H=[x*x for x in range(1,11) if x%2==0]
for i in H:
    print(i)
#生成全排列
K=[m+n for m in 'abc' for n in 'def']
for i in K:
    print(i)
#大写转小写
L=['hello','world',18,'IBM','Apple']
l=[ x.lower() for x in L if isinstance(x,str)]
for i in l:
    print(i)
