from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

job = 'software developer'#str(input('What job you are looking for: '))
location = 'india'#str(input('Please, Type in Location for which you are looking for : '))
driver = webdriver.Firefox()
driver.get('https://www.indeed.com')
search = driver.find_element_by_id('text-input-what')
search.send_keys(job)
search2 = driver.find_element_by_id('text-input-where')
search2.send_keys(location)
search2.send_keys(Keys.RETURN)
#links = driver.find_element(By.TAG_NAME,"a")
link = driver.find_elements_by_tag_name('a')
print(len(link))
for links in link:
    print(links.text)
#companies = driver.find_element_by_xpath("//a[@class='jobtitle turnstileLink visited']")
#print(companies)