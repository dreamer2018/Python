#!/usr/bin/env python
# encoding: utf-8
import datetime
today=datetime.date.today()
print 'today:'
print today
oneday=datetime.timedelta(days=1)
#print oneday
yesterday=today-oneday
tomorrow=today+oneday
print 'yesterday:'
print(yesterday)
print 'tomorrow:'
print(tomorrow)
