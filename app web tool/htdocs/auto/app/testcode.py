from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import time
from html.parser import HTMLParser
import re
import json
import facebook as fb
import sys


def makeApiCall(token,appid):
	try:
		print(token)
		graph = fb.GraphAPI(access_token=token)
		# get permissions
		perm = graph.get_object(id='me/permissions')
		appid.append(perm)
		#write permissions to file
		with open(('app_table_test.csv'), 'a', newline='', encoding='utf8') as f:
			writer = csv.writer(f)
			writer.writerow(appid)		
	except Exception as ee:
		temp = []
		#apli call not possible
		print(ee)
		appid.append("No")
		with open(('app_table_test.csv'), 'a', newline='', encoding='utf8') as f:
			writer = csv.writer(f)
			writer.writerow(appid)

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

if  __name__ =='__main__':
	# firefox_profile = webdriver.FirefoxProfile()
	# firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
	# driver = webdriver.Firefox(firefox_profile=firefox_profile)
	driver = webdriver.Chrome(executable_path='C:\Python34\Scripts\chromedriver.exe')	
	driver.get("http://www.facebook.com")
	emailInput = driver.find_element_by_xpath('//*[@id="email"]')
	emailInput.send_keys("chotaBilal@mail.com")
	passwordInput = driver.find_element_by_xpath('//*[@id="pass"]')
	passwordInput.send_keys("pass12345678")
	passwordInput.send_keys(Keys.RETURN)	
	time.sleep(5)	
	with open('app_data_1000.csv', newline='', encoding='utf8') as f:
			tmp = []
			reader = csv.reader(f)
			for header in reader: 
				try:
					print("*******************************************")
					print(header)
					print("*******************************************")
					#go to permission URL
					url = 'https://www.facebook.com/dialog/oauth?scope=ads_management,create_event,create_note,email,export_stream,friends_about_me,friends_activities,friends_birthday,friends_checkins,friends_education_history,friends_events,friends_games_activity,friends_groups,friends_hometown,friends_interests,friends_likes,friends_location,friends_notes,friends_online_presence,friends_photo_video_tags,friends_photos,friends_questions,friends_relationship_details,friends_relationships,friends_religion_politics,friends_status,friends_subscriptions,friends_videos,friends_website,friends_work_history,manage_friendlists,manage_notifications,manage_pages,photo_upload,publish_actions,publish_checkins,publish_stream,read_friendlists,read_insights,read_mailbox,read_page_mailboxes,read_requests,read_stream,rsvp_event,share_item,sms,status_update,user_about_me,user_activities,user_birthday,user_education_history,user_events,user_games_activity,user_groups,user_hometown,user_interests,user_likes,user_location,user_notes,user_online_presence,user_photo_video_tags,user_photos,user_questions,user_relationship_details,user_relationships,user_religion_politics,user_status,user_subscriptions,user_videos,user_website,user_work_history,video_upload,xmpp_login,offline_access,user_checkins&redirect_uri=https://www.facebook.com/connect/login_success.html&response_type=token&client_id='  + header[0] + '&sso_key=com' 
					driver.get(url)
					time.sleep(2);
					#check if redirect successful
					exdiv = driver.find_element_by_xpath('//*[@id="u_0_m"]/div[1]/div/div/div/div[1]/div[1]/div[2]')
					token = getToken(driver,header[0])
					makeApiCall(token,header)
				except Exception as eee:
					try:
						#check if redirect successful
						exdiv = driver.find_element_by_xpath('//*[@id="platformDialogForm"]/div[1]/div[1]/div[1]/div[2]')
						token = getToken(driver,header[0])
						makeApiCall(token,header)	
					except Exception as wee:
						#redirect not successful
						token = getToken(driver,header[0])
						makeApiCall(token,header)
						continue	