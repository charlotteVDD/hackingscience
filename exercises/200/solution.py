# -*- coding: utf-8 -*-
"""Created on Sep 23 10:08:02 2015
@author: CharlotteVDD."""

import string


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
    if x <= 0:
        return False
    elif x == 1:
        return False
    elif x == 2:
        return True
    elif x == 3:
        return True
    else:
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
            else:
                continue
    return True
print(is_prime(9))
print(is_prime(11))
print(is_prime(97))
print(is_prime(500))

