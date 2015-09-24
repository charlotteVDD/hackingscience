# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 10:02:47 2015
function is_alpha that takes one string as parameter and returns the boolean
value True if every characters of the given parameter are letters,
False otherwise.
@author: CharlotteVDD
"""
import string


def is_alpha(a):
    letters = string.ascii_letters
    for i in a:
        if i in letters:
            continue
        else:
            return False
    return True
