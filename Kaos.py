#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 14:10:01 2021

@author: peter
"""
import matplotlib.pyplot as plt

x1 = 0.8
a = 3
NoOfPoints = 100
y_vals = [0 for i in range(0,NoOfPoints-1)]
y_vals[0] = x1
for i in range(1,NoOfPoints-1):
    x2 = a*x1*(1-x1)
    print(x2)
    x1 = x2
    y_vals[i] = x1;
    
x_vals = range(0,NoOfPoints-1)
plt.plot(x_vals, y_vals)
plt.show
