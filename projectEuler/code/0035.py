#!/usr/bin/env python3

import math as m

# this problem is kinda vague since they mention rotate or permutation?

n = 0

# function to rotate string around
def rev(n, i):
  n_s1 = str(n)[:i]
  n_s2 = str(n)[i:]
  nn = int(n_s2 + n_s1)
  return(nn)

def check_prime(n):
  stat = 1
  if (n % 2 == 0):
    stat -= 1
    return stat
  for i in range(3, m.ceil(m.sqrt(n))):
    if (n % i == 0):
      stat -= 1
      return stat
  return stat

for i in range (11, 1000000, 2):
  i_str = str(i)
  if check_prime(i):
    stat = 1
    for j in range(1, len(i_str)):
      if not check_prime(rev(i, j)):
        stat -= 1
        break
    if (stat == 1):
      n += 1
      print("prime " + str(i) + " satisfied")
  else:
    continue

print("total: " + str(n) + " primes")
