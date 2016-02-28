#!/usr/bin/env python
#coding=utf-8
# File Name: mysqldump.py
# Author: ZhouPan / github:dreamer2018 
# Mail: zhoupans_mail@163.com
# Blog: blog.csdn.net/it_dream_er
# Function:
# Created Time: 2016年02月28日 星期日 15时35分59秒
import os
import time
import threading
import datetime
database='zhoupan'
username='root'
passwd='zhoupan'
database='mysql'

def mysqldump():
    dump_commond="mysqldump -u "+username+" -p"+passwd+" "+database+" > "+filename+".sql"
    #os.system(dump_commond)
    print dump_commond
filename=str(time.strftime("%Y%m%H%M%S",time.localtime(time.time())))
#while True:
now_hour=int(time.strftime("%H",time.localtime(time.time())))
print now_hour
