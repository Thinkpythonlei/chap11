# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 23:54:49 2023

@author: Surface
"""
#11.3
def ack(m,n):

    if m==0:
        return n+1
    elif m>0 and n==0:
        return ack(m-1,1)
    elif m>0 and n>0:
        return ack (m-1,ack(m,n-1))
    
    
cache={}
def ack1(m,n):
    if (m, n) in cache:
        return cache[m, n]
    else:
        cache[m, n] = ack(m-1, ack(m, n-1))
        return cache[m, n]
    
    
print(ack(2,3))
