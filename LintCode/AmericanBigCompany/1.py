#***************************************************************************************************
    # > File Name: 1.py
    # > Author: ZhouPan / github:dreamer2018 
    # > Mail: zhoupans_mail@163.com
    # > Blog: blog.csdn.net/it_dream_er
    # > Declared: Signed on behalf of not only belongs , but also represent a responsibility!
    # > Created Time: 2015年10月29日 星期四 19时29分15秒
#***************************************************************************************************

#!/usr/bin/env python
#coding=utf-8
class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(s, t):
        for i in s:
            if i in t :
                pass
            else:
                return False
        if len(s)==len(t):
            return True 
        return False
    # write your code here
    print(anagram('abce','abce'))
