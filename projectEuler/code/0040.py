#!/usr/bin/env python3

#  An irrational decimal fraction is created by concatenating the positive integers:
#  0.123456789101112131415161718192021...
#  It can be seen that the 12th digit of the fractional part is 1.
#  If dn represents the nth digit of the fractional part, find the value of the following expression.
#  d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

# start counting digit wih var dc
dc = 0

# start counting at number 1
i = 1

# expression of product
p = 1

# array for target index number
arr = [1, 10, 100, 1000, 10000, 100000, 1000000]

# while loop until find the digit at index
while (dc < 1000000):
  if (i % 1000 == 0):
    print("check " + str(i))
  l = len(str(i))
  for cut in range(1, len(str(i))+1):
    if cut + dc in arr:
      a = str(i)[cut-1:cut]
      print("number " + str(i) + " with digit " + a + " at position " \
          + str(cut+dc))
      p *= int(a)
    else:
      continue
  dc += l
  i += 1

print("product expression: " + str(p))
