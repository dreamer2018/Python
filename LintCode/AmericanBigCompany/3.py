#***************************************************************************************************
    # > File Name: 3.py
    # > Author: ZhouPan / github:dreamer2018 
    # > Mail: zhoupans_mail@163.com
    # > Blog: blog.csdn.net/it_dream_er
    # > Declared: Signed on behalf of not only belongs , but also represent a responsibility!
    # > Created Time: 2015年10月29日 星期四 20时31分03秒
#***************************************************************************************************

#!/usr/bin/env python
#coding=utf-8
def compareStrings(A, B):
    # write your code here
    a=[];
    for i in A:
        a.append(i)
    for i in B:
        if i not in a:
            return False
        a.remove(i)
    return True
print(compareStrings('ABCD','AACB'))

