#!/usr/bin/env python3

a = 1
b = 1
i = 2

def fn(a, b):
  global i
  c = a + b
  a = b
  b = c
  i += 1
  return a, b

while (len(str(b)) < 1000):
  a, b = fn(a, b)
  if (len(str(b)) < 5):
    print(b, end = " ")
    print(i)

print(">> DONE <<")
print(i)
print(b)
print(len(str(b)))
