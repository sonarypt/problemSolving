#!/usr/bin/env python3

#  If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#  If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#  NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

def count_letter(word):
  c = 0
  for l in word:
    c += 1
  return c
# some word hard to count in computer
lc = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12:' twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty'}

# generate the rest of dictionary
def mk_dict(num):
  global lc
  for i in range(num+1, num+10):
    lc[i] = lc[num] + lc[i-num]

lc[20] = "twenty"
mk_dict(20)
lc[30] = "thirty"
mk_dict(30)
lc[40] = "forty"
mk_dict(40)
lc[50] = "fifty"
mk_dict(50)
lc[60] = "sixty"
mk_dict(60)
lc[70] = "seventy"
mk_dict(70)
lc[80] = "eighty"
mk_dict(80)
lc[90] = "ninety"
mk_dict(90)

# start var for counting
tc = 0

for i in range(1, 1000):
  if (i/100 >= 1):
    #  print(i)
    if (i % 100 == 0):
      hundred = i/100
      tc = tc + count_letter(lc[hundred]) + 7
    else:
      hundred = (i - i%100)/100
      # the word "and" add extra 3 letters
      tc += (count_letter(lc[hundred]) + 10 + count_letter(lc[i - hundred*100]))
  else:
    #  print(i)
    tc += count_letter(lc[i])

print(tc)
print(count_letter("onethousand"))
tc = tc + count_letter("onethousand")
print(tc)

