#!/usr/bin/env python3

S = 0
for i in range(2,1000000):
  dg = [int(d) for d in str(i)]
  s = 0
  for d in dg:
    s += (d**5)
  if (s == i):
    print(str(i) + " has this property")
    S += i

print(S)
