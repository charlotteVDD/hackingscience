# -*- coding: utf-8 -*-
"""
pernicious number : positive interger where digit sum of its binary rep is
prime
@author: CharlotteVDD
"""
import is_prime

x = range(222281, 222381)
a = []

for i in x:
    result = 0
    b = bin(i)[2:]
    for n in b:
        result = result + int(n)
    if is_prime.is_prime(result) is True:
        print(i)
