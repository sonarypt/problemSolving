#!/usr/bin/env python3

#  A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
#      1/2	= 	0.5
#      1/3	= 	0.(3)
#      1/4	= 	0.25
#      1/5	= 	0.2
#      1/6	= 	0.1(6)
#      1/7	= 	0.(142857)
#      1/8	= 	0.125
#      1/9	= 	0.(1)
#      1/10	= 	0.1
#  Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
#  Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

em = 0
d = 2

while (d < 1000):
  # skip all multiples of 2 and 5
  if (d % 2 == 0) or (d % 5 == 0):
    d += 1
    continue
  else:
    a = 10
    e = 1
    # find the exponential of 10 to remain 1 mod d
    while (a % d > 1):
      a *= 10
      e += 1
    #  print(str(d) + " with cycle: " + str(e))
    if (e > em):
      em = e
    d += 1

print(em)
