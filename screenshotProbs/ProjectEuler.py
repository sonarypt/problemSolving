#!/usr/bin/env python3

import os
import random
import re # to remove "follow me on Twitter" text at the end of post
import time
import datetime
from selenium import webdriver

driver = webdriver.Firefox(executable_path='/usr/bin/geckodriver')

# specify the link for full archive of Project Euler website
pe_main = "https://projecteuler.net/problem="

# save to specific dir
img_dir = "/home/user/scripts/Euler/list"

if not os.path.exists(img_dir):
  os.mkdir(img_dir)

today = datetime.date.today()
dstr = today.strftime('%Y%m%d')

for i in range(1, 684):
  print("problem " + str(i), end = " ")
  img_path = img_dir + "/" + dstr + "_" + str(i) + ".png"
  if os.path.exists(img_path):
    print("exists")
    continue
  pl = pe_main + str(i)
  driver.get(pl)
  f = driver.find_element_by_tag_name("body")
  time.sleep(2)
  f.screenshot(img_dir + "/" + dstr + "_" + str(i) + ".png")
  time.sleep(random.randint(0, 5))

print(">> DONE <<")
driver.close()

