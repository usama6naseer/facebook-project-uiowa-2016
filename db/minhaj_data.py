import csv
import datetime
import time
import mysql.connector
from mysql.connector import errorcode



def get_mdt(st):
	# st = "Friday, March 13, 2015 at 11:47am"
	# st.replace(" ", "")
	try:
		# print("Start")
		t = st.split(',')
		for i in range(0, len(t)):
			t[i] = t[i].strip()
		# print ("1   ", t)
		t1 = t[1].split(' ')
		t2 = t[2].split(' ')
		tm = [t[0] , t1[0] , t1[1] , t2[0]]
		# print ("2   ", tm)
		month = 0
		day = tm[2].strip() 
		year = tm[3].strip()
		mn = tm[1].strip()
		if mn == 'January':
			month = 1
		elif mn == 'February':
			month = 2
		elif mn == 'March':
			month = 3
		elif mn == 'April':
			month = 4
		elif mn == 'May':
			month = 5
		elif mn == 'June':
			month = 6
		elif mn == 'July':
			month = 7
		elif mn == 'August':
			month = 8
		elif mn == 'September':
			month = 9
		elif mn == 'October':
			month = 10
		elif mn == 'November':
			month = 11  
		else:
			month = 12

		time = t2[2];
		# print(time)
		# print(len(time.split('p')))
		if len(time.split('p'))>1:
			tp = int(time.split(':')[0]) + 12
		else:
			tp = int(time.split(':')[0])
		return [month, int(day), tp]
	except Exception as e:
		print (e)
		print ("In TIME")
		return get_mdt_new(st)


def get_mdt_new(st):
# Tuesday, 1 December 2015 at 09:32
	try:
		# print("Start")
		t = st.split(',')
		for i in range(0, len(t)):
			t[i] = t[i].strip()
		# print ("1   ", t)
		t1 = t[1].split(' ')
		# t2 = t[2].split(' ')
		tm = [t[0] , t1[0] , t1[1] , t1[2]]
		# print ("2   ", tm)
		month = 0
		day = tm[1].strip() 
		year = tm[3].strip()
		mn = tm[2].strip()
		if mn == 'January':
			month = 1
		elif mn == 'February':
			month = 2
		elif mn == 'March':
			month = 3
		elif mn == 'April':
			month = 4
		elif mn == 'May':
			month = 5
		elif mn == 'June':
			month = 6
		elif mn == 'July':
			month = 7
		elif mn == 'August':
			month = 8
		elif mn == 'September':
			month = 9
		elif mn == 'October':
			month = 10
		elif mn == 'November':
			month = 11  
		else:
			month = 12

		time = t1[4];
		# print(time)
		# print(len(time.split('p')))
		if len(time.split('p'))>1:
			tp = int(time.split(':')[0]) + 12
		else:
			tp = int(time.split(':')[0])
		return [month, int(day), tp]
	except Exception as e:
		print (e)
		print ("In new TIME")
		return get_mdt_new_new(st)

def get_mdt_new_new(st):
	try:
		# print("Start")
		t = st.split(',')
		for i in range(0, len(t)):
			t[i] = t[i].strip()
		# print ("1   ", t)
		t1 = t[1].split(' ')
		t2 = t[2].split(' ')
		tm = [t[0] , t1[1] , t1[0] , t2[0]]
		# print ("2   ", tm)
		month = 0
		day = tm[2].strip() 
		year = tm[3].strip()
		mn = tm[1].strip()
		if mn == 'January':
			month = 1
		elif mn == 'February':
			month = 2
		elif mn == 'March':
			month = 3
		elif mn == 'April':
			month = 4
		elif mn == 'May':
			month = 5
		elif mn == 'June':
			month = 6
		elif mn == 'July':
			month = 7
		elif mn == 'August':
			month = 8
		elif mn == 'September':
			month = 9
		elif mn == 'October':
			month = 10
		elif mn == 'November':
			month = 11  
		else:
			month = 12

		time = t2[2];
		# print(time)
		# print(len(time.split('p')))
		if len(time.split('p'))>1:
			tp = int(time.split(':')[0]) + 12
		else:
			tp = int(time.split(':')[0])
		return [month, int(day), tp]
	except Exception as e:
		print (e)
		print ("In new new TIME")
		# return get_mdt_new(st)


