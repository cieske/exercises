# -*- coding: utf-8 -*-
"""
Created on Thu May  3 21:50:07 2018

@author: ciesk
"""

n = int(input())

a = 0
b = 1
c = 0
i = 2

if n == 1:
    print('1')
else:
    while i <= n:
        c = a + b
        a = b
        b = c
        i = i + 1
    
    else:
        print(c) 
