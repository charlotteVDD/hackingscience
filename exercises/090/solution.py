# -*- coding: utf-8 -*-
"""Created on Mon Sep 21 10:08:02 2015
@author: CharlotteVDD
that outputs the position of the argument and its value in a new
line using a for."""
import sys
import operator
get_arg = operator.itemgetter(0, 1)
a = list(enumerate(sys.argv))

for i in range(len(a)):
        print(a[i][0], a[i][1])
