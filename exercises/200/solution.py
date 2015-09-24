# -*- coding: utf-8 -*-
"""Created on Sep 23 10:08:02 2015
@author: CharlotteVDD."""


def is_prime_old(x):
    result = True
    if x == 1:
        result = False
    for i in range(2, x):
        r = x % i
        if r == 0:
            result = False
    return(result)


def is_prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0 and x == 1:
            return False

    return True
