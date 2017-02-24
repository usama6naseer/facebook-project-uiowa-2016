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
		print ("In TIME")

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
for ai in range(0,50):
	try:
		a4 = "1000200789924" + str(ai)
		cursor.execute('INSERT INTO posts(post_id,user_id,post_text,post_date,number_likes,destination_id,time_stamp, month, day, time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
		(a4, a2, a5, 0, a7, a4, 0, timevec[0], timevec[1], timevec[2]))
		cnx.commit()
	except Exception as e:
		print (e)
		nn = 1
		print ("post already there")
				

cursor.close()
cnx.close()