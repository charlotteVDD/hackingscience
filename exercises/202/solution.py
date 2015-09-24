# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 10:02:47 2015
starts_with(haystack, needle) with haystack and needle of type string and
returning a boolean.
starts_with will return True if the string in the haystack parameter
starts with needle, and False otherwise.
@author: CharlotteVDD
"""


def starts_with(haystack, needle):
    if len(needle) > len(haystack):
        return False
    for i in range(len(needle)):
        if needle[i] != haystack[i]:
            return False
        else:
            continue
    return True
