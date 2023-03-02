#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 11:42:17 2021

@author: peter
"""

import random
import matplotlib.pyplot as plt

freq = [0 for i in range(101)]
for i in range(1,10000):
    x = random.random()
    y = random.random()
    z = x*y
    z_int = int(round(z*100, 0))
    #print(z, z_int)
    freq[z_int] = freq[z_int] + 1
x_vals = range(101)
plt.plot(x_vals, freq)

freq = [0 for i in range(101)]
for i in range(1,10000):
    x = random.random()
    #y = random.random()
    z = x*x
    z_int = int(round(z*100, 0))
    #print(z, z_int)
    freq[z_int] = freq[z_int] + 1
x_vals = range(101)
plt.plot(x_vals, freq)
plt.show

