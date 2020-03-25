#!/usr/bin/env python3

#  Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
#  For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
#  What is the total of all the name scores in the file?

import string

f = open("./p022_names.txt", "r")
# sort and replace char " at the same time
for l in f:
  a = sorted([i.replace('"', '') for i in l.split(',')])

s = 0

for l in a:
  w = 0
  for ll in l:
    w += string.ascii_uppercase.index(ll)+1
  i = a.index(l) + 1
  s += w*i

print(s)


