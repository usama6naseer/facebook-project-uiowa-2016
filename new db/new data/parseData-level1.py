collusion_networks = {}
collusion_network_users = {}
count_users_posts = {}
file_posts_repeat = open('file_posts_repeat.txt','w')
count_zero = 0
count_all = 0
#file_issues_posts = open('file_issues.txt','w')
with open('ResultOfAllPostsCrawledLevel1AfterCorrection.csv','r') as f:
	for line in f:
		#try:
		line.replace('\n','')
		#print line
		data = line.split(',[')
		data[1] = data[1].replace(']','')
		post_meta_data = data[0].split(',')
		post_users = data[1].split(',')
		#print data[1]
		#print data[0]
		collusion_network_name = post_meta_data[0]
		user_id = post_meta_data[1]
		post_id = post_meta_data[2]
		count_users = post_meta_data[3]
		if collusion_network_name not in collusion_networks:
			collusion_networks[collusion_network_name] = {}
		if post_id in collusion_networks[collusion_network_name]:
			file_posts_repeat.write(collusion_network_name+','+post_id+'\n')
		else:
			collusion_networks[collusion_network_name][post_id] = {}
		count_users = len(post_users)
		if count_users > 1000:
			print count_users
		
		if post_id in count_users_posts:
			if count_users > count_users_posts[post_id]:
				count_users_posts[post_id] = count_users
		else:
			count_users_posts[post_id] = count_users

		for user in post_users:
			collusion_networks[collusion_network_name][post_id][user] = user_id
		count_all += 1

		if collusion_network_name not in collusion_network_users:
			collusion_network_users[collusion_network_name] = {}
		else:
			collusion_network_users[collusion_network_name][user_id] = 1
		#except:
		#	print 'exception in ' + line
#count = 95
file_collusion_users = open('collusion_users.csv','w')
for collusion_network_name,posts in collusion_networks.iteritems():
	for post_id,users in posts.iteritems():
		post = post_id.split('_')
		post_id_only = post[1]
		#print len(users)
		for user_by,user_id in users.iteritems():
			user_by = user_by.replace('\n','')
			#if user_by == '':
			#	print 'crap'
			#	print collusion_network_name+','+user_id+','+post_id+','+post_id_only+','+user_by
			file_collusion_users.write(collusion_network_name+','+user_id+','+post_id+','+post_id_only+','+user_by+'\n')
# with open('file_users_report.txt','w') as f:
# 	for key,collusion_network in collusion_network_users.iteritems():
# 		f.write(key+','+str(len(collusion_network))+'\n')

# with open('likes_posts.txt','r') as f:
# 	for line in f:
# 		#try:
# 		line.replace('\n','')
# 		#print line
# 		data = line.split(',[')
# 		data[1] = data[1].replace(']','')
# 		post_meta_data = data[0].split(',')
# 		post_users = data[1].split(',')
# 		#print data[1]
# 		#print data[0]
# 		collusion_network_name = post_meta_data[0]
# 		user_id = post_meta_data[1]
# 		post_id = post_meta_data[2]
# 		count_users = post_meta_data[3]
		
# 		count_users = len(post_users)
		
		
# 		if count_users_posts[post_id] < 2:
# 			file_issues_posts.write(collusion_network_name+','+user_id+','+post_id+','+str(count_users)+'\n')
# 			count_zero += 1
		
		


# print count_zero
# print count_all
# #print collusion_networks
# #The whole process above seems slightly useless but it is done to make sure data of no one post repeats.
# #print len(collusion_networks['official-liker.net']['100000339803546_677761205578533'])
# del collusion_network_users
# collusion_network_users = {}
# for collusion_network_name,posts in collusion_networks.iteritems():
# 	for post_id,users in posts.iteritems():
# 		for user,val in users.iteritems():
# 			if collusion_network_name not in collusion_network_users:
# 				collusion_network_users[collusion_network_name] = {}
# 			collusion_network_users[collusion_network_name][user] = 1
# #print collusion_network_users
# file_upper_bound = open('ouput_upperbound.csv','w')
# for collusion_network_name,collusion_network in collusion_network_users.iteritems():
# 	count_users = len(collusion_network_users[collusion_network_name])
# 	file_upper_bound.write(collusion_network_name+','+str(count_users)+'\n')
# count_users_all = {}
# for collusion_network_name,collusion_network in collusion_network_users.iteritems():
# 	for key,val in collusion_network.iteritems():
# 		count_users_all[key] = 1
# print 'ALL USERS WITHOUT OVERLAP: ' + str(len(count_users_all))