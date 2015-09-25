# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 15:14:22 2015
ex 280
@author: CharlotteVDD
"""
import sys


try:
    print(sys.argv[1])
except(IndexError):
    print("Not enough parameters")
