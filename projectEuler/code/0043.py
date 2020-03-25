#!/usr/bin/env python3

#  The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
#  Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
#      d2d3d4=406 is divisible by 2
#      d3d4d5=063 is divisible by 3
#      d4d5d6=635 is divisible by 5
#      d5d6d7=357 is divisible by 7
#      d6d7d8=572 is divisible by 11
#      d7d8d9=728 is divisible by 13
#      d8d9d10=289 is divisible by 17
#  Find the sum of all 0 to 9 pandigital numbers with this property.

# reuse function to build list gradually
def add(i, a):
  b = []
  for j in a:
    for z in range(len(j)+1):
      b.append(j[:z] + str(i) + j[z:])
  return sorted(b)

# build the initial array
a = ['10']
for i in range(2, 10):
  a = add(i, a)
#  print(a)

# initalize sum
s = 0

# list of first few primes
pa = [2, 3, 5, 7, 11, 13, 17]

# loop through all numbers in array
for n in a:
  stat = 0
  for i in range(1, 8):
    if (int(n[i:i+3]) % pa[i-1] == 0):
      stat += 1
  if (stat == 7):
    print("number " + n + " with property")
    s += int(n)

print(s)
