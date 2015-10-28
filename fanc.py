#***************************************************************************************************
    # > File Name: fanc.py
    # > Author: ZhouPan / github:dreamer2018 
    # > Mail: zhoupans_mail@163.com
    # > Blog: blog.csdn.net/it_dream_er
    # > Declared: Signed on behalf of not only belongs , but also represent a responsibility!
    # > Created Time: 2015年10月28日 星期三 22时05分04秒
#***************************************************************************************************

#!/usr/bin/env python
#coding=utf-8
def fanc(n):
    if n==1:
        return 1
    return n*fanc(n-1)
print(fanc(100))
