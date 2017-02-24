import csv
import datetime
import time
import mysql.connector
from mysql.connector import errorcode

def make_time(s):
	v = s.split('T')
	v1 = v[1].split('+')
	st = v[0] + ' ' + v1[0]
	return st

# cnx = mysql.connector.connect(host="localhost", port=3306, user='root', password='password-0', database='new_db')
# cursor = cnx.cursor()

map_date = dict()
with open('usersposts.csv', 'r', encoding="utf8") as f:
	reader = csv.reader(f)
	for row in reader:
		try:
			post = str(row[2]).strip()
			date = str(row[6]).strip()
			date = make_time(date)
			map_date[post] = date 
		except Exception as e:
			print('1: ', e)

with open('postscrawled.csv', 'r', encoding="utf8") as f:
	count = 0
	tr = 100
	reader = csv.reader(f)

	total_col_user = 0

	post_insert = ''
	like_insert = ''
	user_insert = ''
	col_user_insert = ''
	our_insert = ''

	for row in reader:
		try:
			count = count + 1
			# if count > 10:
				# break;
			if count == tr:
				print(count)
				tr = tr + 1000
			net = str(row[0]).strip()
			user = str(row[1]).strip()
			post = str(row[2]).strip()
			num = str(row[3]).strip()
			likes = row[4]

			# post string
			try:
				date = map_date[post]
				temp = '(' + "'" + post + "'" + ',' + num + ',' + "'" + net + "'" + ',' + "'" + date + "'" + ',' + "'" + user + "'" + ')'
				if count > 1:
					post_insert = post_insert + ','
					post_insert = post_insert + temp
				else:
					post_insert = post_insert + temp
			except Exception as e1:
				print('post: ', e1)

			# col user string
			temp = '(' + "'" + user + "'" + ',' + "'" + net + "'" + ')'
			if count > 1:
				user_insert = user_insert + ','
				user_insert = user_insert + temp
			else:
				user_insert = user_insert + temp

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
				print("likes vector: ", newe)
			
			# cn = 0
			# print(likes_vec)
			# print(len(likes_vec))
			# print(len(row))

			for like in likes_vec:
				# cn = cn + 1
				# print(cn, ' ', like)
				like = like.strip()
				
				temp = '(' + "'" + like + "'" + ',' + "'" + net + "'" + ')'
				total_col_user = total_col_user + 1
				if count > 1:
					col_user_insert = col_user_insert + ','
					col_user_insert = col_user_insert + temp
				else:
					col_user_insert = col_user_insert + temp

				temp = '(' + "'" + like + "'" + ',' + "'" + post + "'" + ',' + "'" + user + "'" + ',' + "'" + net + "'" + ',' + "'" + date + "'" + ')'
				if count > 1:
					like_insert = like_insert + ','
					like_insert = like_insert + temp
				else:
					like_insert = like_insert + temp
					count = count + 1 

		except Exception as e:
			print('2: ', e)

	try:
		f = open("result.txt","w")
		f.write(post_insert)
		f.write(our_insert)
		f.write(col_user_insert)
		f.write(like_insert)
		f.write(user_insert)
		f.close()
	except:
		a = 0
		pass

	cnx = mysql.connector.connect(host="localhost", port=3306, user='root', password='password-0', database='new_db')
	cursor = cnx.cursor()

	# print(post_insert)
	try:
		query = 'INSERT IGNORE INTO posts(posts_id,number_likes,user_col_net,date,user_id) VALUES' + post_insert
		# print(query)
		cursor.execute(query)
		cnx.commit()
	except Exception as e1:
		print('post insert: ', e1)

	# print(user_insert)
	try:
		query = 'INSERT IGNORE INTO our_users(user_id,collusion_network_id) VALUES' + user_insert
		# print(query)
		cursor.execute(query)
		cnx.commit()
	except Exception as e1:
		print('our user insert: ', e1)

	# print(col_user_insert)
	try:
		query = 'INSERT IGNORE INTO collusion_users(user_id,fb_page_id) VALUES' + col_user_insert
		# print(query)
		cursor.execute(query)
		cnx.commit()
	except Exception as e1:
		print('col user insert: ', e1)

	# print(like_insert)
	try:
		query = 'INSERT IGNORE INTO user_likes(user_id,post_id,post_user_id,post_col_net,date) VALUES' + like_insert
		# print(query)
		cursor.execute(query)
		cnx.commit()
	except Exception as e1:
		print('like insert: ', e1)

	# print(total_col_user)
	cursor.close()
	cnx.close()