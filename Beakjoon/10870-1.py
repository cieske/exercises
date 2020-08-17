# -*- coding: utf-8 -*-
"""
Created on Thu May  3 22:43:14 2018

@author: ciesk
"""

n = int(input())

a = 0
b = 1
c = 0


if n == 1:
    print('1')
else:
    for i in range(n-1):
        c = a + b
        a = b
        b = c
        
    
    else:
        print(c)
