# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 23:30:58 2018

@author: ciesk
"""

N = int(input())

for i in range(1, N+1):
    print(' '*(i-1)+'*'*(N+1-i))