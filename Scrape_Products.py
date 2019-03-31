"""
File: gov-bills-scraper.py
Author: Handy Hasan
Description: A web scraper that retrieves the top 10 
	viewed bills in Congress currently. Print neatly 
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

url = "https://www.congress.gov/resources/display/content/Most-Viewed+Bills"
r = requests.get(url)
soup = BeautifulSoup(r.content)
i = 0
howmany = 0
for bill in soup.find_all("td", {"class":"confluenceTd"}):
	try:
		print(bill.text)
	except:
		pass
	i+=1
	howmany+=1
	if i == 3:
		print("\n")
		i = 0
	if howmany == 30:
		break