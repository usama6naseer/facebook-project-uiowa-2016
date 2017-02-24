from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import time
import datetime
from time import gmtime, strftime
from html.parser import HTMLParser
import re
import json
import facebook as fb
import sys
import requests

def get_app_info(id):
	r = requests.get('http://graph.facebook.com/' + str(app_id))
	if r.status_code == 200:
		st = str(r.content, encoding='UTF-8')
		d = json.loads(st)
		# print (d['name'])
		# print (d['daily_active_users'])
		# print (d['daily_active_users_rank'])
		return (d['name'], d['daily_active_users'], d['daily_active_users_rank'])

def get_permissions(perm):
	data = perm['data']
	permissions_ = data[0]
	keylist = permissions_.keys()
	print(keylist)
	st = ''
	# if (keylist[0] == 'status' or keylist[1] == 'permission'):
	if 'status' in keylist:
		for i in range(0,len(perm['data'])):
			st =  st + str(perm['data'][i]['permission']) + ' '
	elif 'permission' in keylist:
		for i in range(0,len(perm['data'])):
			st =  st + str(perm['data'][i]['permission']) + ' '
	else:
		for key in keylist:
			st = st + str(key) + ' '
	return st

def makeApiCall(token,appid):
	try:
		print(token)
		perm_str = 'error while getting permissions'
		print(1)
		graph = fb.GraphAPI(access_token=token)
		perm = graph.get_object(id='me/permissions')
		print(2)
		# perm_str = perm;
		print(3)
		try:
			perm_str = get_permissions(perm)
			# print(perm_str)
		except Exception as e1:
			print("perm: ", e1)
			pass

		vec = []
		vec.append(appid)
		vec.append(perm)
		with open(('app_table_test.csv'), 'a', newline='', encoding='utf8') as f:
			writer = csv.writer(f)
			writer.writerow(vec)
		graph.delete_object(id='me/permissions')

		return (1, perm_str)
		# return (1,json.dumps(perm))
	except Exception as ee:
		temp = []
		#apli call not possible
		print(ee)
		# appid.append("No")
		# with open(('app_table_test.csv'), 'a', newline='', encoding='utf8') as f:
		# 	writer = csv.writer(f)
		# 	writer.writerow(appid)
		return (0,0)

