file_correction = open('ResultOfAllPostsCrawledLevel1AfterCorrection.csv','w')
count_autolikesub = 0
count_postliker = 0
with open('ResultOfAllPostsCrawledLevel1.csv','r') as f:
	for line in f:
		#line = line.replace('\n','')
		words = line.split(',')
		collusion_network = words[0]
		user_id = words[1]
		if user_id == '100010461645120':
			line = line.replace('autolikesub.com','postlikers.com')
			count_postliker += 1
		if user_id == '100010377152843':
			line = line.replace('postlikers.com','autolikesub.com')
			count_autolikesub += 1
		file_correction.write(line)
print count_autolikesub
print count_postliker