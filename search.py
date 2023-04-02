from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

url = "https://www.instagram.com/login/"

browser = webdriver.Edge()
browser.get(url)

time.sleep(1)


#/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button
browser.find_element(By.NAME, 'username').send_keys('artistic_space8')
#browser.find_element(By.NAME, 'password').send_keys('password')
#WebDriverWait(browser,6).until(EC.element_to_be_clickable((By.XPATH,\
 #   '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button'))).click()


time.sleep(1)
browser.find_element(By.NAME, 'password').send_keys('tina19803', Keys.ENTER)
time.sleep(2)


WebDriverWait(browser,3).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div'))).click()


#/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/span/a
WebDriverWait(browser,3).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/span/a'))).click()


#/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]
WebDriverWait(browser,3).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]'))).click()



WebDriverWait(browser,3).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/a/div/div[1]'))).click()
time.sleep(3)

#/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input
browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input').send_keys('mostlysane',Keys.ENTER)
time.sleep(1000)