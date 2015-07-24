#!/usr/bin/env python
# encoding: utf-8
list=[]
for i in range(0,5,1):
    x=input('请输入第'+str(i+1)+'个元素')
    list=list+[x]
for i in range(0,5,1):
    for j in range(0,5-i-1,1):
        if(list[j]>list[j+1]):
            k=list[j]
            list[j]=list[j+1]
            list[j+1]=k
print list
