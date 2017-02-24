import csv
import datetime
import time
from operator import itemgetter, attrgetter, methodcaller

def make_time(s):
	v = s.split('T')
	v1 = v[1].split('+')
	st = v[0] + ' ' + v1[0]
	return st

array = []
if  __name__ =='__main__':
	# with open('table.csv', 'r', encoding="utf8") as f:
	# 	reader = csv.reader(f)
	# 	for row in reader:
	# 		array.append(row)


	# sorted_data = sorted(array, key=itemgetter(1), reverse=True)
	# c = csv.writer(open("table_sorted.csv", "w", newline=''))
	# for rowentry in sorted_data:
	# 	try:
	# 		c.writerow(rowentry)
	# 	except:
	# 		a = 1 #do nothing


	hmap = dict()
	con = 0
	with open('collusion_users.csv', 'r', encoding="utf8") as f:
		reader = csv.reader(f)
		for row in reader:
			a5 = str(row[4])
			if a5 not in hmap:
				hmap[a5] = 1
				con = con + 1
	print("unique users: ", con)
	print("unique users: ", len(hmap))

