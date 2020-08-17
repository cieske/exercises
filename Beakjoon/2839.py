# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 22:02:24 2018

@author: ciesk
"""
n = int(input())

a = n//5
b = n%5
c = 0

while a>=0:
    if b%3 == 0:
        c = b//3
        break
    a -= 1
    b += 5
        
if b%3 == 0:
    print(a+c)
else:
    print(-1)

