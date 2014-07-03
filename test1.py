#!/usr/bin/python2.7

from bs4 import BeautifulSoup
import requests
import re

url = raw_input("URL: ")
# Ask for the URL.

site = requests.get("http://" +url)
sitedata = site.text
# Go to the site and retrieve the information

file = open("data.txt", 'a')
file.write("\nhttp://"+url+"\n\n")
# This saves the data we get into a file called "data.txt".  If the file does not exist, the program creates it, and if the file does exist, the program appends the data to the file.



soup = BeautifulSoup(sitedata)
# Store the info in the BeautifulSoup datastructure

aff = soup.find("div", { "class" : "affiliated-companies module"})
# Find all objects of class "affiliated-companies module"

print("\n"+aff.h4.string+":\n")
file.write("\n"+aff.h4.string+":\n")

children = aff.findChildren()
for child in children:
    if child.get('href') != None:
        print("www.linkedin.com"+child.get('href'))
        file.write("www.linkedin.com"+child.get('href')+"\n")
# Iterate through the children of the tag and print all contents associated with 'href'.  Since this test is for www.linkedin.com, I hardcoded the beginning of the URL into the program.

file.close()
