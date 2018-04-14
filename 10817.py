# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 01:10:42 2018

@author: ciesk
"""

a, b, c = map(int, input().split())
if a<=b and b<=c:
    print(b)
elif c<=b and b<=a:
    print(b)
elif a<=c and c<=b:
    print(c)
elif b<=c and c<=a:
    print(c)
else:
    print(a)