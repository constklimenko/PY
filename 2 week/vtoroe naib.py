#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 18:10:43 2017

@author: narcom
"""
x = int(input())
max = 0
maxx = 0
y = 0

while x != 0:
    if x >= max:
        y = max
        max = x
    else:
        y = x
    if y >= maxx:
        maxx = y

    x = int(input())

print(maxx)
