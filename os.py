#!/usr/bin/env python
#coding=utf-8
# File Name: os.py
# Author: ZhouPan / github:dreamer2018 
# Mail: zhoupans_mail@163.com
# Blog: blog.csdn.net/it_dream_er
# Function:
# Created Time: 2016年03月03日 星期四 21时42分02秒
import os
import sys
#os.mkdir('test')
#区别在于rename只能更改一层，而renames可以递归式的将文件和文件夹名一次更改
#os.renames('test/1.txt','tes/1.c')
#os.rename('test/1.txt','tes/1.c')
if(os.path.exists(sys.argv[1])):
   print 'Exist'
else:
   print 'Not Exist !'
   exit(0)
print '文件名：',os.path.basename((sys.argv[1]))
print '文件夹名：',os.path.dirname(os.getcwd()+sys.argv[1])
print '最近访问时间：',os.path.getatime(sys.argv[1])
print '文件创建时间：',os.path.getctime(sys.argv[1])
print '文件修改时间：',os.path.getmtime(sys.argv[1])
print '文件大小(字节):',os.path.getsize(sys.argv[1])

