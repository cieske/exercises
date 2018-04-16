# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 23:01:09 2018

@author: ciesk
"""

N = int(input())
a = list(map(int, input().split()))
b = max(a)

for i in range(N):
    a[i] = a[i]/b*100
    
x = sum(a)/N
print(x)