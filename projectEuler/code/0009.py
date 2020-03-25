#!/usr/bin/env python3

#  A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#  a2 + b2 = c2
#  For example, 32 + 42 = 9 + 16 = 25 = 52.
#  There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#  Find the product abc.


def ptg(a, b):
  return a*a - b*b, 2*a*b, a*a + b*b

for i in range(1,32):
  for j in range(i, 32):
    a, b, c = ptg(j, i)
    if (a + b + c == 1000):
      print(str(a) + " " + str(b) + " " + str(c))
      print(str(a*b*c))