def getToken(driver,appid):
	while 1==1:
		try:	
			okButton = driver.find_element_by_css_selector('._42ft._4jy0.layerConfirm._51_n.autofocus.uiOverlayButton._4jy5._4jy1.selected._51sy')
			okButton.click()
			time.sleep(1)
		except Exception as jh:
			break	
	time.sleep(3)
	try:		
		url = 'https://www.facebook.com/dialog/oauth?scope=ads_management,create_event,create_note,email,export_stream,friends_about_me,friends_activities,friends_birthday,friends_checkins,friends_education_history,friends_events,friends_games_activity,friends_groups,friends_hometown,friends_interests,friends_likes,friends_location,friends_notes,friends_online_presence,friends_photo_video_tags,friends_photos,friends_questions,friends_relationship_details,friends_relationships,friends_religion_politics,friends_status,friends_subscriptions,friends_videos,friends_website,friends_work_history,manage_friendlists,manage_notifications,manage_pages,photo_upload,publish_actions,publish_checkins,publish_stream,read_friendlists,read_insights,read_mailbox,read_page_mailboxes,read_requests,read_stream,rsvp_event,share_item,sms,status_update,user_about_me,user_activities,user_birthday,user_education_history,user_events,user_games_activity,user_groups,user_hometown,user_interests,user_likes,user_location,user_notes,user_online_presence,user_photo_video_tags,user_photos,user_questions,user_relationship_details,user_relationships,user_religion_politics,user_status,user_subscriptions,user_videos,user_website,user_work_history,video_upload,xmpp_login,offline_access,user_checkins&redirect_uri=https://www.facebook.com/connect/login_success.html&response_type=token&client_id='  + str(appid) + '&sso_key=com'
		driver.get(url)
		url = 'view-source:https://www.facebook.com/dialog/oauth?scope=ads_management,create_event,create_note,email,export_stream,friends_about_me,friends_activities,friends_birthday,friends_checkins,friends_education_history,friends_events,friends_games_activity,friends_groups,friends_hometown,friends_interests,friends_likes,friends_location,friends_notes,friends_online_presence,friends_photo_video_tags,friends_photos,friends_questions,friends_relationship_details,friends_relationships,friends_religion_politics,friends_status,friends_subscriptions,friends_videos,friends_website,friends_work_history,manage_friendlists,manage_notifications,manage_pages,photo_upload,publish_actions,publish_checkins,publish_stream,read_friendlists,read_insights,read_mailbox,read_page_mailboxes,read_requests,read_stream,rsvp_event,share_item,sms,status_update,user_about_me,user_activities,user_birthday,user_education_history,user_events,user_games_activity,user_groups,user_hometown,user_interests,user_likes,user_location,user_notes,user_online_presence,user_photo_video_tags,user_photos,user_questions,user_relationship_details,user_relationships,user_religion_politics,user_status,user_subscriptions,user_videos,user_website,user_work_history,video_upload,xmpp_login,offline_access,user_checkins&redirect_uri=https://www.facebook.com/connect/login_success.html&response_type=token&client_id=' + str(appid) + '&sso_key=com' 
		driver.get(url)
		time.sleep(1)	
		url_new = driver.current_url
		access_token = url_new[(url_new.find('access_token=')+13):(url_new.find('&expires_in'))]
		return access_token
	except Exception as ff:
		print(ff)	


def delete_app(driver):
	body = driver.find_element_by_tag_name("body")
	body.send_keys(Keys.CONTROL + 't')
	time.sleep(2)
	driver.get('https://www.facebook.com/settings?tab=applications')
	time.sleep(6)
	try:
		driver.find_element_by_xpath('//*[@id="u_2_1w"]').click()
	except Exception as e:
		print("1: ",e)
	time.sleep(3)
	try:
		driver.find_element_by_xpath('//*[@id="pop_content"]/div[1]/div[3]/div[1]/label[2]/input').click()
	except Exception as e:
		print("2: ",e)
	time.sleep(3)

