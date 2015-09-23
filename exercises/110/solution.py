# -*- coding: utf-8 -*-
"""Created on Sep 23 10:08:02 2015
@author: CharlotteVDD."""
import sys
from string import digits


l = sys.argv
a = ["blabla", "b", "/", "1"]

digit = str(digits)
opr = ["+", "-", "*", "/", "%", "^"]

if len(l) < 4:
    print("Error: please give 3 parameters")
elif l[1] in digit and l[3] in digit and l[2] in opr:
    if len(l) < 4:
        print("Error: please give 3 parameters")
    else:
        b = int(l[1])
        c = int(l[3])
        op = l[2]
        if op == '+':
            result = b + c
        elif op == '-':
            result = b - c
        elif op == '*':
            result = b * c
        elif op == '/':
            result = b / c
        elif op == '%':
            result = b % c
        elif op == '^':
            result = b ^ c
    print(result)
else:
    print("input error")
