#!/usr/bin/env python3

#  The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
#  Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#  NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

import math as m

s = 0

def check_prime(n):
  stat = 1
  if (n % 2 == 0):
    stat -= 1
    return stat
  for i in range(3, m.ceil(m.sqrt(n)) + 1):
    if (n % i == 0):
      stat -= 1
      return stat
  return stat

for i in range(11, 5000000, 2):
  i_str = str(i)
  if check_prime(i):
    l = len(str(i))
    lr = []
    rl = []
    for j in range(1, l):
      rl.append(int(i_str[:j]))
      lr.append(int(i_str[(l-j):]))
    st = 1
    for j in range(l-1):
      if not check_prime(rl[j]) or not check_prime(lr[j]):
        st -= 1
        break
    if (st == 1):
      print("number " + i_str)
      #  print("number " + i_str + " satisfy with: ")
      #  print(lr)
      #  print(rl)
      s += i
  else:
    continue

print("sum: " + str(s))
