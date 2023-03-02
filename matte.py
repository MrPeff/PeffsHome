#!/usr/bin/python3.5

import random

tal1 = list(range(10, 21))
tal2 = list(range(1, 11))
ResLim1 = 10
ResLim2 = 20

def Operation1(tal1, tal2):
  return tal1 - tal2

def Operation2(tal1, tal2):
  return tal1 + tal2

def ResOK(res):
  return (ResLim1 <= res) and (res <= ResLim2)

res = []
for i in tal1:
    for j in tal2:
      TalRes = Operation2(i, j)
      if ResOK(TalRes):
        talpar = [i,j]
        res.append(talpar)
random.shuffle(res)

for i in res:
  TalPar = i;
  print(TalPar[0], " + ", TalPar[1], " = ")
