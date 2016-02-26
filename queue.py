#!/usr/bin/env python
#coding=utf-8
# File Name: queue.py
# Author: ZhouPan / github:dreamer2018 
# Mail: zhoupans_mail@163.com
# Blog: blog.csdn.net/it_dream_er
# Function:使用列表模拟队列
# Created Time: 2016年01月26日 星期二 12时56分51秒

#定义一个队列
queue=[]
def Help():
    help='''
    --------------------------
        [I] 入队
        [O] 出队
        [V] 查看队列中元素
        [Q] 退出
    --------------------------
    '''
    print(help)
def In_Q():
    inputs=raw_input('Please Input Element:')
    queue.append(inputs)
def Out_Q():
    if(len(queue)==0):
        print("Queue is null")
    else:
        print "delete",queue[0]
        queue.pop(0)
def View_Q():
    if(len(queue)==0):
        print 'Queue is  null'
    else:
        print queue
inputs='A'
while(inputs!='Q' and inputs!='q'):
    Help()
    try:
        inputs=raw_input("Please Input:")
    except(EOFError,KeyboardInterrupt,IndexError):
        inputs='q'
        continue
    if(inputs=='I' or inputs=='i'):
        In_Q()
    elif(inputs=="O" or inputs=='o'):
        Out_Q()
    elif(inputs=='V' or inputs=='v'):
        View_Q()
    elif(inputs=='Q' or inputs=='q'):
        pass
    else:
        Help()

