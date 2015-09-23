# -*- coding: utf-8 -*-
"""Created on Mon Sep 21 10:08:02 2015
@author: CharlotteVDD
sort_a_list that takes a list as argument and return the list sorted
in the descending order, such as:
In [1]: from solution import sort_a_list
In [2]: l = [1, 3, 2, 4, 6, 5, 9, 7]
In [3]: sort_a_list(l)
Out[3]: [9, 7, 6, 5, 4, 3, 2, 1]"""
import operator


def sort_a_list(l):
    a = sorted(l)
    a.reverse()
    return(a)

my_class = [[6, 'Joshua Tran'], [37, 'Jeanette Wafer'], [85, 'Susan Maddox'],
            [84, 'Joseph Peter'], [12, 'Bonnie Torres'], [36, 'John Freeman'],
            [27, 'Betty Askins'], [22, 'Mark Osbourne'], [42, 'Lidia Robel']]


def sort_by_mark(l):
    a = sort_a_list(my_class)
    print(a)
    for i in a:
        print(i)

getname = operator.itemgetter(1)
c = list(map(getname, my_class))
d = list(sorted(my_class, key=getname))


def sort_by_name(l):
    b = list(sorted(l, key=getname))
    for i in b:
        print(i)

sort_by_mark(my_class)
# sort_by_name(my_class)


def get_marks(l):
    for i in range(len(l)):
        marks = operator.itemgetter(0)(l[i])
        print(marks)
    return(marks)
