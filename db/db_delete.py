import datetime
import mysql.connector

cnx = mysql.connector.connect(host="104.236.97.151", port=3306, user='collusion', password='iowa-lums', database='fb_data')
# cnx = mysql.connector.connect(host="104.236.97.151", port=3306, user='collusion', password='iowa-lums', database='fb_test')
# cnx = mysql.connector.connect(user='root', password='password-0', database='fb_scraped_data')

cursor = cnx.cursor()

# query = ("TRUNCATE our_users;")
# cursor.execute(query)
query = ("TRUNCATE all_users;")
cursor.execute(query)
query = ("TRUNCATE collusion_users;")
cursor.execute(query)
# query = ("TRUNCATE object_crawled;")
# cursor.execute(query)
# query = ("TRUNCATE collusion_networks;")
# cursor.execute(query)
query = ("TRUNCATE posts;")
cursor.execute(query)
query = ("TRUNCATE user_likes;")
cursor.execute(query)
query = ("TRUNCATE user_comments;")
cursor.execute(query)
query = ("TRUNCATE page_likes;")
cursor.execute(query)
query = ("TRUNCATE page_comments;")
cursor.execute(query)

cursor.close()
cnx.close()