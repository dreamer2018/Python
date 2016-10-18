#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import keyword
import string


def is_signal(s):
    kw = keyword.kwlist
    if s in kw:
        return 0
    elif s[0] == '_' or s[0] in string.ascii_letters:  # 判断是否为字母或下划线开头
        for i in s:
            if i == '_' or i in string.ascii_letters or i in string.digits:  # 判断是否由字母数字或下划线组成
                pass
            else:
                return 0
        return 1
    else:
        return 0


def main():
    s = input()
    if is_signal(s) == 1:
        print("True")
    else:
        print("False")


if __name__ == '__main__':
    main()
