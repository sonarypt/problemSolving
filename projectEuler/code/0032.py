#!/usr/bin/env python3

na = [1,2,3,4,5,6,7,8,9]
s = 0
pa = []

for i in range(2,9000):
  for j in range(i):
    p = i * j
    if (len(str(i)) + len(str(j)) + len(str(p)) > 9):
      break
    else:
      a = []
      a.extend([int(d) for d in str(i)])
      a.extend([int(d) for d in str(j)])
      a.extend([int(d) for d in str(p)])
      if sorted(a) == na and p not in pa:
        print("product: " + str(p) + " = " + str(i) + " * " + str(j))
        pa.append(p)
        s += p

print(s)


