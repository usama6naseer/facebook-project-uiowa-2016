import csv
import datetime
import time
from operator import itemgetter, attrgetter, methodcaller

hmap = dict()
array = []
page = dict()
user = dict()
if  __name__ =='__main__':
	with open('page_likes.csv', 'r', encoding="utf8") as f:
		reader = csv.reader(f)
		for row in reader:
			if row[0] not in hmap:
				array.append(row[0])
				hmap[row[0]] = 0
				user[row[0]] = []
			if row[0] in hmap:
				vec = user[row[0]]
				if row[1] not in vec:
					vec.append(row[1])
					user[row[0]] = vec
					hmap[row[0]] = hmap[row[0]] + 1

	a1 = []
	for i in array:
		print(i, ' ', hmap[i])
		a2 = []
		a2.append(i)
		a2.append(hmap[i])
		a1.append(a2)


	# sorted_data = sorted(array, key=itemgetter(1), reverse=True)
	c = csv.writer(open("table_sorted.csv", "w", newline=''))
	for rowentry in a1:
		try:
			c.writerow(rowentry)
		except:
			a = 1 #do nothing


	# hmap = dict()
	# con = 0
	# with open('collusion_users.csv', 'r', encoding="utf8") as f:
	# 	reader = csv.reader(f)
	# 	for row in reader:
	# 		a5 = str(row[4])
	# 		if a5 not in hmap:
	# 			hmap[a5] = 1
	# 			con = con + 1
	# print("unique users: ", con)
	# print("unique users: ", len(hmap))

