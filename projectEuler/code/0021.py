#!/usr/bin/env python3

#  Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#  If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#  For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#  Evaluate the sum of all the amicable numbers under 10000.

a = []
for i in range(1, 10001):
  print(i)
  if i in a:
    continue
  else:
    s1 = 0
    s2 = 0
    for j in range(1, i):
      if (i % j == 0):
        s1 += j
    for j in range(1,s1):
      if (s1 % j == 0):
        s2 += j
    if (s1 == i):
      continue
    if (s2 == i):
      a.extend([i, s1])

print(">> " + str(a))
s = 0
for i in a:
  s += i
print(">> " + str(s))
