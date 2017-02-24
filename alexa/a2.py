# http://www.alexa.com/siteinfo/autolikeviet.vn
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from operator import itemgetter, attrgetter, methodcaller

all_arr= []
f = open('net1.txt', 'r')
x = f.readlines()
c = csv.writer(open("table.csv", "a", newline=''))
c.writerow(["Collusion Network","App","App ID","Worldwide Rank","Country","Usage Percent","Country Rank"])

for r in x:
	driver = webdriver.Firefox()
	arr = []
	try:
		row = r.split(',')
		arr.append(row[0])
		arr.append(row[1])
		arr.append(row[2])
		print(row[0])
		# driver = webdriver.Firefox()
		driver.get("http://www.alexa.com/siteinfo/" + row[0].strip())
		time.sleep(1)
		rank = driver.find_element_by_class_name("rank-row")
		st = rank.text
		st = st.split("Rank")[1]
		st = st.split(' ')
		rank = st[len(st)-2]
		print("rank: ", rank.strip())
		arr.append(rank.strip())

		try:
			v1 = driver.find_element_by_id("visitors-content")
			v2 = v1.find_elements_by_tag_name("span")
			for v3 in v2:
				if v3.get_attribute("class") == "span-col last":
					print("in there")
					# country = v3.find_element_by_tag_name("a").text
					# country = country.strip()
					# print("country: ", country)

					v4 = v3.find_elements_by_tag_name("td")
					country = v4[0].find_element_by_tag_name("a").text
					country = country.strip()
					cper = v4[1].find_element_by_tag_name("span").text
					cper = cper.strip()
					crank = v4[2].find_element_by_tag_name("span").text
					crank = crank.strip()
					arr.append(country)
					arr.append(cper)
					arr.append(crank)
					print(country)
					print(cper)
					print(crank)
					# print(v4[0].find_element_by_tag_name("a").text)
					# print(v4[1].find_element_by_tag_name("span").text)
					# print(v4[2].find_element_by_tag_name("span").text)
					c = csv.writer(open("table.csv", "a", newline=''))
					c.writerow(arr)


		except Exception as e:
			print("exception in country")
			print(e)
			arr.append('null')
			arr.append('null')
			arr.append('null')
			c = csv.writer(open("table.csv", "a", newline=''))
			c.writerow(arr)

		driver.quit()

	except Exception as e:
		print(e)
		print("NOOOOOOOOO")
		driver.quit()
# sorted_data = sorted(data_all, key=itemgetter(1), reverse=True)
# c = csv.writer(open("table.csv", "w", newline=''))
# c.writerow(["Collusion Network","App","App ID","Worldwide Rank","Country","Country Rank"])
# for rowentry in all_arr:
# 	try:
# 		c.writerow(rowentry)
# 	except:
# 		a=1 #do nothing

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# import csv

# def goAndLoginToFB(driver,url):
# 	driver.get(url)
# 	# time.sleep(5)
# 	# emailInput = driver.find_element_by_xpath('//*[@id="email"]')
# 	# emailInput.send_keys("usama94naseer@gmail.com")
# 	# passwordInput = driver.find_element_by_xpath('//*[@id="pass"]')
# 	# passwordInput.send_keys("password-0")
# 	# passwordInput.send_keys(Keys.RETURN)
# 	return driver

# def get_posts(profilepagedriver):
# 	for bb in range(0,20):
# 		profilepagedriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# 		time.sleep(5)
# 	arr = []
# 	p = profilepagedriver.find_elements_by_class_name('_5pcq')
# 	for i in range(0,len(p)):
# 		arr.append(p[i].get_attribute('href'))
# 		# print(p[i].get_attribute('href'))

# 	return arr

# def get_id(post):
# 	driver = webdriver.Firefox()
# 	driver.get(post)
# 	time.sleep(5)
# 	emailInput = driver.find_element_by_xpath('//*[@id="email"]')
# 	emailInput.send_keys("usama94naseer@gmail.com")
# 	passwordInput = driver.find_element_by_xpath('//*[@id="pass"]')
# 	passwordInput.send_keys("password-0")
# 	passwordInput.send_keys(Keys.RETURN)


# 	like_bar = driver.find_element_by_class_name('UFINoWrap').click()

# 	time.sleep(5)

