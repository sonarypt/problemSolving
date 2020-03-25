#!/usr/bin/env python3

#  The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.
#  Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#  (Please note that the palindromic number, in either base, may not include leading zeros.)

s = 0

# check for palindromic characteristic
def cpl(n):
  l = len(str(n))
  nn = [d for d in str(n)]
  nn_ = []
  for i in range(l):
    nn_.append(nn[l-1-i])
  n_ = "".join(nn_)
  if (str(n) == n_):
    return 1
  return 0

for n in range(1000000):
  bn = int(bin(n)[2:])
  if cpl(n) and cpl(bn):
    print("number " + str(n) + " and its bin: " + str(bn))
    s += n

print("sum: " + str(s))
