#!/usr/bin/env python3

lp = 1

for i in range(100, 1000):
  for j in range(100, 1000):
    p = i * j
    if (str(p) == str(p)[::-1]) and (p > lp):
      lp = p

print(lp)
