from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

if  __name__ =='__main__':
	driver = 0;
	try:
		print(1000)
		# driver = webdriver.Firefox()
		# driver = webdriver.Chrome()
		# driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
		driver = webdriver.Chrome(executable_path='C:\Python34\Scripts\chromedriver.exe')
		print(2000)
		# time.sleep(1)
		driver.get('http://www.goal.com/en-us/rumours/last/72')
		print(3000)
		time.sleep(2)
		driver.quit()
	except Exception as e:
		print(e)
		# driver.quit()
