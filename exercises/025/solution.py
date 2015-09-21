# -*- coding: utf-8 -*-
"""Created on Mon Sep 21 10:08:02 2015
@author: CharlotteVDD
print the actual date (day month year hour minute and seconds)
in a human readable format such as:
Today is 2015-09-17 and it is 18:34:35"""
import datetime
a = datetime.date.today()
b = datetime.datetime.now()
b = str(b)
c = len(b)
b = b[0:19]
b = str.split(b)
print("Today is", b[0], " and it is ", b[1])