def checkVul(driver,appid): 
	try:
		# valid app check
		r = requests.get('http://graph.facebook.com/' + str(appid))
		print (r.status_code)
		# print (r.headers)
		# print (r.content)
		if r.status_code == 200:
			print('valid')
		else:
			print('not valid')	
			return (-1,-1)
	except Exception as e:
		print('app not valid exception: ', e)
		return (-1,-1)

	try:
		#go to permission URL
		url = 'https://www.facebook.com/dialog/oauth?scope=ads_management,create_event,create_note,email,export_stream,friends_about_me,friends_activities,friends_birthday,friends_checkins,friends_education_history,friends_events,friends_games_activity,friends_groups,friends_hometown,friends_interests,friends_likes,friends_location,friends_notes,friends_online_presence,friends_photo_video_tags,friends_photos,friends_questions,friends_relationship_details,friends_relationships,friends_religion_politics,friends_status,friends_subscriptions,friends_videos,friends_website,friends_work_history,manage_friendlists,manage_notifications,manage_pages,photo_upload,publish_actions,publish_checkins,publish_stream,read_friendlists,read_insights,read_mailbox,read_page_mailboxes,read_requests,read_stream,rsvp_event,share_item,sms,status_update,user_about_me,user_activities,user_birthday,user_education_history,user_events,user_games_activity,user_groups,user_hometown,user_interests,user_likes,user_location,user_notes,user_online_presence,user_photo_video_tags,user_photos,user_questions,user_relationship_details,user_relationships,user_religion_politics,user_status,user_subscriptions,user_videos,user_website,user_work_history,video_upload,xmpp_login,offline_access,user_checkins&redirect_uri=https://www.facebook.com/connect/login_success.html&response_type=token&client_id='  + appid + '&sso_key=com' 
		driver.get(url)
		time.sleep(6);
		#check if redirect successful
		exdiv = driver.find_element_by_xpath('//*[@id="u_0_p"]/div[1]/div/div/div/div[1]/div[1]/div[2]')
		token = getToken(driver,appid)
		apiVul, perm = makeApiCall(token,appid)
		return (1,apiVul,perm)
	except Exception as eee:
		print("1: ", eee)
		try:
			#check if redirect successful
			# time.sleep(2);
			exdiv = driver.find_element_by_xpath('//*[@id="platformDialogForm"]/div[1]/div[1]/div[1]/div[2]')
			token = getToken(driver,appid)
			apiVul,perm = makeApiCall(token,appid)
			return (1,apiVul,perm)	
		except Exception as wee:
			print("2: ", wee)
			try:
				# time.sleep(2);
				exdiv = driver.find_element_by_xpath('//*[@id="u_0_q"]/div[1]/div/div/div/div[1]/div[1]/div[2]')
				# exdiv = driver.find_element_by_xpath('//*[@id="platformDialogForm"]')
				token = getToken(driver,appid)
				apiVul,perm = makeApiCall(token,appid)
				return (1,apiVul,perm)	
			except Exception as weeee:
				print("3: ", weeee)
				cur_url = driver.current_url
				if cur_url == 'https://www.facebook.com/connect/blank.html#_=_':
					token = getToken(driver,appid)
					apiVul, perm = makeApiCall(token,appid)
					return (1,apiVul,perm)
				return(0,0,0)



if  __name__ =='__main__':
	firefox_profile = webdriver.FirefoxProfile()
	firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
	driver = webdriver.Firefox(firefox_profile=firefox_profile)
	# driver = webdriver.Chrome(executable_path='C:\Python34\Scripts\chromedriver.exe')	
	driver.get("http://www.facebook.com")
	emailInput = driver.find_element_by_xpath('//*[@id="email"]')
	emailInput.send_keys("chotaBilal@mail.com")
	passwordInput = driver.find_element_by_xpath('//*[@id="pass"]')
	passwordInput.send_keys("pass12345678")
	passwordInput.send_keys(Keys.RETURN)	
	time.sleep(1)
	app_id = 0
	with open('app-id.csv', newline='', encoding='utf8') as f:
		reader = csv.reader(f)
		for row in reader:
			app_id = row[0]
	print("app_id is: ", app_id) 
	redirectVul, apiVul, perm = checkVul(driver,app_id)
	print(4)
	name, dau, daur = get_app_info(app_id)
	print(5)
	driver.quit()

	arr = []
	arr.append(redirectVul)
	arr.append(apiVul)
	arr.append(app_id)
	arr.append(name)
	arr.append(dau)
	arr.append(daur)
	arr.append(perm)
	print(arr)

	fname = str(app_id) + '.csv'
	with open(fname, 'w', newline='', encoding='utf8') as f:
		writer = csv.writer(f)
		writer.writerow(arr)

	arr = []
	arr.append(app_id)
	arr.append(name)
	arr.append(dau)
	arr.append(daur)
	arr.append(redirectVul)
	arr.append(apiVul)

	# day = datetime.datetime.now().date()
	day = strftime("%Y-%m-%d %H:%M:%S", gmtime())
	arr.append(day)
	arr.append(perm)
	print(arr)

	# array = []
	# array.append(arr)
	# with open('app-record.csv', newline='', encoding='utf8') as f1:
	# 	reader = csv.reader(f1)
	# 	for row in reader:
	# 		array.append(row)
	with open(('app-record.csv'), 'a', newline='', encoding='utf8') as f:
		writer = csv.writer(f)
		writer.writerow(arr)

	# print (redirectVul)
	# print (apiVul)	


