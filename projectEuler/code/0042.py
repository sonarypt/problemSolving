#!/usr/bin/env python3

import string

# array of first few more triangle numbers
na = []
for i in range(30):
  na.append(int(i*(i+1)/2))

print(na)

# count number of that words
n = 0

f = open("./p042_words.txt", "r")
line = f.readline()
arr = line.split("\"")
for e in arr:
  if (e == ",") or (e == ""):
    arr.remove(e)

for w in arr:
  s = 0
  for l in w:
    s += string.ascii_uppercase.index(l)+1
  if s in na:
    print("checking " + w, end = " ")
    print("with value " + str(s))
    print(">> triangular word <<")
    n += 1

print("number of word " + str(n))

