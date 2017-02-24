import csv
import datetime
import time
import mysql.connector
from mysql.connector import errorcode


cnx = mysql.connector.connect(host="localhost", port=3306, user='root', password='password-0', database='fb_data')
# cnx = mysql.connector.connect(host="104.236.97.151", port=3306, user='collusion', password='iowa-lums', database='fb_data')
cursor = cnx.cursor()
with open('catBuser.csv', 'r', encoding="utf8") as f:
	reader = csv.reader(f)
	kl = 0;
	for row in reader:
		try:
			print(kl);
			kl = kl +1;
			a1 = str(row[0])
			a1 = a1.strip()
			a2 = str(row[1])
			a2 = a2.strip()
			try:
				cursor.execute('INSERT INTO category_b(user_id, col_name) VALUES (%s,%s)',
				(a1, a2))
				cnx.commit()
			except Exception as e:
				print (e)
				nn = 1
				print ("post already there")
			
		except Exception as e:
			print (e)
			print ("not utf8")


cursor.close()
cnx.close()