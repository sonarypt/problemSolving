#!/usr/bin/env python3

s = 0

for i in range(1001):
  print(i, end=" ")
  s += i**i

print('last 10 digit ' + str(s)[-10:])
