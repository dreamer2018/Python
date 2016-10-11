#!/usr/bin/env python3.4
# coding=utf-8
import sys


keywards = {}

# 关键字部分
keywards['False'] = 101
keywards['class'] = 102
keywards['finally'] = 103
keywards['is'] = 104
keywards['return'] = 105
keywards['None'] = 106
keywards['continue'] = 107
keywards['for'] = 108
keywards['lambda'] = 109
keywards['try'] = 110
keywards['True'] = 111
keywards['def'] = 112
keywards['from'] = 113
keywards['nonlocal'] = 114
keywards['while'] = 115
keywards['and'] = 116
keywards['del'] = 117
keywards['global'] = 118
keywards['not'] = 119
keywards['with'] = 120
keywards['as'] = 121
keywards['elif'] = 122
keywards['if'] = 123
keywards['or'] = 124
keywards['yield'] = 125
keywards['assert'] = 126
keywards['else'] = 127
keywards['import'] = 128
keywards['pass'] = 129
keywards['break'] = 130
keywards['except'] = 131
keywards['in'] = 132
keywards['raise'] = 133

# 符号
keywards['+'] = 201
keywards['-'] = 202
keywards['*'] = 203
keywards['/'] = 204
keywards['='] = 205
keywards[':'] = 206
keywards['<'] = 207
keywards['>'] = 208
keywards['<='] = 209
keywards['>='] = 210
keywards['%'] = 211
keywards['&'] = 212
keywards['!'] = 213
keywards['('] = 214
keywards[')'] = 215
keywards['['] = 216
keywards[']'] = 217
keywards['{'] = 218
keywards['}'] = 219
keywards['#'] = 220
keywards['++'] = 220
keywards['--'] = 221
keywards['|'] = 222
keywards[','] = 223
keywards['=='] = 224
keywards['!='] = 225
keywards['"""'] = 226
# 变量
keywards['var'] = 301

# 常量
keywards['const'] = 401

# 预处理函数，将文件中的空格，换行等无关字符处理掉
def Pretreatment(file_name):
    try:
        fp_read = open(file_name,'r')
        fp_write = open('file.tmp','w')
        sign = 0
        while (1):
            read = fp_read.read(1)
            if not read:
                break
            if read == '#':
                sign = 1
            elif read == '\n':
                if sign == 1:
                    sign = 6
                else:
                    sign = 2
            elif (read == ' ' or read == '\t') and (sign != 1 and sign != 4) :   # 此处屏蔽掉注释
                if sign == 3 :
                    sign = 5
                else:
                    sign = 3
            # elif i == '"""' and sign != 4:
            #     if sign != 4 :
            #         sign = 0
            #     else:
            #         sign = 4

            if sign == 2 :
                read = ' '
                sign = 3
            if sign != 1:
                fp_write.write(read)

    except Exception as e:
        print(file_name,': This FileName Not Found!')
def main():
    if(len(sys.argv) < 2 ):
        print("Please Input FileName")
    else:
        Pretreatment(sys.argv[1])
if __name__ == '__main__':
    main()
