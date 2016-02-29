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
from conf import *
def mysqldump():
    filename=str(time.strftime("%Y%m%H%M%S",time.localtime(time.time())))
    filename='dump/'+filename
    dump_commond="mysqldump -u "+username+" -p"+passwd+" "+database+" > "+filename+".sql"
    os.system(dump_commond)
def gettime():
    now_hour= int(time.strftime("%H",time.localtime(time.time())))
    now_min = int(time.strftime("%M",time.localtime(time.time())))
    now_sec = int(time.strftime("%S",time.localtime(time.time())))
    return now_hour,now_min,now_sec
def timeer():
    hour,minute,second=gettime()
   # print hour
    if hour < 12:
        sleeptime=(12-hour)*3600-minute*60-second
        time.sleep(sleeptime)
        mysqldump()
    else:
        sleeptime=(24-hour)*3600-minute*60-second
        #timer=threading.Timer(sleeptime,mysqldump)
        #timer.start()
    #    print sleeptime
	time.sleep(sleeptime)
        mysqldump()
def main():
    while True:
        timeer()
main()
