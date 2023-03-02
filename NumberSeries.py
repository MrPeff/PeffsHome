# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def GenerateNextValue(val_1, val_2):
    val_3 = val_1 + val_2
    return val_3
    
print("hejsan")

val_1 = 1
val_2 = 1
print(val_1)
print(val_2)
for i in range(50):
    val = GenerateNextValue(val_1, val_2)
    print(val)
    val_1 = val_2
    val_2 = val



