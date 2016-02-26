#!/usr/bin/env python
#coding=utf-8
# File Name: stack.py
# Author: ZhouPan / github:dreamer2018 
# Mail: zhoupans_mail@163.com
# Blog: blog.csdn.net/it_dream_er
# Function:使用列表来模拟堆栈
# Created Time: 2016年01月26日 星期二 12时08分43秒

#创建栈
stack=[]
#帮助函数
def Help():
    help='''
    ----------------------
        [U] 入栈
        [O] 出栈
        [V] 查看栈中元素
        [Q] 推出操作
    ----------------------
    '''
    print help

#入栈函数
def Push():
    inputs=raw_input("Enter New Element:")
    stack.append(inputs)
def Pop():
    if(len(stack)==0):
        print('stack is null')
    else:
        print 'delete:',stack[len(stack)-1]
        stack.pop()
def View():
    if(len(stack)==0):
        print('stack is null')
    else:
        print stack
inputs='A'
while(inputs!='Q' and inputs!='q'):
    Help()
    try:
        inputs=raw_input("Please input:")
    except(EOFError,KeyboardInterrupt,IndexError):
        inputs='q'
        continue
    if(inputs=='U' or inputs=='u'):
        Push()
    elif(inputs=="O" or inputs=='o'):
        Pop()
    elif(inputs=='V' or inputs=='v'):
        View()
    elif(inputs=='Q' or inputs=='q'):
        pass
    else:
        Help()
