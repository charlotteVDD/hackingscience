# -*- coding: utf-8 -*-
"""Created on Mon Sep 21 10:08:02 2015
@author: CharlotteVDD
solution.py that print the result of simple addition. If no parameters
are given, you must print the following
error message : usage: python3 solution.py OP1 OP2"""
import sys
num = sys.argv
if len(sys.argv) == 3:
    result = int(num[-2]) - int(num[-1])
    print(result)
else:
    print("usage: python3 solution.py OP1 OP2")
