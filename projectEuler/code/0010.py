#!/usr/bin/env python3

#  The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#  Find the sum of all the primes below two million.

s = 2
arr_p = [2]

for i in range(3, 2000000):
  stat = 0
  for p in arr_p:
    if (i % p == 0):
      stat += 1
      break
    else:
      continue
  if (stat == 0):
    print(i)
    arr_p.append(i)
    s += i

print("Sum: " + str(s))
