# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 00:40:48 2018

@author: ciesk
"""

N = int(input())

for i in range(1, N+1):
    print(' '*(N+1-i)+'*'*i)