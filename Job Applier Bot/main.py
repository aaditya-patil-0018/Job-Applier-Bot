from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup as bs

#This is information needed for working the code
job = str(input('What job you are looking for: '))
location = str(input('Please, Type in Location for which you are looking for : '))
email = str(input('Type your email here : '))
password = str(input('Type your indeed password : '))

# This will start the browser
driver = webdriver.Firefox()	

# This is for signing in
driver.get('https://secure.indeed.com/account/login')


e_mail = driver.find_element_by_id('login-email-input')
e_mail.send_keys(email)	
passw = driver.find_element_by_id('login-password-input')
passw.send_keys(password)
driver.find_element_by_id('login-submit-button').click()

time.sleep(2)
try:
	driver.find_element_by_class_name('gnav-Logo-icon').click()
except Exception:
	print('You maybe Trapped in Captcha. Just Type in Done!')
	done = str(input('Type Beside this when you are done : '))
	while done == None:
		time.sleep()
	driver.find_element_by_id('login-password-input')
	passw.send_keys(password)
	time.sleep(2)
	driver.find_element_by_class_name('gnav-Logo-icon').click()

time.sleep(2)
search = driver.find_element_by_id('text-input-what')
search.send_keys(job)
search2 = driver.find_element_by_id('text-input-where')
search2.send_keys(location)
search2.send_keys(Keys.RETURN)

time.sleep(5)

job_list = driver.find_elements_by_xpath("//div[@data-tn-component='organicJob']")
for each_job in job_list:
    job_title = each_job.find_elements_by_xpath(".//h2[@class='title']/a")[0]
    job_title.click()
    time.sleep(4)
    job_apply = each_job.find_elements_by_id("apply-button-container")
    try:
    	a = driver.find_element_by_class_name("indeed-apply-button").click()
    	time.sleep(10)
    	b = driver.find_element_by_id('form-action-continue').click()
    	print('Done')
    	driver.back()
    	time.sleep(1)
    except Exception:
    	print('This is not onsite Apply Job!')
driver.quit()