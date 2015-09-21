# -*- coding: utf-8 -*-
"""Created on Mon Sep 21 10:08:02 2015
@author: CharlotteVDD
that print the first parameter given to the script.
If thereis no parameters given, it should print the following
error message : usage: python3 solution.py PARAM."""
import sys
script = sys.argv
if len(script) > 1:
    print(script[-1])
else:
    print("usage: python3 solution.py PARAM")
