#!/usr/bin/env python3

#  We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
#  What is the largest n-digit pandigital prime that exists?

import math as m

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

# initialize number record
rec = 0

# reuse function to build list gradually
def add(i, a):
  b = []
  for j in a:
    for z in range(len(j)+1):
      b.append(j[:z] + str(i) + j[z:])
  return sorted(b)

# build the initial array
a = ['1']
for i in range(2, 10):
  a = add(i, a)
  #  print(a)
  for j in a:
    print(j)
    if check_prime(j) and int(j) > rec:
      print("new record " + str(j))
      rec = int(j)

print("final record " + str(rec))
