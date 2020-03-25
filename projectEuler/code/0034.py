#!/usr/bin/env python3

#  145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#  Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#  Note: as 1! = 1 and 2! = 2 are not sums they are not included.

import math as m

rs = 0
for d in range(3, 10000000):
  a = [int(i) for i in str(d)]
  s = 0
  for j in a:
    s += m.factorial(j)
  if (s == d):
    print("number: " + str(d))
    rs += d

print(rs)
