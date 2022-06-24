from selenium import webdriver
from details import email,pas
import time
import os
import webbrowser

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://accounts.google.com/ServiceLogin/identifier?service')

user = driver.find_element_by_id('identifierId')
user.send_keys(email)

nt = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button')
nt.click()

'''
password = driver.find_element_by_id('pass')
password.send_keys(pas)


button = driver.find_element_by_id('loginbutton')
button.submit()

time.sleep(10)

body = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/div[2]/span/div/div[1]')
body.click()

time.sleep(5)

body1 = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div[1]/div[1]/div[2]/div/div[3]/div[1]/div/a/div[1]/div[2]/div[1]/div/div/div[2]/span/span/div/span[1]/span')
body1.click()


time.sleep(5)

message = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')
message.send_keys("hlo")

time.sleep(10)

send = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/form/div/div[3]/span[2]/div')
send.click()

account = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/span/div/div[1]')
account.click()

time.sleep(10)

logout = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div[4]/div/div[1]/div[2]/div')
logout.click()
'''
#driver.close()
