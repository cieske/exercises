#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 22:36:34 2018

@author: cieske
"""

N, X = map(int, input().split())
a = list(map(int,input().split()))

for i in range(N):
    if X > a[i]:
        print(a[i], end=' ')