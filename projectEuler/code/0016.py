#!/usr/bin/env python3

n = 2**1000
a = list(int(d) for d in str(n))
print(a)
s = 0
for i in a:
  print(i, end=" ")
  s += i
  print(s)
print(s)
