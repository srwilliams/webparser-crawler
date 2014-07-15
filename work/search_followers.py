#!/usr/bin/python2.7

import time, os, random
from datetime import date
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


# Setup

random.seed()

number = random.randint(1, 15)

driver = webdriver.Firefox()

try:
    dbase = file("database.txt")
except IOError:
    print 'Unable to open file', dbase

curdate = date.today()
curdate = curdate.isoformat()

file = open( curdate, 'a')

lnum = 0
line = dbase.readline()

driver.get("http://www.linkedin.com")
time.sleep(10)

start = time.time()

# Begin loop

while 1:

    lntok = line.split()
    try:
        ext = lntok[0]
    except IndexError:
        break

    link = "www.linkedin.com/company/" + ext
    site = driver.get(link)
    elem = driver.find_element_by_xpath("//*")
    source_code = elem.get_attribute("outerHTML")
    soup = BeautifulSoup(source_code)
    followercount = soup.find("p", {"class" : "followers-count"})

    if followercount is not None:
        count = followercount.a.strong.string
        count = count.replace(',','')
    else:
        time.sleep(60)
        continue
    lnum +=1
    print(str(lnum) + "\t" + link + "\t" + count)
    file.write(lntok[0] + "\t" + lntok[1] + "\t" + count + "\n")
    time.sleep(number)

    line = dbase.readline()

end = time.time()
print("Finished")
print("Time elapsed: " + str(end - start))
print("Number of URLs read: " + str(lnum))

file.close()
dbase.close()
driver.quit()
