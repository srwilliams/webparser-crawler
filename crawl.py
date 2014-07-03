#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests

url = raw_input("URL: ")

site = requests.get("http://" +url)
sitetext = site.text

soup = BeautifulSoup(sitetext)

for link in soup.find_all('a'):
    print(link.get('href'))

print(soup.get_text())

