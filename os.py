#!/usr/bin/env python
#coding=utf-8
# File Name: os.py
# Author: ZhouPan / github:dreamer2018 
# Mail: zhoupans_mail@163.com
# Blog: blog.csdn.net/it_dream_er
# Function:
# Created Time: 2016年03月03日 星期四 21时42分02秒
import os
#os.mkdir('test')
#区别在于rename只能更改一层，而renames可以递归式的将文件和文件夹名一次更改
#os.renames('test/1.txt','tes/1.c')
#os.rename('test/1.txt','tes/1.c')
print os.getcwd()
print os.path.basename('2q')
print os.path.dirname('/home/zhoupan/2q')
