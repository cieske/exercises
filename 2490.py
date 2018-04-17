# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 00:06:53 2018

@author: ciesk
"""

x = list(map(int, input().split()))
y = list(map(int, input().split()))
z = list(map(int, input().split()))

def minsoknole(a):   
        if sum(a) == 1:
            print('C')
        elif sum(a) == 2:
            print('B')
        elif sum(a) == 3:
            print('A')
        elif sum(a) == 4:
            print('E')
        elif sum(a) == 0:
            print('D')
        
minsoknole(x)
minsoknole(y)
minsoknole(z)