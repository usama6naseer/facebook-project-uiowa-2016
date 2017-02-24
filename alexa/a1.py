from bs4 import BeautifulSoup
import requests
import csv
import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import xml.etree.ElementTree as ET
from operator import itemgetter, attrgetter, methodcaller

all_arr= []
f = open('net.txt', 'r')
x = f.readlines()
for row in x:
	if 2>1:
		print(row)
		arr = []
		arr.append(row[0])
		arr.append(row[1])
		arr.append(row[2])

		r  = requests.get("http://data.alexa.com/data?cli=10&dat=s&url=" + row[0])
		# r  = requests.get("http://data.alexa.com/data?cli=10&dat=s&url=http://official-liker.net/")
		data = r.text
		tree = ET.ElementTree(ET.fromstring(data))
		doc = tree.getroot()
		thingy = doc.find('SD/POPULARITY')
		rank = thingy.get("TEXT")
		thingy = doc.find('SD/COUNTRY')
		country = thingy.get("NAME")
		c_rank = thingy.get("RANK")

		arr.append(rank)
		arr.append(country)
		arr.append(c_rank)
		all_arr.append(arr)




# with open('net.csv', 'r', encoding="utf8") as f:
# 	reader = csv.reader(f)
# 	for row in reader:
# 		print(row)
		# arr = []
		# arr.append(row[0])
		# arr.append(row[1])
		# arr.append(row[2])

		# r  = requests.get("http://data.alexa.com/data?cli=10&dat=s&url=" + row[0])
		# # r  = requests.get("http://data.alexa.com/data?cli=10&dat=s&url=http://official-liker.net/")
		# data = r.text
		# tree = ET.ElementTree(ET.fromstring(data))
		# doc = tree.getroot()
		# thingy = doc.find('SD/POPULARITY')
		# rank = thingy.get("TEXT")
		# thingy = doc.find('SD/COUNTRY')
		# country = thingy.get("NAME")
		# c_rank = thingy.get("RANK")

		# arr.append(rank)
		# arr.append(country)
		# arr.append(c_rank)
		# all_arr.append(arr)


# sorted_data = sorted(data_all, key=itemgetter(1), reverse=True)
c = csv.writer(open("table.csv", "w", newline=''))
# c.writerow(["col_name","users","likes","comments","page_likes","date_created","present_date","days_passed"])
for rowentry in all_arr:
	try:
		c.writerow(rowentry)
	except:
		a=1 #do nothing

