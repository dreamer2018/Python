#!/usr/bin/env python
#coding=utf-8

'makeTextFile.py -- create text file'

import os
ls =os.linesep

#get filename

while True:
    if os.path.exists(fname):
        print "ERROR: '%s' already exists" % fname
    else :
        break;

#get file content (text) lines

all=[]

print "\n Enter lines ('.' by itself to quit).\n"


