#!/usr/bin/env python3

#  Euler discovered the remarkable quadratic formula:
#  n^2+n+41
#  It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39
#  . However, when n=40,40^2+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,41^2+41+41
#  is clearly divisible by 41.
#  The incredible formula n^2−79n+1601
#  was discovered, which produces 80 primes for the consecutive values 0≤n≤79
#  . The product of the coefficients, −79 and 1601, is −126479.
#  Considering quadratics of the form:
#      n^2+an+b
#  , where |a|<1000 and |b|≤1000
#  where |n|
#  is the modulus/absolute value of n
#  e.g. |11|=11 and |−4|=4
#  Find the product of the coefficients, a
#  and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.

import math as m

# function check for prime
def check_prime(n):
  s = 1
  if (n < 0) or (n % 2 == 0):
    s -= 1
    return s
  for i in range(3, m.ceil(m.sqrt(n)+1), 2):
    if (n % i == 0):
      s -= 1
      break
  return s
    
def quad(n, a, b):
  return n*n + a*n + b

r_step = 0
r_a = 0
r_b = 0

# loop through pair of a, b
for a in range(-999, 1000):
  for b in range(-1000, 1001):
    step = 0
    # check for range of n 
    while (check_prime(quad(step, a, b))):
      step += 1
    #  if (step > 60):
    #    print("pair (" + str(a) + ", " + str(b) + ") - step: " + str(step))
    # if greater than record pairs, add to value
    if (step > r_step):
      r_step = step
      r_a = a
      r_b = b

print("record: (" + str(r_a) + "; " + str(r_b) + ") - step: " + str(r_step))
