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
# 				(a2, "activity_tab", make_timestamp(a4)))
# 				cnx.commit()
# 			except Exception as e:
# 				nn = 1
# 				# print ("first", e)

# 			try:
# 				cursor.execute('INSERT INTO our_users(user_id, first_name, last_name, blocked, collusion_network_id, creation_time) VALUES (%s,%s,%s,%s,%s,%s)',
# 				(a1, "", "", 0, a2.strip(), make_timestamp(a4)))
# 				cnx.commit()
# 			except Exception as e:
# 				nn = 1
# 				# print ("first", e)

# 			try:
# 				cursor.execute('INSERT INTO collusion_networks(fb_page_id, name, time_stamp) VALUES (%s,%s,%s)',
# 				(a2.strip(), "", make_timestamp(a4)))
# 				cnx.commit()
# 			except Exception as e:
# 				nn = 1
# 				# print ("first", e)
	
# 		except Exception as e:
# 			nn = 1
# 			# print ("second", e)


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
# 				cursor.execute('INSERT INTO all_users(user_id, first_name, last_name) VALUES (%s,%s,%s)',
# 				(a3, a4, ""))
# 				cnx.commit()
# 			except Exception as e:
# 				nn = 1
# 				print (e)
# 				print ("user already present")
# 			try:
# 				timevec = get_mdt(a6)
# 				cursor.execute('INSERT INTO user_comments(user_id,post_id,comment_id,comment_text,post_type,time_stamp,month,day,time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',
# 				(a3, a5, a5, a7, 'text', 0, timevec[0], timevec[1], timevec[2]))
# 				cnx.commit()
# 			except Exception as e:
# 				nn = 1
# 				print (e)
# 				print ("comment already present")
# 			try:
# 				cursor.execute('INSERT INTO collusion_users (user_id, fb_page_id, time_stamp,month,day,time) VALUES (%s,%s,%s,%s,%s,%s)',
# 				(a3, a2.strip(), 0, st[0], st[1], st[2])) # give collusion network
# 				cnx.commit()
# 			except Exception as e:
# 				nn = 1
# 				print (e)
# 				print ("collusion user already present")

# 		except:
# 			nn = 1
# 			# print ("not utf8")

# with open('activity_tab_likes.csv', 'r', encoding="utf8") as f:
# 	reader = csv.reader(f)
# 	for row in reader:
# 		# print(fl)
# 		fl = fl+1
# 		print(fl)
# 		try:
# 			a1 = str(row[0])
# 			a2 = str(row[1])
# 			a3 = str(row[2])
# 			a4 = str(row[3])
# 			a5 = str(row[4])
# 			a6 = str(row[5])
# 			timevec = get_mdt(a6)
# 			if timevec[0] > 9:
# 				if timevec[1] > 11:
# 					print ("month is: " , timevec[0])
# 					print ("day is: " , timevec[1])
# 					print ("time is: " , timevec[2])
# 					try:
# 						cursor.execute('INSERT INTO all_users(user_id, first_name, last_name) VALUES (%s,%s,%s)',
# 						(a3, a4, ""))
# 						cnx.commit()
# 					except Exception as e:
# 						nn = 1
# 						print (e)
# 						print ("user already present")
# 					try:
# 						timevec = get_mdt(a6)
# 						cursor.execute('INSERT INTO user_likes(user_id,post_id,post_type,time_stamp,month,day,time) VALUES (%s,%s,%s,%s,%s,%s,%s)',
# 						(a3, a5, 'text', 0, timevec[0], timevec[1], timevec[2]))
# 						cnx.commit()
# 					except Exception as e:
# 						nn = 1
# 						print (e)
# 						print ("like already present")
# 					try:
# 						timevec = get_mdt(a6)
# 						cursor.execute('INSERT INTO activity_tab_likes(user_id,post_id,post_type,time_stamp,month,day,time) VALUES (%s,%s,%s,%s,%s,%s,%s)',
# 						(a3, a5, 'text', 0, timevec[0], timevec[1], timevec[2]))
# 						cnx.commit()
# 					except Exception as e:
# 						nn = 1
# 						print (e)
# 						print ("like already present")
					
# 					try:
# 						cursor.execute('INSERT INTO collusion_users (user_id, fb_page_id, time_stamp,month,day,time) VALUES (%s,%s,%s,%s,%s,%s)',
# 						(a3, a2.strip(), 0, st[0], st[1], st[2])) # give collusion network
# 						cnx.commit()
# 					except Exception as e:
# 						nn = 1
# 						print (e)
# 						print ("collusion user already present")

# 		except Exception as e:
# 			nn = 1
# 			print (e)
# 			print ("not utf8")



# # with open('page_likes.csv', 'r', encoding="utf8") as f:
# # 	reader = csv.reader(f)
# # 	for row in reader:
# # 		fl = fl+1
# # 		print(fl)
# # 		# print(fl)
# # 		try:
# # 			a1 = str(row[0])
# # 			a2 = str(row[1])
# # 			a3 = str(row[2])
# # 			a4 = str(row[3])
# # 			a5 = str(row[4])
# # 			a6 = str(row[5])
# # 			# day = datetime.datetime.now().date()
# # 			# current_time = datetime.datetime.now().time()	
# # 			# st = str(day) + ' ' + str(current_time)
			
# # 			try:
# # 				cursor.execute('INSERT INTO collusion_pages(page_id, name) VALUES (%s,%s)',
# # 				(a3, a4))
# # 				cnx.commit()
# # 			except Exception as e:
# # 				nn = 1
# # 				# print (e)
# # 				# print ("user already present")

# # 			try:
# # 				timevec = get_mdt(a6)
# # 				cursor.execute('INSERT INTO page_likes(page_id,user_id,post_id,time_stamp,month,day,time) VALUES (%s,%s,%s,%s,%s,%s,%s)',
# # 				(a3, a1, a5, 0, timevec[0], timevec[1], timevec[2]))
# # 				cnx.commit()
# # 			except Exception as e:
# # 				nn = 1
# # 				print (e)
# # 				print ("like already present")
			
# # 		except Exception as e:
# # 			nn = 1
# # 			# print (e)
# # 			# print ("not utf8")


cursor.execute('INSERT INTO all_users(user_id, first_name, last_name) VALUES (%s,%s,%s)',
("HELLO", "KKKKKKKKKKKKKKKKK", ""))
cnx.commit()

cursor.close()
cnx.close()