# -*- coding: utf-8 -*-
"""Created on Mon Sep 21 10:08:02 2015
@author: CharlotteVDD."""

import operator


my_class = [['Kermit Wade', 27], ['Hattie Schleusner', 67], ['Ben Ball', 5],
            ['William Lee', 2]]


def select_student(l, m):
    accepted = []
    refused = []
    for i in l:
        if i[1] < m:
            refused.append(i)
            get_mark = operator.itemgetter(1)
            ref = list(sorted(refused, key=get_mark))
        else:
            accepted.append(i)
    status = dict({'Accepted': accepted, 'Refused': ref})
    return(status)

print(select_student(my_class, 20))