def make_timestamp(st):
	# st = "Friday, March 13, 2015 at 11:47am"
	# st.replace(" ", "")
	t = st.split(',')
	for i in range(0, len(t)):
		t[i] = t[i].strip()
	# print (t)
	t1 = t[1].split(' ')
	t2 = t[2].split(' ')
	tm = [t[0] , t1[0] , t1[1] , t2[0]]
	# print (tm)
	month = 0
	day = tm[2].strip() 
	year = tm[3].strip()
	mn = tm[1].strip()
	if mn == 'January':
		month = 1
	elif mn == 'February':
		month = 2
	elif mn == 'March':
		month = 3
	elif mn == 'April':
		month = 4
	elif mn == 'May':
		month = 5
	elif mn == 'June':
		month = 6
	elif mn == 'July':
		month = 7
	elif mn == 'August':
		month = 8
	elif mn == 'September':
		month = 9
	elif mn == 'October':
		month = 10
	elif mn == 'November':
		month = 11
	else:
		month = 12
	sd = str(year) + '-' + str(day) + '-' + str(month)
	tim = t2[2].split('p')[0]
	tim = tim.split('a')[0] + ":00.00"
	return (sd + ' ' + tim)

	# return time.mktime(datetime.datetime.strptime(sd, "%d/%m/%Y").timetuple())

def make_time(s):
	day = datetime.datetime.now().date()
	st = str(day) + ' ' + s
	# dt = datetime.datetime.strptime(st, "%Y-%m-%d %H:%M:%S.%f")
	# new_time = time.mktime(dt.timetuple())
	# return new_time
	return st

def get_page(s):
	s1 = s.split('/')
	return (s1[3].split('?')[0])

cnx = mysql.connector.connect(host="localhost", port=3306, user='root', password='password-0', database='fb_data')
# cnx = mysql.connector.connect(host="104.236.97.151", port=3306, user='collusion', password='iowa-lums', database='fb_data')
cursor = cnx.cursor()
fl = 0;
# day = datetime.datetime.now().date()
# current_time = datetime.datetime.now().time()	
# st = str(day) + ' ' + str(current_time)
day = datetime.datetime.now().date()
current_time = datetime.datetime.now().time()	
d = str(day).split('-')
st = [int(d[1]), int(d[2]), int(str(current_time).split(':')[0])]


# # URL scrapped, Time of scrapping
# with open('activity_log_record.csv', 'r', encoding="utf8") as f:
# 	reader = csv.reader(f)
# 	for row in reader:
# 		fl = fl+1
# 		print(fl)

# 		try:
# 			a1 = str(row[0])
# 			a2 = str(row[1])
# 			a3 = str(row[2])
# 			a4 = str(row[3])
# 			# print(row)
# 			try:
# 				cursor.execute('INSERT INTO object_crawled(object_id, object_type, time_stamp) VALUES (%s,%s,%s)',
# 				(a2, "tab", 0))
# 				cnx.commit()
# 			except Exception as e:
# 				nn = 1
# 				# print ("first1", e)

# 			try:
# 				cursor.execute('INSERT INTO our_users(user_id, first_name, last_name, blocked, collusion_network_id, creation_time) VALUES (%s,%s,%s,%s,%s,%s)',
# 				(a1, "", "", 0, a2.strip(), 0))
# 				cnx.commit()
# 			except Exception as e:
# 				nn = 1
# 				# print ("first2", e)

# 			try:
# 				cursor.execute('INSERT INTO collusion_networks(fb_page_id, name, time_stamp) VALUES (%s,%s,%s)',
# 				(a2.strip(), "", 0))
# 				cnx.commit()
# 			except Exception as e:
# 				nn = 1
# 				# print ("first3", e)
	
# 		except Exception as e:
# 			nn = 1
# 			# print ("second4", e)


# with open('activity_tab_comments.csv', 'r', encoding="utf8") as f:
# 	reader = csv.reader(f)
# 	for row in reader:
# 		fl = fl+1
# 		print(fl)
# 		try:
# 			a1 = str(row[0])
# 			a2 = str(row[1])
# 			a3 = str(row[2]) #profile ID
# 			a4 = str(row[3])
# 			a5 = str(row[4])
# 			a6 = str(row[5])
# 			a7 = str(row[6])
# 			# a8 = str(row[7])
# 			# day = datetime.datetime.now().date()
# 			# current_time = datetime.datetime.now().time()	
# 			# st = str(day) + ' ' + str(current_time)

# 			try:
# 				timevec = get_mdt(a6)
# 				cursor.execute('INSERT INTO posts(post_id,user_id,post_text,post_date,number_likes,destination_id,time_stamp, month, day, time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
# 				(a5.strip(), a3, "",0 , -1, a3, 0, timevec[0], timevec[1], timevec[2]))
# 				cnx.commit()
# 			except Exception as e:
# 				print (e)
# 				nn = 1
# 				print ("post already there")
			# try:
			# 	cursor.execute('INSERT INTO all_users(user_id, first_name, last_name) VALUES (%s,%s,%s)',
			# 	(a3, "", ""))
			# 	cnx.commit()
			# except Exception as e:
			# 	nn = 1
			# 	print (e)
			# 	# print ("user already present check 1")
			# try:
			# 	timevec = get_mdt(a6)
			# 	cursor.execute('INSERT INTO user_comments(user_id,post_id,comment_id,comment_text,post_type,time_stamp,month,day,time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',
			# 	(a3, a5, a5, a7, 'text', 0, timevec[0], timevec[1], timevec[2]))
			# 	cnx.commit()
			# except Exception as e:
			# 	nn = 1
			# 	print (e)
			# 	# print ("comment already present check 2")
			# try:
			# 	cursor.execute('INSERT INTO collusion_users (user_id, fb_page_id, time_stamp,month,day,time) VALUES (%s,%s,%s,%s,%s,%s)',
			# 	(a3, a2.strip(), 0, st[0], st[1], st[2])) # give collusion network
			# 	cnx.commit()
			# except Exception as e:
			# 	nn = 1
			# 	print (e)
			# 	# print ("collusion user already present check 3")

		# except:
		# 	nn = 1
		# 	# print ("not utf8")

