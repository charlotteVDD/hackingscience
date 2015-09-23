# -*- coding: utf-8 -*-
"""Created on Sep 23 10:08:02 2015
@author: CharlotteVDD."""


def is_prime(x):
    for i in range(2, x):
        r = x % i
        if r == 0:
            resultat = False
        else:
            resultat = True
    return resultat

print(is_prime(54))
