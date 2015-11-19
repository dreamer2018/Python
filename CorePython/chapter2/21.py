#!/usr/bin/env python
#coding=utf-8

logfile=open("logfile.log","a")
print >>logfile,'Fatal error:invalid input!'
logfile.close()
name=raw_input('请输入你的姓名：')
print 'your name is',name
num=raw_input('Please imput a number:')
print 'You input number is %d ' % (int(num))