with open('activity_tab_likes.csv', 'r', encoding="utf8") as f:
	reader = csv.reader(f)
	for row in reader:
		# print(fl)
		try:
			a1 = str(row[0])
			a1 = a1.strip()
			a2 = str(row[1])
			a2 = a2.strip()
			a3 = str(row[2])
			a3 = a3.strip()
			a4 = str(row[3])
			a4 = a4.strip()
			a5 = str(row[4])
			a5 = a5.strip()
			a6 = str(row[5])
			a6 = a6.strip()
			# timevec = get_mdt(a6)
			if 10 > 9:
				if 12 > 11:
					fl = fl+1
					print(fl)

					try:
						timevec = get_mdt(a6)
						# print(timevec)
						cursor.execute('INSERT INTO posts(post_id,user_id,post_text,post_date,number_likes,destination_id,time_stamp, month, day, time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
						(a5.strip(), a3, "",0 , -1, a3, 0, timevec[0], timevec[1], timevec[2]))
						cnx.commit()
					except Exception as e:
						# print (e)
						nn = 1
						# print ("post already there")

					# print ("month is: " , timevec[0])
					# print ("day is: " , timevec[1])
					# print ("time is: " , timevec[2])
					try:
						cursor.execute('INSERT INTO all_users(user_id, first_name, last_name) VALUES (%s,%s,%s)',
						(a3.strip(), "", ""))
						cnx.commit()
					except Exception as e:
						nn = 1
						# print (e)
						# print ("user already present check 4")
					try:
						timevec = get_mdt(a6)
						cursor.execute('INSERT INTO user_likes(user_id,post_id,post_type,time_stamp,month,day,time) VALUES (%s,%s,%s,%s,%s,%s,%s)',
						(a3.strip(), a5.strip(), 'text', 0, timevec[0], timevec[1], timevec[2]))
						cnx.commit()
					except Exception as e:
						nn = 1
						# print (e)
						# print ("like already present check 5")
					try:
						timevec = get_mdt(a6)
						cursor.execute('INSERT INTO activity_tab_likes(user_id,post_id,post_type,time_stamp,month,day,time,our_user) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',
						(a3.strip(), a5.strip(), 'text', 0, timevec[0], timevec[1], timevec[2], a1))
						cnx.commit()
					except Exception as e:
						nn = 1
						# print (e)
						# print ("like already present check 6")
					
					try:
						cursor.execute('INSERT INTO collusion_users (user_id, fb_page_id, time_stamp,month,day,time) VALUES (%s,%s,%s,%s,%s,%s)',
						(a3.strip(), a2.strip(), 0, st[0], st[1], st[2])) # give collusion network
						cnx.commit()
					except Exception as e:
						nn = 1
						# print (e)
						# print ("collusion user already present check 7")

		except Exception as e:
			nn = 1
			print (e)
			print ("not utf8")



with open('page_likes.csv', 'r', encoding="utf8") as f:
	reader = csv.reader(f)
	for row in reader:
		fl = fl+1
		print(fl)
		# print(fl)
		try:
			a1 = str(row[0])
			a2 = str(row[1])
			a3 = str(row[2])
			a4 = str(row[3])
			a5 = str(row[4])
			a6 = str(row[5])
			day = datetime.datetime.now().date()
			current_time = datetime.datetime.now().time()	
			st = str(day) + ' ' + str(current_time)
			
			try:
				cursor.execute('INSERT INTO collusion_pages(page_id, name) VALUES (%s,%s)',
				(a3.strip(), ""))
				cnx.commit()
			except Exception as e:
				nn = 1
				print (e)
				print ("user already present check 8")

			try:
				timevec = get_mdt(a6)
				cursor.execute('INSERT INTO page_likes(page_id,user_id,post_id,time_stamp,month,day,time) VALUES (%s,%s,%s,%s,%s,%s,%s)',
				(a3.strip(), a1.strip(), a5.strip(), 0, timevec[0], timevec[1], timevec[2]))
				cnx.commit()
			except Exception as e:
				nn = 1
				print (e)
				print ("like already present check 9")
			
		except Exception as e:
			nn = 1
			print (e)
			print ("not utf8")




cursor.close()
cnx.close()