import csv
import datetime
import time
from operator import itemgetter, attrgetter, methodcaller

def make_time(s):
	v = s.split('T')
	v1 = v[1].split('+')
	st = v[0] + ' ' + v1[0]
	return st

if  __name__ =='__main__':
	cn = 0;
	tr = 5000;
	array = []
	net = []
	hmap_users = dict()
	hmap_users_num = dict()
	hmap_likes = dict()
	hmap_posts = dict()
	hmap_all_users = dict()
	hmap_all_posts = dict()
	with open('collusion_users.csv', 'r', encoding="utf8") as f:
		reader = csv.reader(f)
		for row in reader:
			try:
				cn = cn + 1;
				if cn == tr:
					print(cn)
					tr = tr + 5000
				a1 = str(row[0])
				a2 = str(row[1])
				a3 = str(row[2])
				a4 = str(row[3])
				a5 = str(row[4])

				# if a1 not in net:
					# net.append(a1)
				# USERS
				if a1 not in hmap_users:
					net.append(a1)
					hmap_users[a1] = []
					hmap_users[a1].append(a5)
					hmap_users_num[a1] = 1

				vec = hmap_users[a1]
				if a5 not in vec:
					num = hmap_users_num[a1]
					hmap_users_num[a1] = num + 1
					hmap_users[a1].append(a5)

				# LIKES
				if a1 not in hmap_likes:
					hmap_likes[a1] = 0
				if a1 in hmap_likes:
					num = hmap_likes[a1]
					hmap_likes[a1] = num + 1
				
				# POSTS
				if a1 not in hmap_posts:
					hmap_posts[a1] = 0
				if a3 not in hmap_all_posts:
					hmap_all_posts[a3] = 1
					num = hmap_posts[a1]
					hmap_posts[a1] = num + 1

			except Exception as e:
				print("1: ", e)

	try:
		f = open("result.txt","w")
		f.write(hmap_posts)
		f.write(hmap_likes)
		f.write(hmap_users_num)
		f.close()
	except:
		a = 0
		pass



	# array.append("name","users","posts","likes")
	for i in net:
		arr = []
		arr.append(i)
		arr.append(hmap_users_num[i])
		arr.append(hmap_posts[i])
		arr.append(hmap_likes[i])
		# print(i,' ',hmap_users_num[i],hmap_posts[i],hmap_likes[i])
		array.append(arr)

	c = csv.writer(open("table.csv", "w", newline=''))
	for rowentry in array:
		try:
			c.writerow(rowentry)
		except:
			a = 1 #do nothing

