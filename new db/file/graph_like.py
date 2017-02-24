import csv
import datetime
import time
from operator import itemgetter, attrgetter, methodcaller

net = []
hmap = dict()
posts = dict()
with open('like_data.csv', 'r', encoding="utf8") as f:
	reader = csv.reader(f)
	for row in reader:
		try:
			a1 = str(row[0])
			a2 = str(row[1])
			a3 = str(row[2])
			a4 = str(row[3])
			a5 = str(row[4])
			# a6 = str(row[5])
			# a7 = str(row[6])

			if a5 in hmap:
				if a2 in posts:
					num = posts[a2]
					posts[a2] = num + 1

				if a2 not in posts:
					posts[a2] = 1
					hmap[a5].append(a2)

			if a5 not in hmap:
				hmap[a5] = []
				net.append(a5)
				posts[a2] = 1
				hmap[a5].append(a2)
	
		except Exception as e:
			print("1: ", e)

	# print(net)		
	all_arr = []
	try:
		for i in net:
			arr = []
			# print(i)
			arr.append(i)
			for j in hmap[i]:
				arr.append(posts[j])
				# print(j)
				# print(posts[j])
			all_arr.append(arr)
	except Exception as e:
		print(e)

	# all_arr = sorted(all_arr, key=itemgetter(0), reverse=True)
	c = csv.writer(open("likes_per_post.csv", "w", newline=''))
	# c.writerow(["col_name","users","likes","comments","page_likes","date_created","present_date","days_passed"])
	for rowentry in all_arr:
		try:
			c.writerow(rowentry)
		except:
			a=1 #do nothing