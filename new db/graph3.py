import csv
import datetime
import time
import mysql.connector
from mysql.connector import errorcode
from operator import itemgetter, attrgetter, methodcaller

def get_name(s):
	s = s.split('.')
	# print("s    ", s)
	name = s[(len(s)-2)]
	v = name.split('/')
	if len(v)>2:
		name = v[2] 
	end = s[(len(s)-1)]
	end = end.split('/')[0]
	# print("***** ", name + '.' + end)
	return name + '.' + end

def get_date(d, pre):
	v = d.split('-')
	if (v[1] == "10"):
		return (31-int(v[0]) + pre)
	if (v[1] == "9"):
		return (30-int(v[0]) + 31 + pre)


cnx = mysql.connector.connect(host="localhost", port=3306, user='root', password='password-0', database='fb_data')
cursor = cnx.cursor()
try:
	hashmap_users = dict()
	hashmap_likes = dict()
	hashmap_comments = dict()
	hashmap_page_likes = dict()
	hashmap_date = dict()
	col_name = []
	col_users = []

	cursor.execute('SELECT fb_page_id, count(*) FROM collusion_users group by fb_page_id order by fb_page_id asc')
	for i in cursor:
		name = get_name(i[0].strip())
		if name in hashmap_users:
			pre = hashmap_users[name]
			new = pre + i[1]
			hashmap_users[name] = new
		if name not in hashmap_users:
			hashmap_users[name] = i[1]
			col_name.append(name)
		# print(i[0], ' ', i[1])
		# print(hashmap_users[i[0]])
	# 	col_users.append(i[1])
	# print(col_name)
	# print(col_users)
	
	cursor.execute('SELECT collusion_users.fb_page_id, count(*) FROM fb_data.user_likes left join collusion_users on user_likes.user_id=collusion_users.user_id group by collusion_users.fb_page_id order by collusion_users.fb_page_id')
	for i in cursor:
		try:
			name = get_name(i[0].strip())
			if name in hashmap_likes:
				pre = hashmap_likes[name]
				new = pre + i[1]
				hashmap_likes[name] = new
			if name not in hashmap_likes:
				hashmap_likes[name] = i[1]

			# hashmap_likes[name] = i[1]
		except:
			pass
		# print(i[0], ' ', i[1])
		# print(hashmap_likes[i[0]])

	cursor.execute('SELECT collusion_users.fb_page_id, count(*) FROM fb_data.user_comments left join collusion_users on user_comments.user_id=collusion_users.user_id group by collusion_users.fb_page_id;')
	for i in cursor:
		try:
			name = get_name(i[0].strip())
			if name in hashmap_comments:
				pre = hashmap_comments[name]
				new = pre + i[1]
				hashmap_comments[name] = new
			if name not in hashmap_comments:
				hashmap_comments[name] = i[1]

			# hashmap_comments[name] = i[1]
		except:
			pass	
		# print(i[0], ' ', i[1])
		# print(hashmap_comments[i[0]])


	cursor.execute('SELECT collusion_network_id, count(*) FROM page_likes left join our_users on page_likes.user_id=our_users.user_id group by collusion_network_id;')
	for i in cursor:
		try:
			name = get_name(i[0].strip())
			if name in hashmap_page_likes:
				pre = hashmap_page_likes[name]
				new = pre + i[1]
				hashmap_page_likes[name] = new
			if name not in hashmap_page_likes:
				hashmap_page_likes[name] = i[1]

			# hashmap_page_likes[name] = i[1]
		except:
			pass
		# print(i[0], ' ', i[1])
		# print(hashmap_page_likes[i[0]])

	cursor.execute('SELECT col_name, month, day FROM date_created;')
	for i in cursor:
		try:
			name = get_name(i[0].strip())
			hashmap_date[name] = [i[1],i[2]]
		except:
			pass
		

	data_all = []
	for i in col_name:
		data = []
		data.append(i)
		try:
			data.append(hashmap_users[i])
		except:
			data.append(0)
		try:
			data.append(hashmap_likes[i])
		except:
			data.append(0)
		try:
			data.append(hashmap_comments[i])
		except:
			data.append(0)
		try:
			data.append(hashmap_page_likes[i])
		except:
			data.append(0)
		try:
			b = hashmap_date[i]
			d = str(b[1]) + '-' + str(b[0]) + '-' + "2015"
			data.append(d)
			data.append("10-12-2015")
			present = get_date(d,40)
			data.append(present)
		except:
			data.append("0-0-0")
			data.append("0-0-0")
			data.append(0)


		data_all.append(data)

	sorted_data = sorted(data_all, key=itemgetter(1), reverse=True)
	c = csv.writer(open("table.csv", "w", newline=''))
	c.writerow(["col_name","users","likes","comments","page_likes","date_created","present_date","days_passed"])
	for rowentry in sorted_data:
		try:
			c.writerow(rowentry)
		except:
			a=1 #do nothing

except Exception as e:
	print (e)
	nn = 1					

cursor.close()
cnx.close()
