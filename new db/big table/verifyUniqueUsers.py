collusion_networks = {}
collusion_network_users = {}
count_users_posts = {}
#file_posts_repeat = open('file_posts_repeat.txt','w')
count_zero = 0
count_all = 0
#file_issues_posts = open('file_issues.txt','w')
users_all = {}
cn=0;
with open('ResultOfAllPostsCrawledLevel1AfterCorrection.csv','r') as f:
	for line in f:
		#try:
		line.replace('\n','')
		#print line
		data = line.split(',[')
		# data[1] = data[1].replace(']','')
		data[1] = data[1].split(']')[0]
		post_meta_data = data[0].split(',')
		post_users = data[1].split(',')
		# print(post_users[0],' * ',post_users[len(post_users)-1])
		#print data[1]
		#print data[0]

		# collusion_network_name = post_meta_data[0]
		# user_id = post_meta_data[1]
		# post_id = post_meta_data[2]
		# count_users = post_meta_data[3]

		for user in post_users:
			# if user not in users_all:
				# if user is not '':
					# cn = cn + 1
			# print(user)
			users_all[user] = 1
			
		count_all += 1
print (len(users_all))
print(cn)
# print (users_all)