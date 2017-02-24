from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import time
import datetime
from time import gmtime, strftime
from html.parser import HTMLParser
import re
import json
import facebook as fb
import sys
import requests
from timeout import timeout

def get_permissions():
	time.sleep(50)
	# perm = json.loads(st)
	# data = perm['data']
	# permissions_ = data[0]
	# keylist = permissions_.keys()
	# for key in keylist:
	# 	st = st + str(key) + " "

	# st = ""
	# for i in range(0,len(perm['data'])):
	# 	st =  st + str(perm['data'][i]['permission']) + " "
if  __name__ =='__main__':
	try:
		# @timeout(10, os.strerror(errno.ETIMEDOUT))
		get_permissions()
	except Exception as e:
		print(e)