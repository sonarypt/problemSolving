#!/usr/bin/env python3

#  By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#  What is the 10 001st prime number?

index = 1
arr_p = [2]
n = 3

while (index < 10002):
  ps = 0
  for p in arr_p:
    if (n % p == 0):
      ps += 1
      break
    else:
      continue
  if (ps == 0):
    index += 1
    arr_p.append(n)
    print(str(index) + " prime: " + str(n))
  # prime case
  n += 2
