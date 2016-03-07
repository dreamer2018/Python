#!/bin/bash
# File Name: start.sh
# Author: ZhouPan / github:dreamer2018 
# Mail: zhoupans_mail@163.com
# Blog: blog.csdn.net/it_dream_er
# Function:
# Created Time: 2016年03月13日 星期日 00时00分52秒
if [ ! -d 'dump' ];then
    mkdir dump
fi
nohup python mysqldump.py &
