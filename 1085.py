# -*- coding: utf-8 -*-
"""
Created on Sat May  5 19:12:49 2018

@author: ciesk
"""

x, y, w, h = map(int, input().split())

print(min(x-0, y-0, w-x, h-y))