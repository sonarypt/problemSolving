#!/usr/bin/env python3

#  A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
#  012   021   102   120   201   210
#  What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# build the list gradually by adding more digit into
def add(i, a):
  b = []
  for j in a:
    for z in range(len(j)+1):
      b.append(j[:z] + str(i) + j[z:])
  return sorted(b)

# build the initial array
a = ['01', '10']
for i in range(2, 10):
  a = add(i, a)

print(a[999999])
