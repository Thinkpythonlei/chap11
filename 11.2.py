# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 19:20:53 2023

@author: Surface
"""
#11.2
dict1 = {'a': 1, 'b': 2, 'c': 3}
def invert_dict(d):
    return dict([(v,k) for (k,v) in d.iteritems()]
print(invert_dict(dict1))





