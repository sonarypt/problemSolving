#!/usr/bin/env python3

import os
import random
import re # to remove "follow me on Twitter" text at the end of post
import time
import datetime
import pickle
from selenium import webdriver

driver = webdriver.Firefox(executable_path='/usr/bin/geckodriver')
cookies = pickle.load(open("/data/user/Downloads/cookies.txt", "rb"))
for cookie in cookies:
  driver.add_cookie(cookie)

# specify the link for full archive of Project Euler website
pe_main = "https://projecteuler.net/location=Vietnam;page="

for i in range(1, 5):
  driver.get(pe_main + str(i))
  info_list = driver.find_elements_by_xpath("//tbody//div[@class='info']")
  for p in info_list:
    stat = p.find_element_by_xpath("./span").text
    # get only number of day from status string
    num = re.findall(r"\d+", stat)[0]
    # get info of user only last 30 days
    if (num < 30):
      # replace stat string from <div> class
      text = info_list.text
      un = text.replace(stat, '')
      print("Found user: " + un + " online last: " + num + " days")
  time.sleep(random.randint(0, 5))


print(">> DONE <<")
driver.close()

