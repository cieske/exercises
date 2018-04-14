# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 01:25:43 2018

@author: ciesk
"""

a, b, c = map(int, input().split())
print((a+b)%c)
print((a%c+b%c)%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)