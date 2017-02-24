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
		# print (e)
		# print ("In TIME")
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
		# print (e)
		# print ("In new TIME")
		return time_time(st)

def time_time(st):
	try:
		v = st.split('-')
		v1 = v[2]
		s = v1[0] + v1[1]
		v2 = v1.split(':')
		v3 = v2[0].split('T')
		time = v3[1]
		# print([v[1], s, time])
		return [int(v[1]), int(s), int(time)]

	except Exception as e:
		ajk = 0
		# print("in new time time", e)

def make_timestamp(st):
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
		sd = str(year) + '-' + str(day) + '-' + str(month)
		tim = t2[2].split('p')[0]
		tim = tim.split('a')[0] + ":00.00"
		return (sd + ' ' + tim)
	except Exception as e:
		print (e)
		print ("Innnnnn TIME")

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

# day = datetime.datetime.now().date()
# current_time = datetime.datetime.now().time()	
# st = str(day) + ' ' + str(current_time)
day = datetime.datetime.now().date()
current_time = datetime.datetime.now().time()	
d = str(day).split('-')
st = [int(d[1]), int(d[2]), int(str(current_time).split(':')[0])]

		
# URL scrapped, Time of scrapping

# posterName,posterId,collusion_network,posturl,posttext,users_wholikedthepost,noOfLikes,Post_time,localtime_whenlikesCollected_y/m/d

with open('likesInfoOfPosts.csv', 'r', encoding="utf8") as f:
	reader = csv.reader(f)
	kl = 0;
	for row in reader:
		try:
			print(kl);
			kl = kl +1;
			a1 = str(row[0])
			a2 = str(row[1])
			a3 = str(row[2])
			a4 = str(row[3])
			a5 = str(row[4])
			a6 = row[5]
			a7 = str(row[6])
			a8 = str(row[7])
			a9 = str(row[8])

			# timevec = get_mdt(a8)
			timevec = 0
			try:
				timevec = get_mdt(a8)
			except:
				do=0

			try:
				query = 'DELETE FROM our_users WHERE user_id =' + a2
				cursor.execute(query)
				cnx.commit()
				# cursor.execute('INSERT INTO our_users(user_id, first_name, last_name, blocked, collusion_network_id, creation_time) VALUES (%s,%s,%s,%s,%s,%s)',
				# (a2, "", a1, 0, a3.strip(), 0))
				# cnx.commit()
			except Exception as e:
				nn = 1
				print ("OUR USER ERROR: ", e)


			try:
				cursor.execute('DELETE FROM posts WHERE user_id = %s and post_id = %s',
				(a2, a4))
				# query = 'DELETE FROM posts WHERE user_id =' + a2 ' and post_id =' + a4
				# cursor.execute(query)
				cnx.commit()
				# print("** ", timevec)
				# if timevec:
				# 	cursor.execute('INSERT INTO posts(post_id,user_id,post_text,post_date,number_likes,destination_id,time_stamp, month, day, time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
				# 	(a4, a2, a5, 0, a7, a4, 0, timevec[0], timevec[1], timevec[2]))
				# 	cnx.commit()
				# else:
				# 	cursor.execute('INSERT INTO posts(post_id,user_id,post_text,post_date,number_likes,destination_id,time_stamp, month, day, time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
				# 	(a4, a2, a5, 0, a7, a4, 0, 0,0,0))
				# 	cnx.commit()

			except Exception as e:
				print (e)
				# try:
				# 	if int(a7) > 0:
				# 		print("id: ", a4)
				# 		cursor.execute(('UPDATE posts SET number_likes=%s, month=%s, day=%s, time=%s WHERE post_id = %s'),(str(a7),timevec[0],timevec[1],timevec[2],str(a4)))
				# 		cnx.commit()
				# except Exception as e1:
				# 	nn = 1
				# 	print (e1)
				# 	print ("***POST UPDATE ERROR***")
				# print (e)
				nn = 1
				print ("post already there")
				

			# print (make_timestamp(a8))
			vec = a6.split('[')[1]
			vec = vec.split(']')[0]
			vec = vec.split(',')
			for b in vec:
				# break
				if b:
					# print("*** inside: ", kl);
					# kl = kl +1;

					b = str(b)
					vc = b.split("'")
					# print(vc)
					b = vc[1]
					# print(b)

					try:
						query = 'DELETE FROM all_users WHERE user_id =' + b
						cursor.execute(query)
						# cursor.execute('INSERT INTO all_users(user_id, first_name, last_name) VALUES (%s,%s,%s)',
						# (b, "", ""))
						cnx.commit()
					except Exception as e:
						print (e)
						nn = 1
						print ("user already present")
					
					try:
						cursor.execute('DELETE FROM collusion_users WHERE user_id = %s and fb_page_id = %s',
							(b, a3.strip()))
						# cursor.execute('INSERT INTO collusion_users(user_id, fb_page_id, time_stamp, month, day, time) VALUES (%s,%s,%s,%s,%s,%s)',
						# (b, a3.strip(), 0, st[0], st[1], st[2])) # give collusion network
						cnx.commit()
					except Exception as e:
						print (e)
						nn = 1
						print ("collusion user already present")

					try:
						cursor.execute('DELETE FROM user_likes WHERE user_id = %s and post_id = %s',
							(b, a4))
						# cursor.execute('INSERT INTO user_likes(user_id,post_id,post_type,time_stamp, month, day, time) VALUES (%s,%s,%s,%s,%s,%s,%s)',
						# (b, a4, 'text', 0, st[0], st[1], st[2]))
						cnx.commit()
					except Exception as e:
						print (e)
						print ("like already present")
						nn = 1
			
		except Exception as e:
			print (e)
			print ("not utf8")


cursor.close()
cnx.close()