import csv
import datetime
import time
import mysql.connector
from mysql.connector import errorcode

with open('postscrawled.csv', 'r', encoding="utf8") as f:
# with open('ResultOfAllPostsCrawledLevel1AfterCorrection.csv', 'r', encoding="utf8") as f:
	cn = 0
	cn1 = 0
	hm = dict()
	reader = csv.reader(f)
	for row in reader:
		try:
			likes_vec = []
			try:
				for i in range(4, len(row)):
					nc = ''
					if i == 4:
						nc = row[i].split('[')[1]
					elif i == len(row)-1:
						nc = row[i].split(']')[0]
						# print("last: ", nc)
					else:
						nc = row[i]
					likes_vec.append(nc)
			except Exception as newe:
				ahj=1

			# print(likes_vec[0], ' ', likes_vec[len(likes_vec)-1])
			for like in likes_vec:
				# cn1 = cn1 + 1
				if like not in hm:
					hm[like] = 1
					cn = cn + 1

		except Exception as e:
			print('2: ', e)
	print(cn)
	print(len(hm))