https://www.facebook.com/dialog/oauth?scope=ads_management,create_event,create_note,email,export_stream,friends_about_me,friends_activities,friends_birthday,friends_checkins,friends_education_history,friends_events,friends_games_activity,friends_groups,friends_hometown,friends_interests,friends_likes,friends_location,friends_notes,friends_online_presence,friends_photo_video_tags,friends_photos,friends_questions,friends_relationship_details,friends_relationships,friends_religion_politics,friends_status,friends_subscriptions,friends_videos,friends_website,friends_work_history,manage_friendlists,manage_notifications,manage_pages,photo_upload,publish_actions,publish_checkins,publish_stream,read_friendlists,read_insights,read_mailbox,read_page_mailboxes,read_requests,read_stream,rsvp_event,share_item,sms,status_update,user_about_me,user_activities,user_birthday,user_education_history,user_events,user_games_activity,user_groups,user_hometown,user_interests,user_likes,user_location,user_notes,user_online_presence,user_photo_video_tags,user_photos,user_questions,user_relationship_details,user_relationships,user_religion_politics,user_status,user_subscriptions,user_videos,user_website,user_work_history,video_upload,xmpp_login,offline_access,user_checkins&redirect_uri=https://www.facebook.com/connect/login_success.html&response_type=token&client_id=41158896424

https://www.facebook.com/dialog/oauth?scope=ads_management,create_event,create_note,email,export_stream,friends_about_me,friends_activities,friends_birthday,friends_checkins,friends_education_history,friends_events,friends_games_activity,friends_groups,friends_hometown,friends_interests,friends_likes,friends_location,friends_notes,friends_online_presence,friends_photo_video_tags,friends_photos,friends_questions,friends_relationship_details,friends_relationships,friends_religion_politics,friends_status,friends_subscriptions,friends_videos,friends_website,friends_work_history,manage_friendlists,manage_notifications,manage_pages,photo_upload,publish_actions,publish_checkins,publish_stream,read_friendlists,read_insights,read_mailbox,read_page_mailboxes,read_requests,read_stream,rsvp_event,share_item,sms,status_update,user_about_me,user_activities,user_birthday,user_education_history,user_events,user_games_activity,user_groups,user_hometown,user_interests,user_likes,user_location,user_notes,user_online_presence,user_photo_video_tags,user_photos,user_questions,user_relationship_details,user_relationships,user_religion_politics,user_status,user_subscriptions,user_videos,user_website,user_work_history,video_upload,xmpp_login,offline_access,user_checkins&redirect_uri=https://www.facebook.com/connect/login_success.html&response_type=token&client_id=162729813767876

https://www.facebook.com/dialog/oauth?scope=ads_management,create_event,create_note,email,export_stream,friends_about_me,friends_activities,friends_birthday,friends_checkins,friends_education_history,friends_events,friends_games_activity,friends_groups,friends_hometown,friends_interests,friends_likes,friends_location,friends_notes,friends_online_presence,friends_photo_video_tags,friends_photos,friends_questions,friends_relationship_details,friends_relationships,friends_religion_politics,friends_status,friends_subscriptions,friends_videos,friends_website,friends_work_history,manage_friendlists,manage_notifications,manage_pages,photo_upload,publish_actions,publish_checkins,publish_stream,read_friendlists,read_insights,read_mailbox,read_page_mailboxes,read_requests,read_stream,rsvp_event,share_item,sms,status_update,user_about_me,user_activities,user_birthday,user_education_history,user_events,user_games_activity,user_groups,user_hometown,user_interests,user_likes,user_location,user_notes,user_online_presence,user_photo_video_tags,user_photos,user_questions,user_relationship_details,user_relationships,user_religion_politics,user_status,user_subscriptions,user_videos,user_website,user_work_history,video_upload,xmpp_login,offline_access,user_checkins&redirect_uri=https://www.facebook.com/connect/login_success.html&response_type=token&client_id=