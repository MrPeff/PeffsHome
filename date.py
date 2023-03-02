#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date

delta_arr = []

def SetupDeltaArr(delta):
    delta_arr.clear()
    while delta > 0:
        reminder = delta % 10
        delta_arr.append(reminder)ö.
        delta -= reminder
        delta //= 10
    delta_arr.reverse()
    print(delta_arr)

def Round1000(Days) :
    return ((Days % 1000) == 0)

def SameNumber() :
     i = 0
     Same = False
     while delta_arr[i+1] != -1:
         Same = delta_arr[i] == delta_arr[i+1]
         if not Same:
             break
         i += 1
     return Same

def CheckIfSpecialNumber(Days) :
    if Round1000(Days) :
        print("hej", Days)
    if SameNumber():
        print("Same number", Days)
    
    
def ReportSpecialDays(DateBorn, Name) :
    DateToday   = date.today()
    delta = DateToday - DateBorn
    SetupDeltaArr(delta.days)
    print(Name, delta.days)
    CheckIfSpecialNumber(delta.days)

ReportSpecialDays(date(1966,  4, 19), "Peter"   )
ReportSpecialDays(date(1966, 11,  8), "Hanna"   )
ReportSpecialDays(date(1997,  4,  7), "Joel"    )
ReportSpecialDays(date(2003,  1, 10), "Shelton" )
ReportSpecialDays(date(1940,  4, 28), "Anka"    )
ReportSpecialDays(date(1969,  1, 19), "Snosse"  )
ReportSpecialDays(date(1994,  5, 12), "Bröllop" )

SetupDeltaArr(3333)
CheckIfSpecialNumber(3333)
print("urk")

