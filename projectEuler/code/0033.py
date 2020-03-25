#!/usr/bin/env python3

from fractions import Fraction

af = []

for j in range(11, 100):
  for i in range(10, j):
    ai = [int(d) for d in str(i)]
    aj = [int(d) for d in str(j)]
    for b in ai:
      if b in aj:
        if (b == 0):
          continue
        else:
          ai.remove(b)
          aj.remove(b)
    if (len(ai) + len(aj) > 2):
      continue
    else:
      if (ai[0] == 0) or (aj[0] == 0):
        continue
    if (i/j == ai[0]/aj[0]):
      print("fraction: " + str(i) + "/" + str(j))
      af.append([i,j])

num = 1
den = 1

for i in range(len(af)):
  num *= af[i][0]
  den *= af[i][1]

print(str(num) + "/" + str(den))
print(Fraction(num, den))

