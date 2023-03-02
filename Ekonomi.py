#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 17:17:18 2022

@author: peter
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 14:10:01 2021

@author: peter
"""
import matplotlib.pyplot as plt

save_per_month = 400
val = save_per_month
NrOfMonths = 12*3
growth = 1.0 + 0.05/12.0
print(growth)
print(save_per_month*NrOfMonths)
y_vals = [0 for i in range(0,NrOfMonths)]
for i in range(0,NrOfMonths):
    y_vals[i] = val
    val = val*growth + save_per_month
print(y_vals)    

plt.plot(range(0,NrOfMonths), y_vals)
plt.show
