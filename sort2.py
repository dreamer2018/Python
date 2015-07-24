#!/usr/bin/env python
# encoding: utf-8
list=[]
for i in range(0,5,1):
    x=input("请输入第"+str(i+1)+"个元素")
    list=list+[x]
for i in range(0,5,1):
    for j in range(i,5,1):
       # print j
        k=i
        if(list[k]<list[j]):
            k=j
        h=list[k]
        list[k]=list[i]
        list[i]=h
print list
