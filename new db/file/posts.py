import csv
import datetime
import time
import mysql.connector
from mysql.connector import errorcode
from operator import itemgetter, attrgetter, methodcaller
# from operator import attrgetter

def make_time(s):
	v = s.split('T')
	v1 = v[1].split('+')
	st = v[0] + ' ' + v1[0]
	return st
map_date = dict()
with open('usersposts.csv', 'r', encoding="utf8") as f:
	reader = csv.reader(f)
	for row in reader:
		try:
			post = str(row[2]).strip()
			date = str(row[6]).strip()
			date = make_time(date)
			map_date[post] = date 
		except Exception as e:
			print('1: ', e)
with open('collusion_users.csv', 'r', encoding="utf8") as f:
	count = 0
	arr = []
	reader = csv.reader(f)
	for row in reader:
		a = []
		a.append(row[4])
		a.append(row[2])
		a.append(map_date[row[2]])
		a.append(row[1])
		a.append(row[0])
		arr.append(a)

sorted_list = sorted(arr, key=itemgetter(2))
c = csv.writer(open("like_data.csv", "w", newline=''))
for rowentry in sorted_list:
	try:
		c.writerow(rowentry)
	except:
		a = 1 #do nothing


