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
keywards['|'] = 221
keywards[','] = 222
keywards['=='] = 223
keywards['!='] = 224
keywards['"""'] = 225
keywards['+='] = 226
keywards['-='] = 227
# 变量
# keywards['var'] = 301

# 常量
# keywards['const'] = 401

# Error
# keywards['const'] = 501

signlist = {}


# 预处理函数，将文件中的空格，换行等无关字符处理掉
def Pretreatment(file_name):
    try:
        fp_read = open(file_name, 'r')
        fp_write = open('file.tmp', 'w')
        sign = 0
        while (True):
            read = fp_read.readline()
            if not read:
                break
            length = len(read)
            i = -1
            while i < length - 1:
                i += 1
                if sign == 0:
                    if read[i] == ' ':
                        continue
                if read[i] == '#':
                    break
                elif read[i] == ' ':
                    if sign == 1:
                        continue
                    else:
                        sign = 1
                        fp_write.write(' ')
                elif read[i] == '\t':
                    if sign == 1:
                        continue
                    else:
                        sign = 1
                        fp_write.write(' ')
                elif read[i] == '\n':
                    if sign == 1:
                        continue
                    else:
                        fp_write.write(' ')
                        sign = 1
                elif read[i] == '"':
                    fp_write.write(read[i])
                    i += 1
                    while i < length and read[i] != '"':
                        fp_write.write(read[i])
                        i += 1
                    if i >= length:
                        break
                    fp_write.write(read[i])
                elif read[i] == "'":
                    fp_write.write(read[i])
                    i += 1
                    while i < length and read[i] != "'":
                        fp_write.write(read[i])
                        i += 1
                    if i >= length:
                        break
                    fp_write.write(read[i])
                else:
                    sign = 3
                    fp_write.write(read[i])
    except Exception:
        print(file_name, ': This FileName Not Found!')


def Save(string):
    if string in keywards.keys():
        if string not in signlist.keys():
            signlist[string] = keywards[string]
    else:
        Save_Var(string)


def Save_Var(string):
    if string not in signlist.keys():
        if len(string.strip()) < 1:
            pass
        else:
            signlist[string] = 301


def Save_Const(string):
    if string not in signlist.keys():
        signlist[string] = 401


def Save_Error(string):
    if string not in signlist.keys():
        signlist[string] = 501


def Recognition(FileName):
    try:
        fp_read = open(FileName, 'r')
        string = ""
        sign = 0
        while True:
            read = fp_read.read(1)
            if not read:
                break

            if read == ' ':
                if len(string.strip()) < 1:
                    sign = 0
                    pass
                else:
                    if sign == 1 or sign == 2:
                        string += read
                    else:
                        Save(string)
                        string = ""
                        sign = 0
            elif read == '(':
                if sign == 1 or sign == 2:
                    string += read
                else:
                    Save(string)
                    string = ""
                    Save('(')
            elif read == ')':
                if sign == 1 or sign == 2:
                    string += read
                else:
                    Save(string)
                    string = ""
                    Save(')')
            elif read == '[':
                if sign == 1 or sign == 2:
                    string += read
                else:
                    Save(string)
                    string = ""
                    Save('[')
            elif read == ']':
                if sign == 1 or sign == 2:
                    string += read
                else:
                    Save(string)
                    string = ""
                    Save(']')
            elif read == '{':
                if sign == 1 or sign == 2:
                    string += read
                else:
                    Save(string)
                    string = ""
                    Save('{')
            elif read == '}':
                if sign == 1 or sign == 2:
                    string += read
                else:
                    Save(string)
                    string = ""
                    Save('}')
            elif read == ',':
                Save(string)
                string = ""
                Save(',')
            elif read == "'":
                string += read
                if sign == 1:
                    sign = 0
                    Save(string)
                    string = ""
                else:
                    if sign != 2:
                        sign = 1
            elif read == '"':
                string += read
                if sign == 2:
                    sign = 0
                    Save(string)
                    string = ""
                else:
                    if sign != 1:
                        sign = 2
            elif read == ':':
                if sign == 1 or sign == 2:
                    string += read
                else:
                    Save(string)
                    string = ""
                    Save(':')
            elif read == '+':
                #sign = 3
                Save(string)
                string = "+"
                # Save('+')
            elif read == '=':
                Save(string)
                string = ""
                Save('=')
            else:
                string += read

    except Exception as e:
        print(e)


def main():
    if (len(sys.argv) < 2):
        print("Please Input FileName")
    else:
        Pretreatment(sys.argv[1])
    Recognition('file.tmp')
    for i in signlist.keys():
        print("(", signlist[i], ",", i, ")")


if __name__ == '__main__':
    main()