# 	for bb in range(0,50):
# 		driver.find_element_by_class_name('clearfix').send_keys(Keys.PAGE_DOWN)
# 		# time.sleep(0.1)
# 	id_arr = []
# 	count = 0
# 	vec = driver.find_elements_by_class_name('fbProfileBrowserListItem')
# 	for i in range(0,len(vec)):
# 		count = count + 1
# 		a = vec[i].find_element_by_tag_name('a')
# 		b = a.get_attribute('data-hovercard')
# 		# print(count, ': ', b)
# 		s = str(b)
# 		s = s.split('=')[1]
# 		s = s.split('&')[0]
# 		print(s)
# 		id_arr.append(s)

# 	driver.quit()
# 	return id_arr

	
# def ids(url):
# 	# initial_browse_result
# 	count = 0
# 	driver = webdriver.Firefox()
# 	profilepagedriver = goAndLoginToFB(driver,url)

# 	time.sleep(5)

# 	for j in range(0,100):
# 		for bb in range(0,4):
# 			driver.find_element_by_id('initial_browse_result').send_keys(Keys.PAGE_DOWN)
# 			time.sleep(1)
# 		time.sleep(5)

# 	el = driver.find_element_by_id('initial_browse_result')
# 	el1 = el.find_elements_by_tag_name('div')
# 	arr = []
# 	for ind in range(0,len(el1)):
# 		try:
# 			if el1[ind].get_attribute('class') == "_3u1 _gli _5und":
# 				arr.append(el1[ind])
# 		except:
# 			pass

# 	for ind in range(0,len(arr)):
# 		try:
# 			st = arr[ind].get_attribute('data-bt')
# 			s1 = st.split(',')[0]
# 			s2 = s1.split(':')[1]
# 			print(s2)
# 		except:
# 			print(arr[ind].get_attribute('data-bt'))

	# driver.quit()

# def post_status():
# 	driver = webdriver.Firefox()
# 	driver.get("https://www.facebook.com/profile.php?id=100010417846650")
# 	time.sleep(2)
# 	emailInput = driver.find_element_by_xpath('//*[@id="email"]')
# 	emailInput.send_keys("bingchandlerbing2@gmail.com")
# 	passwordInput = driver.find_element_by_xpath('//*[@id="pass"]')
# 	passwordInput.send_keys("pass12345678")
# 	passwordInput.send_keys(Keys.RETURN)
# 	time.sleep(3)

# 	driver.find_element_by_xpath('//*[@id="blueBarNAXAnchor"]/div[1]/div/div/div[2]/ul/li[1]/a/span').click()
# 	# body = driver.find_element_by_tag_name("body")
# 	# body.send_keys(Keys.CONTROL + 't')
# 	# driver.get("https://www.facebook.com/profile.php?id=100010417846650")
# 	time.sleep(10)

# 	post = driver.find_element_by_xpath('//*[@id="js_2d"]/div[2]')
# 	status = "HELLYEAH"
# 	post.send_keys(status)
# 	driver.find_element_by_xpath('//*[@id="js_2d"]/div[4]/div[2]/div/div[2]/div/button/span').click()
# 	print('posted')
# 	time.sleep(5)




# if  __name__ =='__main__':

# 	post_status()

# 	driver = webdriver.Firefox()
# 	driver.get("http://www.f8-autoliker.com/")
	
# 	# body = driver.find_element_by_tag_name("body")
# 	# body.send_keys(Keys.CONTROL + 't')
# 	# driver.get("http://www.official-liker.net")
# 	submit_bar = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/form/div/input[1]')
# 	access_token = "https://www.facebook.com/connect/login_success.html#access_token=CAAAACZAVC6ygBABeZCBZCZBu6Odqua9D1p2NAAuLNKXpyui7LRdAjlNxpET2o5wkOm22S0EGkG1KkxQEGhJbM7Gs1ZBgfF75ScAZAJ0aszoZACBRtwboNkNZADIB0NZA7bclg7eZA8aXuZBROG0m0rz4diuiQ3821ZAz2MhWsRN9ECgt2mfb1n9U1TW7HvRchQHGig4vZAKe4FP1lHgZDZD&expires_in=0"
# 	submit_bar.send_keys(access_token)
# 	submit_bar.send_keys(Keys.RETURN)

# 	# driver.find_element_by_xpath('/html/body/div[1]/div/div/div/section/section[1]/form/input[2]').click()
# 	bar = driver.find_element_by_class_name('col-lg-12')
# 	form = bar.find_elements_by_tag_name('form')[0]
# 	form.find_elements_by_tag_name('input')[1].click()

