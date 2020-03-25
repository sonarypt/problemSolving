#!/usr/bin/env python3

import os
import random
import re # to get only problem links
import time
import datetime
import threading
from selenium import webdriver

# current highest number of id
cur_id = 1236

# specify the link for full archive of Project Euler website
cf_main = "http://codeforces.com/contest/"

# save to specific dir
img_dir = "/home/user/scripts/codeforces/list"

if not os.path.exists(img_dir):
  os.mkdir(img_dir)

def cdf(begin, end):
  driver = webdriver.Firefox(executable_path='/usr/bin/geckodriver')
  for i in range(begin, end + 1):
    print("contest " + str(i), end = " ")
    prob_dir = img_dir + "/" + "{:04d}".format(i)
    
    # if not exists create dir
    if not os.path.exists(prob_dir):
      os.mkdir(prob_dir)
    plink = cf_main + str(i)
    
    # get contest link
    driver.get(plink)
    time.sleep(3)

    # find all problem link in contest link
    plist = driver.find_elements_by_xpath("//a")

    # build regex with var
    rel = r'contest/{0}/problem/\w?'.format(i)

    # empty array to append link
    al = []
    contest_str = "contest/" + str(i) + "/problem/"
    for l in plist:
      ll = l.get_attribute("href")
      #  if re.match(r'contest/%s/problem/\w?' % i, ll) and ll not in al:
      if re.match("[a-zA-Z.:/]+contest/\d+/problem/\w?$", ll) and ll not in al:
      #  if contest_str in ll and ll not in al:
        al.append(ll)

    # start count index of problem, append to file name then screenshot
    pi = 1
    for l in al:
      driver.get(l)
      f = driver.find_element_by_tag_name("body")
      img_path = prob_dir + "/" +  "{:04d}".format(i) + "_" + str(pi) + ".png"
      if os.path.exists(img_path):
        print("exists")
        pi += 1
        continue
      time.sleep(2)
      f.screenshot(img_path)
      time.sleep(random.randint(0, 5))
      pi += 1

  print(">> DONE <<")
  driver.close()

if __name__ == "__main__":
  # creating thread 
  t1 = threading.Thread(target=cdf, args=(1,206,)) 
  t2 = threading.Thread(target=cdf, args=(207,412,)) 
  t3 = threading.Thread(target=cdf, args=(413,618,)) 
  t4 = threading.Thread(target=cdf, args=(619,824,)) 
  t5 = threading.Thread(target=cdf, args=(825,1030,)) 
  t6 = threading.Thread(target=cdf, args=(1031,1236,)) 

  t1.start() 
  t2.start() 
  t3.start()
  t4.start()
  t5.start()
  t6.start()

  t1.join()
  t2.join() 
  t3.join()
  t4.join()
  t5.join()
  t6.join()

  # both threads completely executed 
  print("Done!")
