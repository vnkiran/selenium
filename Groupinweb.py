from selenium import webdriver
from secrete import email,pas
import time
import os
import webbrowser
#link = 'https://www.google.com/'
#webbrowser.open(link)

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://groupin.app/')



company = driver.find_element_by_xpath('/html/body/header/div/nav/div[2]/div[1]/ul/li[4]/a')
company.click()

team = driver.find_element_by_xpath('/html/body/header/div/nav/div[2]/div[1]/ul/li[4]/ul/li/div/div/div[3]/ul/li/a/h3')
team.click()

time.sleep(5)

chrmn = driver.find_element_by_xpath('/html/body/section[2]/div/div/div[2]/div/button')
chrmn.click()

time.sleep(5)

rclose= driver.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/button/span')
rclose.click()
time.sleep(10)
'''
cofnr= driver.find_element_by_xpath('/html/body/section[3]/div/div/div[1]/div/button')
cofnr.click()


time.sleep(5)

crclose = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/button/span')
crclose.click()
time.sleep(10)


time.sleep(5)

message = driver.find_element_by_xpath('')
message.send_keys("")

time.sleep(10)

send = driver.find_element_by_xpath('')
send.click()

account = driver.find_element_by_xpath('')
account.click()

time.sleep(10)

logout = driver.find_element_by_xpath('')
logout.click()
'''
#driver.close()
