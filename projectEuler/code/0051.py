#!/usr/bin/env python3

#  By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
#  By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.
#  Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

# status var to loop
s = 0

# number to test looping
n = 100

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

# generate array of numbers 
def gen_arr(n, d):

while (s == 0):
  n += 1
  n_str = str(n)
  if not check_prime(n):
    continue
  # number of digit to replace
  for i in range(len(n_str)):


