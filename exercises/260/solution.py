# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 08:58:34 2015

@author: CharlotteVDD
"""
import numpy as np
from math import pow
from math import sqrt


x = [2, 3]
y = [5, 6]


def euclidean(a, b):
    result = 0
    sum_sqr = 0
    if len(a) >= 2:
        for i in range(len(a)):
            sum_sqr = sum_sqr + (b[i] - a[i])**2
        result = (sum_sqr)**0.5
    else:
        print("Error")
    return result


def opt_euclidean(a, b):
    result = 0
    sum_sqr = 0
    if len(a) >= 2:
        for i in range(len(a)):
            sum_sqr = sum_sqr + pow((b[i] - a[i]), 2)
        result = sqrt(sum_sqr)
    else:
        print("Error")
    return result


def np_euclidean(a, b):
    result = 0
    sum_sqr = 0
    if len(a) >= 2:
        for i in range(len(a)):
            sum_sqr = sum_sqr + (np.power((b[i] - a[i]), 2))
        result = np.sqrt(sum_sqr)
    else:
        print("Error")
    return result
