#!/usr/bin/env python3

#  It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
#  Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

import math as m

# check if x and 6x has the same number of digits
def same_dig(a, b):
  # check the power of 10 that frame a:
  pa = a
  pb = b
  ppa = 0
  ppb = 0
  while (pa >= 1):
    pa = m.floor(pa/10)
    ppa += 1
  while (pb >= 1):
    pb = m.floor(pb/10)
    ppb += 1
  if ppa == ppb:
    return 1
  else:
    return 0

# loop through all
# choose s as variable to stop
x = 10
s = 1
while (s != 0):
  x += 1
  if x % 500000 == 0:
    print("checked " + str(x))
  #  # 2x version
  #  if not same_dig(x, 2*x):
  #    continue
  #  xa = [int(i) for i in str(x)].sort()
  #  xa2 = [int(i) for i in str(2*x)].sort()
  #  if xa == xa2:
  #    s = 0
  #    print("number " + str(x) + " satisfied")
  # 6x version
  if not same_dig(x, 6*x):
    continue
  xa = [int(i) for i in str(x)]
  xa2 = [int(i) for i in str(2*x)]
  xa3 = [int(i) for i in str(3*x)]
  xa4 = [int(i) for i in str(4*x)]
  xa5 = [int(i) for i in str(5*x)]
  xa6 = [int(i) for i in str(6*x)]
  xa.sort()
  xa2.sort()
  xa3.sort()
  xa4.sort()
  xa5.sort()
  if xa == xa2 and xa2 == xa3 and xa3 == xa4 and xa4 == xa5 and xa5 == xa6:
    s = 0
    print("number " + str(x) + " satisfied")

