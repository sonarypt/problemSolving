#!/usr/bin/env python3

#  The prime 41, can be written as the sum of six consecutive primes:
#  41 = 2 + 3 + 5 + 7 + 11 + 13
#  This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#  The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#  Which prime, below one-million, can be written as the sum of the most consecutive primes?

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

for i in range(5, 200000, 2):
  rec = 1
  sp = 2
  ind = 1
  for j in range(3, i+1, 2):
    if check_prime(j):
      sp += i
      ind += 1
  if check_prime(sp):
    if sp > rec and sp != 2: 
      rec = sp
      print("new record " + str(rec) + " with lengths " + str(ind))



