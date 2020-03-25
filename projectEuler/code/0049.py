#!/usr/bin/env python3

import math as m

# check prime with integer
def check_prime(nn):
  n = int(nn)
  stat = 1
  if (n % 2 == 0):
    stat -= 1
    return stat
  for i in range(3, m.ceil(m.sqrt(n))):
    if (n % i == 0):
      stat -= 1
      return stat
  return stat

def gen_triple(a, n):
  return a, a+n, a+2*n

def comp_digit(a, b, c):
  ar_a = sorted([d for d in str(a)])
  ar_b = sorted([d for d in str(b)])
  ar_c = sorted([d for d in str(c)])
  if (ar_a == ar_b) and (ar_b == ar_c):
    return 1
  else:
    return 0

for i in range(1000, 10000):
  if (i % 100 == 0):
    print("testing " + str(i))
  for j in range(1, 5000):
    a, b, c = gen_triple(i, j)
    if (b > 10000) or (c > 10000):
      continue
    else:
      if check_prime(a) and check_prime(b) and check_prime(c) \
          and comp_digit(a, b, c):
        print("triple: " + str(a) + ", " + str(b) + ", " + str(c))
      else:
        continue

